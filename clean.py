import json
import re

with open('suspicious_0.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cleaned = []

for item in data:
    orig = item['orig']
    fr = item['fr']
    
    # 1. Clean the garbage
    garbage_patterns = [
        r"(\s*Poster de l'actrice.*)",
        r"(\s*Machine(\s|\n)*#\d+ de\s*la rangée.*)",
        r"(\s*Machine de blackjack.*)",
        r"(\s*Le casier contient.*)",
        r"(\s*Ordre de la Sainte Lance.*)",
        r"(\s*Le stock de Personae.*)",
        r"(\s*Le corps de\s*Fujii.*)",
        r"(\s*Quelque chose est écrit.*)",
        r"(\s*Machine\s*#\d+ de\s*la rangée.*)"
    ]
    
    garbage = ""
    fr_clean = fr
    for pattern in garbage_patterns:
        match = re.search(pattern, fr_clean, flags=re.DOTALL)
        if match:
            garbage = match.group(1).lstrip()
            fr_clean = fr_clean[:match.start()]
            break
            
    # 2. Split if > 2 lines
    lines = fr_clean.split('\n')
    if len(lines) > 2:
        new_lines = []
        for i in range(0, len(lines), 2):
            new_lines.append('\n'.join(lines[i:i+2]))
        fr_clean = '[1205][000A]'.join(new_lines)
        
    cleaned.append({
        "file": item["file"],
        "id": item["id"],
        "fr_cleaned": fr_clean,
        "garbage_removed": garbage
    })

with open('cleaned_0.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)
