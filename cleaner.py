import json

with open('C:\\Users\\nolan\\Desktop\\6666666656\\repo\\suspicious_5.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out = []
for d in data:
    fr = d['fr']
    garbage = ""
    if d['id'] == 7 and d['file'] == 'script_387.json':
        garbage = " Se téléporter à Seven?[SP][SP] OuiNon"
        fr = fr.replace(garbage, "")
    
    # split > 2 lines
    lines = fr.split('\n')
    if len(lines) > 2:
        chunks = []
        for i in range(0, len(lines), 2):
            chunks.append('\n'.join(lines[i:i+2]))
        fr_cleaned = '[1205][000A]'.join(chunks)
    else:
        fr_cleaned = fr
        
    out.append({
        "file": d["file"],
        "id": d["id"],
        "fr_cleaned": fr_cleaned,
        "garbage_removed": garbage
    })

with open('C:\\Users\\nolan\\Desktop\\6666666656\\repo\\cleaned_5.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
