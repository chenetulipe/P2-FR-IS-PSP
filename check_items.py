import json

with open('suspicious_all_6.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('items_dump_utf8.txt', 'w', encoding='utf-8') as out:
    for i, it in enumerate(items):
        out.write(f"=== #{i:02d} ID:{it['id']} ===\n")
        out.write(f"ORIG: {repr(it['orig'])}\n")
        out.write(f"FR  : {repr(it['fr'])}\n\n")
