import json

with open('suspicious_all_6.json', 'r', encoding='utf-8') as f:
    suspicious = json.load(f)

cleaned_items = [
    # 0: ID 101
    {
        "file": "MMAP03.json",
        "id": 101,
        "fr_cleaned": "Des boutiques qui vendent des armures ?\nDes restaurants qui vendent des armes ?\nCette ville devient folle."
    },
    # 1: ID 102
    {
        "file": "MMAP03.json",
        "id": 102,
        "fr_cleaned": "Rosa Candida à Aoba :\nbonne qualité, cher."
    },
    # 2: ID 104
    {
        "file": "MMAP03.json",
        "id": 104,
        "fr_cleaned": "Rosa Candida à Aoba : prix corrects,\nmais qualité insuffisante."
    },
    # 3: ID 105
    {
        "file": "MMAP03.json",
        "id": 105,
        "fr_cleaned": "Des boutiques qui vendent des armures ?\nDes restaurants qui vendent des armes ?\nCette ville devient folle."
    },
    # 4: ID 106
    {
        "file": "MMAP03.json",
        "id": 106,
        "fr_cleaned": "Rosa Candida à Aoba :\ngrand choix, reprises basses."
    },
    # 5: ID 107
    {
        "file": "MMAP03.json",
        "id": 107,
        "fr_cleaned": "Des boutiques qui vendent des armures ?\nDes restaurants qui vendent des armes ?\nCette ville devient folle."
    },
    # 6: ID 113
    {
        "file": "MMAP03.json",
        "id": 113,
        "fr_cleaned": "Je n'ai jamais gagné de concours.[1205][000F]\nMais gagner donne de vraies armes et objets."
    },
    # 7: ID 115
    {
        "file": "MMAP03.json",
        "id": 115,
        "fr_cleaned": "Jamais gagné de concours.[1205][000F]\nMais gagner donne de vraies armes et objets."
    },
    # 8: ID 117
    {
        "file": "MMAP03.json",
        "id": 117,
        "fr_cleaned": "Jamais gagné de concours.[1205][000F]\nMais gagner donne de vraies armes et objets."
    },
    # 9: ID 119
    {
        "file": "MMAP03.json",
        "id": 119,
        "fr_cleaned": "Jamais intéressé par les arcades,\nmais Mu a un casino maintenant.[1205][000F] L'idée\nde jouer m'excite..."
    },
    # 10: ID 120
    {
        "file": "MMAP03.json",
        "id": 120,
        "fr_cleaned": "Un ami y est allé.[1205][000F] On peut gagner gros à la\nmachine de poker n°5. Je ne sais pas jouer au poker."
    },
    # 11: ID 121
    {
        "file": "MMAP03.json",
        "id": 121,
        "fr_cleaned": "Jamais intéressé par les arcades,\nmais Mu a un casino maintenant.[1205][000F] L'idée\nde jouer m'excite..."
    },
    # 12: ID 123
    {
        "file": "MMAP03.json",
        "id": 123,
        "fr_cleaned": "Jamais intéressé par les arcades,\nmais Mu a un casino maintenant.[1205][000F] L'idée\nde jouer m'excite..."
    },
    # 13: ID 125
    {
        "file": "MMAP03.json",
        "id": 125,
        "fr_cleaned": "J'adore les antiquités. Je fréquentais Time Castle.[1205][000F]\nAu fait, savez-vous ce qu'est une arme légendaire ?"
    },
    # 14: ID 130
    {
        "file": "MMAP03.json",
        "id": 130,
        "fr_cleaned": "Pas étonnant qu'il n'y ait pas d'arme légendaire.\nElle n'a pas encore été livrée."
    },
    # 15: ID 131
    {
        "file": "MMAP03.json",
        "id": 131,
        "fr_cleaned": "Le vendeur attend à l'usine abandonnée,\nmais le propriétaire a peur des monstres. Quel lâche !"
    },
    # 16: ID 133
    {
        "file": "MMAP03.json",
        "id": 133,
        "fr_cleaned": "Trop tard. Une femme malchanceuse a acheté\nl'arme légendaire avant que je puisse la voir."
    },
    # 17: ID 134
    {
        "file": "MMAP03.json",
        "id": 134,
        "fr_cleaned": "Un autre amateur d'antiquités.\nSi j'avais décidé plus tôt, j'aurais été premier. Quel dommage."
    },
    # 18: ID 135
    {
        "file": "MMAP03.json",
        "id": 135,
        "fr_cleaned": "Quelle malchance. Le propriétaire a donné\nl'arme légendaire."
    },
    # 19: ID 136
    {
        "file": "MMAP03.json",
        "id": 136,
        "fr_cleaned": "À une fille aux cheveux courts, dit-on.\nIndice trop vague. *soupir* Si seulement je l'avais achetée !"
    },
    # 20: ID 137
    {
        "file": "MMAP03.json",
        "id": 137,
        "fr_cleaned": "Tu as entendu ? Le fantôme d'une femme\n apparaît dans le parc d'Aoba.[1205][000F]"
    },
    # 21: ID 138
    {
        "file": "MMAP03.json",
        "id": 138,
        "fr_cleaned": "Tu crois que c'est vrai ?[1205][000F]\nJe devrais changer mon itinéraire."
    },
    # 22: ID 139
    {
        "file": "MMAP03.json",
        "id": 139,
        "fr_cleaned": "Qu'allons-nous faire... ?\nMême les pompiers ont été bombardés..."
    },
    # 23: ID 140
    {
        "file": "MMAP03.json",
        "id": 140,
        "fr_cleaned": "Personne pour éteindre les flammes\n en cas de nouvelle attaque !"
    },
    # 24: ID 141
    {
        "file": "MMAP03.json",
        "id": 141,
        "fr_cleaned": "Tu sais ce qu'est le Dernier Bataillon ?[1205][000F]\nOn dit qu'ils sont les terroristes responsables,\nmais je n'en ai jamais entendu parler."
    },
    # 25: ID 144
    {
        "file": "MMAP03.json",
        "id": 144,
        "fr_cleaned": "Dommage qu'ils ne soient pas plus précis\naux infos."
    },
    # 26: ID 145
    {
        "file": "MMAP03.json",
        "id": 145,
        "fr_cleaned": "Ils ne font que semer plus de confusion\n sur les terroristes !"
    },
    # 27: ID 147
    {
        "file": "MMAP03.json",
        "id": 147,
        "fr_cleaned": "Ouf... Dans le ciel, mes options de marche sont limitées.[1205][000F]\nHein ? Ce n'est pas le moment ?"
    },
    # 28: ID 148
    {
        "file": "MMAP03.json",
        "id": 148,
        "fr_cleaned": "Inutile de paniquer. Ça a déjà trop empiré.[1205][000F]\nJe m'en fiche qu'on évolue ou qu'on meure."
    },
    # 29: ID 149
    {
        "file": "MMAP03.json",
        "id": 149,
        "fr_cleaned": "Tu as entendu ?[1205][000F]\nDes rumeurs sur la fin des gens d'en bas."
    },
    # 30: ID 150
    {
        "file": "MMAP03.json",
        "id": 150,
        "fr_cleaned": "La dernière : la Grande Croix provoquera\n une tempête magnétique brûlant la Terre."
    },
    # 31: ID 155
    {
        "file": "MMAP03.json",
        "id": 155,
        "fr_cleaned": "Hé, le fantôme de l'idole à Aoba était réel ?[1205][000F]\nJ'ai entendu des gens en parler !"
    },
    # 32: ID 161
    {
        "file": "MMAP03.json",
        "id": 161,
        "fr_cleaned": "C'est quoi un Sauteur Vieux ?[1205][000F]\nIl y en aurait un au mont Katatsumuri."
    },
    # 33: ID 166
    {
        "file": "MMAP03.json",
        "id": 166,
        "fr_cleaned": "La Sorcière du Buffet, c'est la vieille femme\nqui vit dans un buffet, c'est ça ?"
    },
    # 34: ID 174
    {
        "file": "MMAP03.json",
        "id": 174,
        "fr_cleaned": "Effrayant d'acheter des armes en pleine rue à Yumezaki.\nBon choix, reprises basses."
    },
    # 35: ID 176
    {
        "file": "MMAP03.json",
        "id": 176,
        "fr_cleaned": "Effrayant d'acheter des armes en rue à Yumezaki.\nQualité médiocre, prix bas."
    },
    # 36: ID 178
    {
        "file": "MMAP03.json",
        "id": 178,
        "fr_cleaned": "Effrayant d'acheter des armes en rue à Yumezaki.\nQualité et prix moyens."
    },
    # 37: ID 180
    {
        "file": "MMAP03.json",
        "id": 180,
        "fr_cleaned": "Effrayant d'acheter des armes en rue à Yumezaki.\nChères, mais très haute qualité."
    },
    # 38: ID 182
    {
        "file": "MMAP03.json",
        "id": 182,
        "fr_cleaned": "Clair de Lune, le restau français ?"
    },
    # 39: ID 185
    {
        "file": "MMAP03.json",
        "id": 185,
        "fr_cleaned": "Clair de Lune, le restau français ?"
    },
    # 40: ID 188
    {
        "file": "MMAP03.json",
        "id": 188,
        "fr_cleaned": "Clair de Lune, le restau français ?"
    },
    # 41: ID 191
    {
        "file": "MMAP03.json",
        "id": 191,
        "fr_cleaned": "Clair de Lune, le restau français ?"
    },
    # 42: ID 194
    {
        "file": "MMAP03.json",
        "id": 194,
        "fr_cleaned": "Clair de Lune, le restau français ?"
    },
    # 43: ID 202
    {
        "file": "MMAP03.json",
        "id": 202,
        "fr_cleaned": "Le Rosa Candida de Rengedai vend des armures.\nQualité et prix moyens."
    },
    # 44: ID 204
    {
        "file": "MMAP03.json",
        "id": 204,
        "fr_cleaned": "Rosa Candida vend des armures.\nQualité basse, prix bas."
    },
    # 45: ID 206
    {
        "file": "MMAP03.json",
        "id": 206,
        "fr_cleaned": "Rosa Candida vend des armures.\nCher, mais qualité incroyable."
    },
    # 46: ID 226
    {
        "file": "MMAP03.json",
        "id": 226,
        "fr_cleaned": "Je fais faire un costume chez London Clothier.[1205][000F]\nMais ils vendent aussi des armures ?"
    },
    # 47: ID 228
    {
        "file": "MMAP03.json",
        "id": 228,
        "fr_cleaned": "Je fais faire un costume chez London Clothier.[1205][000F]\nMais ils vendent aussi des armures ?"
    },
    # 48: ID 230
    {
        "file": "MMAP03.json",
        "id": 230,
        "fr_cleaned": "Je fais faire un costume chez London Clothier.[1205][000F]\nMais ils vendent aussi des armures ?"
    },
    # 49: ID 232
    {
        "file": "MMAP03.json",
        "id": 232,
        "fr_cleaned": "Je fais faire un costume chez London Clothier.[1205][000F]\nMais ils vendent aussi des armures ?"
    }
]

assert len(cleaned_items) == len(suspicious)
for c, s in zip(cleaned_items, suspicious):
    assert c['id'] == s['id']
    assert c['file'] == s['file']

with open('cleaned_all_6.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_items, f, indent=2, ensure_ascii=False)

print("Saved cleaned_all_6.json successfully!")
