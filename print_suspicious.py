import json

with open('suspicious_all_6.json', 'r', encoding='utf-8') as f:
    suspicious = json.load(f)

for i, item in enumerate(suspicious):
    print(f"=== [{i}] id={item['id']} ===")
    print("ORIG:", item['orig'].replace('\n', '\\n'))
    print("FR  :", item['fr'].replace('\n', '\\n'))
