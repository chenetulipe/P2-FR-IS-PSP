import json

with open('suspicious_all_6.json', 'r', encoding='utf-8') as f:
    suspicious = json.load(f)

with open('traduction/MMAP03.json', 'r', encoding='utf-8') as f:
    mmap03 = json.load(f)

mmap_dict = {item['id']: item for item in mmap03 if 'id' in item}

with open('analysis_utf8.txt', 'w', encoding='utf-8') as out:
    for idx, s in enumerate(suspicious):
        sid = s['id']
        orig = s['orig']
        fr = s['fr']
        out.write(f"==================================================\n")
        out.write(f"INDEX: {idx} | ID: {sid}\n")
        out.write(f"ORIG: {repr(orig)}\n")
        out.write(f"FR  : {repr(fr)}\n")
        for offset in range(-2, 3):
            target_id = sid + offset
            if target_id in mmap_dict:
                m = mmap_dict[target_id]
                out.write(f"  [MMAP03 id={target_id}] name={m.get('nom_orig')} | orig={repr(m.get('texte_orig'))}\n         fr_name={m.get('nom_fr')} | fr={repr(m.get('texte_fr'))}\n")
