#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P2IS FR Tool  ·  Persona 2 Innocent Sin PSP (EUR ULES01557)
============================================================
Module spécialisé pour le parsing et l'encodage des fichiers MMAP01-06.BNP.

Les fichiers MMAP (carte du monde, dialogues de PNJ par zone) utilisent un
format binaire propre différent de l'event.bin :

  - Format conteneur : MIG.00.1PSP (format propriétaire Atlus)
  - Terminateur de dialogue MMAP : 
      Variante 1: [0x1106][0x1102][0x1103][0x1431][0x0000][0x0000] (12 octets)
      Variante 2: [0x1106][0x1102][0x1431][0x0000][0x0000] (10 octets)
  - Pas de zéros de padding entre dialogues : slot_size == data_size
  - Les dialogues sont contigus dans la zone de données du BNP

Ce module gère correctement ces spécificités ainsi que l'alignement
des menus de choix pour éviter les crashs.
"""

import struct, json, re
from pathlib import Path
from src.config import *
from src.core.text import decode_text, text_to_bytes, _align_menu_text

# ── Terminateurs spécifiques MMAP ───────────────────────────────────────────────
MMAP_TERM_1 = [0x1106, 0x1102, 0x1103, 0x1431, 0x0000, 0x0000]
MMAP_TERM_2 = [0x1106, 0x1102, 0x1431, 0x0000, 0x0000]

MMAP_TERM_1_BYTES = b''.join(struct.pack('<H', w) for w in MMAP_TERM_1)
MMAP_TERM_2_BYTES = b''.join(struct.pack('<H', w) for w in MMAP_TERM_2)

# Codes de contrôle à nettoyer du texte extrait
_CTRL_MMAP = {
    0x1101: '[NL]', 0x1102: '[E2]', 0x1103: '[E3]', 0x1104: '[E4]',
    0x1106: '[1106]', 0x1109: '[1109]', 0x1120: '[SP]',
    0x1113: '[1113]', 0x1112: '[1112]', 0x1208: '[1208]', 0x1205: '[1205]',
    0x1431: '[1431]',
}

def _valid_mmap_name(data: bytes, offset: int) -> bool:
    j = offset + 2
    if j + 1 >= len(data):
        return False
    first = struct.unpack_from('<H', data, j)[0]
    if first == SP:
        return False
    chars = []
    pr = al = uk = 0
    while j < len(data) - 1:
        cp = struct.unpack_from('<H', data, j)[0]
        if cp == NL:
            n = len(chars)
            if not (1 <= n <= 40):
                return False
            return al >= 1 and (pr / max(1, n)) >= 0.6
        if 0x20 <= cp <= 0x7E:
            pr += 1
            al += 0x41 <= cp <= 0x7A
        elif cp == SP:
            pr += 1
        else:
            uk += 1
        if uk > 2:
            return False
        chars.append(cp)
        if len(chars) > 40:
            return False
        j += 2
    return False

def _decode_mmap_text(raw: bytes) -> str:
    out = ""
    for i in range(0, len(raw) - 1, 2):
        cp = struct.unpack_from('<H', raw, i)[0]
        if cp in _CTRL_MMAP:
            out += _CTRL_MMAP[cp]
        elif 0x20 <= cp <= 0x7E:
            out += chr(cp)
        elif 0x80 <= cp <= 0xFF:
            out += chr(cp)
        else:
            out += f'[U+{cp:04X}]'
    return out

def scan_mmap_bnp(data: bytes, stem: str, out_dir: Path, log_fn) -> int:
    dialogs = []
    i = 0

    while i < len(data) - 1:
        w = struct.unpack_from('<H', data, i)[0]
        if w != 0x0022 or not _valid_mmap_name(data, i):
            i += 2
            continue

        start = i
        
        # Chercher le terminateur MMAP à partir de start
        idx1 = data.find(MMAP_TERM_1_BYTES, start + 2)
        idx2 = data.find(MMAP_TERM_2_BYTES, start + 2)
        
        if idx1 == -1 and idx2 == -1:
            i += 2
            continue
            
        # Prendre le plus proche
        if idx1 != -1 and (idx2 == -1 or idx1 < idx2):
            term_idx = idx1
            term_seq = MMAP_TERM_1
            term_bytes = MMAP_TERM_1_BYTES
        else:
            term_idx = idx2
            term_seq = MMAP_TERM_2
            term_bytes = MMAP_TERM_2_BYTES

        if term_idx > start + 4000:
            i += 2
            continue

        end = term_idx + len(term_bytes)

        raw_text = data[start:term_idx]
        full_text = _decode_mmap_text(raw_text)

        lines = full_text.split('[NL]')
        nom = lines[0].lstrip('"') if lines else ''
        body = '[NL]'.join(lines[1:]) if len(lines) > 1 else ''
        body_clean = body.strip()

        entry = {
            'id': len(dialogs),
            'offset': start,
            'data_size': end - start,
            'slot_size': end - start,
            '_term': term_seq,
            'nom_orig': nom,
            'texte_orig': body_clean,
            'nom_fr': '',
            'texte_fr': '',
        }
        dialogs.append(entry)
        i = end

    if not dialogs:
        if log_fn:
            log_fn(f'  {stem.upper()}: aucun dialogue trouvé', 'warn')
        return 0

    out_path = out_dir / f'{stem.upper()}.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(dialogs, f, ensure_ascii=False, indent=2)

    if log_fn:
        log_fn(f'  {stem.upper()}: {len(dialogs)} dialogues -> {out_path.name}', 'ok')
    return len(dialogs)


def encode_mmap_bnp_from_json(
    bin_path: str, json_path: str, log_fn, out_path: str = None
) -> str:
    data = bytearray(open(bin_path, 'rb').read())
    dlgs = json.loads(open(json_path, encoding='utf-8').read(), strict=False)

    ok = skip = kept = 0
    nl_bytes = struct.pack('<H', NL)

    for d in dlgs:
        n_fr = d.get('nom_fr', '').strip()
        t_fr = d.get('texte_fr', '').strip()

        if not n_fr and not t_fr:
            kept += 1
            continue

        n_fr = n_fr or d.get('nom_orig', '').replace('[SP]', ' ').strip()
        t_fr = t_fr or d.get('texte_orig', '').strip()
        n_orig = d.get('nom_orig', '')
        t_orig = d.get('texte_orig', '')

        # Alignement des menus de choix pour éviter les crashs
        t_fr = _align_menu_text(n_orig, t_orig, n_fr, t_fr)

        enc = text_to_bytes('"' + n_fr + '\n' + t_fr)

        # Terminateur exact du JSON
        term_seq = d.get('_term', MMAP_TERM_1)
        term_bytes = b''.join(struct.pack('<H', w) for w in term_seq)
        
        avail = d['data_size'] - len(term_bytes) - 2  # -2 pour le [NL] final

        if len(enc) > avail:
            depassement = len(enc) - avail
            if log_fn:
                log_fn(
                    f'  [!] [MMAP] [id {d["id"]}] Texte FR trop long de {depassement} '
                    f'octets. Troncature automatique.',
                    'warn'
                )
            tokens = re.split(r'(\[[a-zA-Z0-9+\-_]+\]|\s)', t_fr)
            tokens = [t for t in tokens if t]
            while tokens and len(text_to_bytes('"' + n_fr + '\n' + ''.join(tokens))) > avail:
                tokens.pop()
            t_fr = ''.join(tokens)
            enc = text_to_bytes('"' + n_fr + '\n' + t_fr)

        # Construire la séquence sans padding interne
        full = enc + nl_bytes + term_bytes

        # Vérifier si on dépasse la taille
        if len(full) > d['slot_size']:
            # Normalement géré par la troncature plus haut, mais sécurité au cas où
            full = full[:d['slot_size'] - len(term_bytes)] + term_bytes
        
        # Padding avec des zéros APRÈS le terminateur
        # Cela évite que le jeu parse des espaces infinis et freeze les bulles de dialogue
        pad_len = d['slot_size'] - len(full)
        if pad_len > 0:
            full += b'\x00' * pad_len

        if len(full) != d['slot_size']:
            if log_fn:
                log_fn(
                    f'  [!] [MMAP] [id {d["id"]}] Taille incorrecte: '
                    f'{len(full)} != {d["slot_size"]}. Ignore.',
                    'warn'
                )
            skip += 1
            continue

        data[d['offset']:d['offset'] + d['slot_size']] = full
        ok += 1

    if out_path is None:
        out_path = bin_path

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'wb') as f:
        f.write(data)

    if log_fn:
        log_fn(
            f'  [MMAP] {ok} traduits | {skip} ignores | {kept} conserves '
            f'-> {Path(out_path).name}',
            'ok'
        )
    return out_path
