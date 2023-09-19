##### CES ELEMENTS ONT ÉTÉ GÉNÉRÉS PAR CHATGPT. IL S'AGIT DE COMPRENDRE
# LA LOGIQUE À IMPLÉMENTER DANS MON CODE. 

mot_secret = "LILLE"
mot_affiche = ["_"] * len(mot_secret)

def afficher_mot():
    print("Mot à deviner :", " ".join(mot_affiche))

def deviner_lettre():
    lettre = input("Entrez une lettre : ").upper()

    if lettre in mot_secret:
        for i in range(len(mot_secret)):
            if mot_secret[i] == lettre:
                mot_affiche[i] = lettre
        return True
    else:
        print("Mauvaise proposition.")
        return False

while "_" in mot_affiche:
    afficher_mot()
    deviner_lettre()

while deviner_lettre() == "exit" :
    break

print("Félicitations, vous avez deviné le mot :", "".join(mot_affiche))
