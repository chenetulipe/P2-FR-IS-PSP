import json

def process():
    with open('suspicious_3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    out = []
    for item in data:
        fr = item['fr']
        garbage = ""
        
        # known garbage
        if "C'est un modèle de" in fr:
            idx = fr.find("C'est un modèle de")
            garbage = fr[idx:]
            fr = fr[:idx].strip()
        elif "[E3]\nMaya affronta le plat" in fr:
            idx = fr.find("[E3]\nMaya affronta")
            garbage = fr[idx:]
            fr = fr[:idx].strip()
        elif "attire les 05]les ennuis" in fr:
            fr = fr.replace("05]les ", "[1205][000F]")
        elif "mes goûts [1205][000F]restent" in fr:
            pass
        elif "L'enjeu, 00F]L'enjeu, c'est" in fr:
            fr = fr.replace("L'enjeu, 00F]", "[1205][000F]")
        elif "aller à l'usineabandonnée" in fr:
            fr = fr.replace("usineabandonnée", "usine abandonnée")
        elif "ne pas tropgaspiller" in fr:
            fr = fr.replace("tropgaspiller", "trop gaspiller")
        elif "pourvoir" in fr and "pour voir" not in fr:
            fr = fr.replace("pourvoir", "pour voir")
        elif "ferabombarder" in fr:
            fr = fr.replace("ferabombarder", "fera bombarder")
        elif "qu'ilveut" in fr:
            fr = fr.replace("qu'ilveut", "qu'il veut")
        elif "partieinfiltrer" in fr:
            fr = fr.replace("partieinfiltrer", "partie infiltrer")
        elif "ététouchée" in fr:
            fr = fr.replace("ététouchée", "été touchée")
        elif "auraientpéri" in fr:
            fr = fr.replace("auraientpéri", "auraient péri")
        elif "somespecial" in fr:
            fr = fr.replace("somespecial", "some special")
        elif "latienne" in fr:
            fr = fr.replace("latienne", "la tienne")
        elif "appétitrevient" in fr:
            fr = fr.replace("appétitrevient", "appétit revient")
        elif "invisiblesdans" in fr:
            fr = fr.replace("invisiblesdans", "invisibles dans")
        elif "unerumeur" in fr:
            fr = fr.replace("unerumeur", "une rumeur")
        elif "àKismet" in fr:
            fr = fr.replace("àKismet", "à Kismet")
        elif "s'ilsse" in fr:
            fr = fr.replace("s'ilsse", "s'ils se")
        elif "chezelle" in fr:
            fr = fr.replace("chezelle", "chez elle")
        elif "aupire" in fr:
            fr = fr.replace("aupire", "au pire")
        elif "notresélection" in fr:
            fr = fr.replace("notresélection", "notre sélection")
        elif "debombes" in fr:
            fr = fr.replace("debombes", "de bombes")
            
        
        lines = fr.split('\n')
        chunks = []
        for i in range(0, len(lines), 2):
            chunks.append('\n'.join(lines[i:i+2]))
        
        fr_cleaned = '[1205][000A]'.join(chunks)
        
        out.append({
            "file": item["file"],
            "id": item["id"],
            "fr_cleaned": fr_cleaned,
            "garbage_removed": garbage
        })
        
    with open('cleaned_3.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

process()
