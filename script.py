import json

with open('suspicious_all_3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cleaned_data = []

for i, item in enumerate(data):
    file_name = item['file']
    item_id = item['id']
    orig = item['orig']
    fr = item['fr']
    
    # Special handling for choice menu garbage in items 6 & 8
    if file_name == 'MMAP01.json' and item_id in (334, 348):
        # "[1113]-kun ?[1205][000F] On devrait chercher par ici ?\n[NULL][NULL]Ouais, jetons un œil..."
        fr_clean = "[1113]-kun ?[1205][000F] On devrait chercher par ici ?"
        # garbage is everything after fr_clean
        garbage = fr[len(fr_clean):].strip()
    else:
        parts = fr.split('[NL]')
        fr_clean = parts[0].strip()
        garbage = '[NL]'.join(parts[1:]).strip() if len(parts) > 1 else ""
    
    cleaned_data.append({
        "file": file_name,
        "id": item_id,
        "fr_cleaned": fr_clean,
        "garbage_removed": garbage
    })

with open('cleaned_all_3.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated cleaned_all_3.json with {len(cleaned_data)} items.")











