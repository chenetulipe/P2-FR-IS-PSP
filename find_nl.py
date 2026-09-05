import json, glob

for fn in sorted(glob.glob('cleaned_*.json')):
    idx = fn.split('_')[1].split('.')[0]
    with open(fn, 'r', encoding='utf-8') as f_cl, open(f'suspicious_{idx}.json', 'r', encoding='utf-8') as f_sp:
        cl = json.load(f_cl)
        sp = json.load(f_sp)
    for c, s in zip(cl, sp):
        if '[NL]' in s['fr']:
            cid = c['id']
            print(f"=== {fn} id={cid} ===")
            print("ORIG    :", repr(s['orig']))
            print("SUSP_FR :", repr(s['fr']))
            print("CLEANED :", repr(c['fr_cleaned']))
            print("GARBAGE :", repr(c.get('garbage_removed')))
