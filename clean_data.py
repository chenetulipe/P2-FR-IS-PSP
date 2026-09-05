import json

def fix_lines(text):
    # If text has more than 2 lines, we chunk by 2 lines and insert [1205][000A]
    lines = text.split('\n')
    out = []
    for i in range(0, len(lines), 2):
        chunk = '\n'.join(lines[i:i+2])
        out.append(chunk)
    return '[1205][000A]'.join(out)

fixes = [
    # script_351.json, 48
    ("M-Mon Dieu! Ils volaient! [1205][000F]Des soldats\nvolaient dans le ciel! Je l'ai vu\nde mes propres yeux! De longues\nlances et des armures noires...", ""),
    # script_352.json, 18
    ("J'ai toujours voulu être [1205][000F]riche.\nJe parle ainsi et porte des habits\ncoûteux, mais en vrai je suis dans\nle rouge. Je bosse pour payer.", ""),
    # script_356.json, 16
    ("Mais quand même...[1205][000F] Est-ce la\nmeilleure façon...? Qu'on me remette\nmon but sur un plateau comme ça...\nÇa me rendra vraimentheureuse...?", ""),
    # script_359.json, 97
    ("Tiens, de retour.", " Choisissez une option.\nDemander des rumeurs Parler à Baofu Annuler\nChoisissez un sujet. Rumeurs armureries\nRumeurs armures Autres Rien\nChoisissez une région. Rengedai Yumezaki\nAoba Kounan Aucune Choisissez une région.\nRengedai Yumezaki Aoba Kounan Aucune\nChoisissez un sujet. Concours magazines\nRumeurs Mu Armes légendaires Aucun\nVérifié. Soumettre. Patientez après envoi."),
    # script_359.json, 120
    ("Hé, j'ai entendu que c'est un\ngroupe, le Cercle masqué, qui fait\nça. 05]ça. C'est vrai? J'aime pas\nça... Sumaru devait être paisible...", ""),
    # script_360.json, 35
    ("Te revoilà.", " Choisis une option. Demander\ndes rumeurs Parler avec Baofu Annuler\nChoisis un sujet. Rumeurs armureries\nRumeurs armures Autres Rien\nChoisis une région. Rengedai Yumezaki\nAoba Kounan Aucune Choisis une région.\nRengedai Yumezaki Aoba Kounan Aucune Choisis\nun sujet. Rumeurs concours Rumeurs Mu\nRumeurs armes légendaires Aucune Vérifié.\nSoumettre les infos. Après envoi, patientez."),
    # script_361.json, 27
    ("La fin est proche. Ce garçon... je l'ai déjà\nvu quelque part?", " Panneau SS: Accueil général,\nBureau étrangers RDC: Objets trouvés,\nPermis, Conseillers 2e: Aide victimes,\nAide sinistrés Panneau 3e: Interrogatoire,\nAffaires internes 4e: Labo, Crimes juvéniles\n5e: Personnesdisparues, Enquêtes spéciales"),
    # script_361.json, 37
    ("Katsuya est très populaire auprès des femmes\ndu commissariat...[1205][000F] Mais pas de petite\namie. Il est du genre marié à son boulot?", "\nAvis Si vous voyez cet homme, appelez le\n17! Je crois l'avoir vu quelque part..."),
    # script_362.json, 36
    ("Ce crétin s'est échappé, et maintenant\nces soldats... Pourquoi j'ai si peu de\nchance?", " Une nouvelle chaîne. [1205][000F]La seule\nchose propre ici. Jouer un CD? OuiNon"),
    # script_364.json, 0
    ("Le choc était trop fort pour Jun?\n[1205][000F]Son image de Maya a été réduite\nen miettes. L'écart entre l'image\net la réalité était trop grand...", ""),
    # script_364.json, 5
    ("Mais tu sais... un plus jeune me\ntente aussi. Si j'en trouve un mignon,\nje le[1205][000F] garde tant que je peux...", " Un\nradiocassette neuf. La seule chose\npropre de la pièce. Lire un CD? OuiNon"),
    # script_365.json, 10
    ("Quand le Musée de l'Aéronautique\nfut construit, les gens ont\ndit que ça jurait dans Sumaru.\nDésormais y'a foule de visiteurs.", ""),
    # script_365.json, 17
    ("Le courage de Maya face au danger\nm'impressionne toujours. Elle\na jamais piloté de dirigeable\navant! Je pense pas en toutcas...", ""),
    # script_366.json, 10
    ("Le moment venu j'ignorerai encore\ntant de choses, mais je veux croire\nque je ferais le [1205][000F]bon choix. Je\nne veux plus porter de masque...", ""),
    # script_367.json, 70
    ("Vous achetez des armures contre\nles terroristes? Il paraît que ce\nCercle Masqué n'accorde pas plus de\nvaleur à un homme qu'àune pierre...", ""),
    # script_368.json, 15
    ("Je n'étais pas le plus doué, mais\nj'avais ma place dans l'art. [1205][000F]Les\nbiens matériels ne m'intéressent\nplus. Ce n'est plus mon monde...", ""),
    # script_369.json, 46
    ("Le monde va s'éteindre? Vraiment?\nOn va évoluer en Idéaliens?\nSérieusement? Et celui que j'attends\nn'est toujours pas là!?Vraiment!?", ""),
    # script_370.json, 9
    ("Je n'y suis pas tout à fait arrivée,[1205][000F]\nmais j'ai fini par me trouver moi-même...\nême... C'est dur à expliquer, maisje\nsens que j'ai trouvé le vrai moi.", ""),
    # script_373.json, 37
    ("Je ne pensais pas qu'Eikichi\nréagirait autant au poisson. On\ndirait un réflexe conditionné...\nOu plutôt une empreinteanimale?", ""),
    # script_373.json, 58
    ("Toro m'a recommandé des chaussures\npour maigrir juste en les portant.\n[1205][000F]Mais puis-je lui faire confiance\npour ce genre de choses...", ""),
    # script_373.json, 104
    ("Le festival du Lycée Kasu a l'air\ngénial cette année. Leur président\ndu BDE est vraiment pas comme\nles autres, pas vrai Eikichi!?", ""),
    # script_373.json, 159
    ("Ce type là-bas a eu un coup de\nchance soudain. Il se plaignait\ntoujours qu'il resterait un esclave\nsalarié avec des dettes sans fin.", ""),
    # script_373.json, 167
    ("Mwaha! Je suis enfin devenu président.\nManger des sushis le midi pendant\nque mes sous-fifres bossent prouve\nque j'ai grimpé les échelons!", ""),
    # script_373.json, 179
    ("In Lak'ech... Haha, formidable!\nCe monde morne va tomber et on\nentamera une nouvelle voie en\ntranshumains: l'idéal de l'homme! Haha!", ""),
    # script_375.json, 33
    ("Je crois qu'on peut lui dire\nqu'il est en sécurité. La dernière\ncible sera le Musée aérospatial,\nautant qu'il s'inquiète pas trop.", ""),
    # script_375.json, 48
    ("Ceux perdus dans le labyrinthe\nde la vie [1205][000F]dérivent jusqu'ici.\nNous éclairons leur chemin vers\nl'avenir. Je suis la Génie de Sumaru.", ""),
    # script_375.json, 49
    ("Votre première visite, on dirait.\n[1205][000F]Êtes-vous quelqu'un qui a perdu sa\nvoie vers le futur? Ou venez-vous\nentendreles récits de ce monde éphémère?", ""),
    # script_375.json, 91
    ("Pour les prochains temps, votre\noptimisme fera naître de nouvelles\nperspectives, permettant à toutes\nles négociations de se dérouler bien.", ""),
    # script_375.json, 114
    ("On dit que [E4][NULL][NULL][0006]Tony's Shop[E4][NULL][NULL][0002] à Yumezaki\nvend de [E4][NULL][NULL][0006]vraies armes[E4][NULL][NULL][0002]. [1205][000F]Leur qualité\nLL][NULL][0006]qualité est exquise, mais les prix\nsont élevés[E4][NULL][NULL][0002]. Que c'est dangereux...", ""),
    # script_375.json, 115
    ("Ah. Eikichi de Kasugayama a quitté\nson poste de Boss...[1205] Ne connaissant\nguère la vie étudiante, j'ignore\nla valeur de cettehistoire.", ""),
    # script_375.json, 118
    ("Il semble que [E4][NULL][NULL][0006]Jolly Roger[E4][NULL][NULL][0002] vende\nde [E4][NULL][NULL][0006]vraies[1205][000F] armes[E4][NULL][NULL][0002]. Je suis surprise\nqu'un si proche voisin vende des\n[E4][NULL][NULL][0006]armements de qualité, au prix fort[E4][NULL][NULL][0002].", ""),
    # script_375.json, 140
    ("Quand je suis revenu(e) [1205][000F]à moi,\nj'étais ici... Cette [1432][NULL][NULL][0014]boule de cristal[1432][NULL][NULL][0014]\nn'est que du verre. J'inventais...\nSauf que ça se réalise quandmême!", ""),
    # script_375.json, 141
    ("Croyez-moi, j'en étais le plus\nsurpris(e). [1205][000F]Mais plus ça se produisait,\nplus j'étais convaincu(e)... Mes\nprédictions se réalisenttoujours.", ""),
    # script_375.json, 146
    ("Hm. Je vous ai dit toutes les\nhistoires que je connais pour\nl'instant. Partageons à nouveau quand\nj'en aurai de nouvelles à raconter.", ""),
    # script_375.json, 178
    ("En parlant de ça... La Génie ici...\nOn ne voit pas son visage mais cette\nvoix... Je l'ai entendue quelque\npart Impossible de savoiroù...", ""),
    # script_375.json, 193
    ("Mon vrai boulot c'est capitaine de\nbateau. Je roule avec mon chapeau\nde [1205][000F]yacht. Je gagne bien la nuit,\nalorsje dors dans mon taxi à l'usine.", ""),
    # script_375.json, 194
    ("Y'a un type qui copie mon style,\nmais j'le vois plus trop depuis un\nmoment, alors j'suis venu le chercher.[1205][000F]\nT'aurais pas entendu parler de lui ?", ""),
    # script_376.json, 10
    ("Le crâne de cristal de feu...\nC'est la deuxième fois qu'on la eu\nC'est ]C'est celui que mon ombre a\nemporté... Je m'en sens toujours mal.", ""),
    # script_376.json, 16
    ("Le plus proche tu es aux pôles,\nplus l'impact sera faible... Mais\nles tsunamis et tremblements de\nterre n'épargnerontpersonne...", ""),
    # script_376.json, 58
    ("Bientôt, la fortune t'accompgnera et\ntu vivras dans le bohnneur.", " [E4][NULL][NULL]\"Génie\nSumaru, colporteuse de rumeurs Oui...\nJe vois... Ton destin se cristalise...\nHmm... C'est... La Tempérance..."),
    # script_376.json, 121
    ("Tu sais ce que ça veut dire? En tant que\n[1205][000F]politicien, je serai l'homme le plus puissant\ndu monde! Mwahahaha!", " Message de debug. Vous\nne devriez pas me voir. Reset du BIT voyance."),
    # script_376.json, 122
    ("Je bosse à Sumaru TV, et un collègue\nest un vrai trouillard. à la 205]la\nvieille usine abandonnée je lui\nai raconté une histoire flippante.", ""),
    # script_376.json, 124
    ("Et comme je le pensais, ce qu'il a\nimaginé l'a terrorisé. Il est devenu\nblanc comme un linge ![1205][000F] Hihi...\nAhaha ! Ça me fait encore rire !", ""),
    # script_377.json, 24
    ("Mes tarifs dépendent de la valeur du\nmarché pour les soins, mais je soigne\ntout le monde, donc tu pourras économiser\nunpeu au final.", " Erreur Aucun BIT de saut.\nContactez Kanada, ou plutôt votre chef QA."),
    # script_377.json, 34
    ("D'accord! Douleur, douleur, va-t'... Hé! T'as\npas assez d'argent! Reviens quand tes poches\nseront pleines!", " Erreur Aucun BIT de saut.\nContactez Kanada, ou plutôt votre chef QA."),
    # script_378.json, 3
    ("Une vraie dame japonaise est\nmodeste, discrète, respecte la piété\nfiliale et les[1205][001E] règles du foyer.\n[001E]Viens, ta leçon de thécommence.", ""),
    # script_378.json, 5
    ("Une vraie dame japonaise est\nmodeste, discrète, respecte la piété\nfiliale et les[1205][001E] règles du foyer.\n[001E]Viens, ta leçon de thécommence.", ""),
    # script_378.json, 24
    ("Le tirage au sort? Ah oui, bien sûr. Ceci\na été livré ici. Tenez, prenez-le.", " Lettre\n[NULL][NULL]Merci d'avoir participé à notre tirage.\nMalheureusement, vous n'êtes pas gagnantcette\nfois. Tentez à nouveau votre chance![NULL][NULL]"),
    # script_378.json, 25
    ("Le tirage au sort? Ah oui, bien sûr.\nCeci a été livré ici. Tenez, prenez-le.", "\nLettre [NULL][NULL]Merci d'avoir participé à\nnotre tirage. Félicitations! Vous\navez été sélectionnégagnant! [NULL][NULL]Veuillez\naccepter ceci [E4][NULL][NULL][NULL][E4][NULL][NULL] en guise de prix.\nTentez à nouveau votre chance![NULL][NULL] Vous\nn'avez plus de place pour un autre [E4][NULL][NULL][NULL][E4][NULL][NULL]..."),
    # script_379.json, 27
    ("[1432][NULL][NULL][0014]Porter[1432][NULL][NULL][0014] un Persona signifie,\npour un utilisateur comme vous,\nl'accepter en soi. Posséder sa\ncarte seule ne vous servira àrien.", "")
]

with open('suspicious_4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out_data = []
for i, item in enumerate(data):
    if i < len(fixes):
        cleaned, garbage = fixes[i]
        final_clean = fix_lines(cleaned)
        out_data.append({
            "file": item["file"],
            "id": item["id"],
            "fr_cleaned": final_clean,
            "garbage_removed": garbage.strip() if garbage else ""
        })

with open('cleaned_4.json', 'w', encoding='utf-8') as f:
    json.dump(out_data, f, indent=2, ensure_ascii=False)
