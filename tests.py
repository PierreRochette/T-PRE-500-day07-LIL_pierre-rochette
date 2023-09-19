##### CES ELEMENTS ONT ÉTÉ GÉNÉRÉS PAR CHATGPT. IL S'AGIT DE COMPRENDRE
# LA LOGIQUE À IMPLÉMENTER DANS MON CODE. 

"""

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


print("Félicitations, vous avez deviné le mot :", "".join(mot_affiche))


"""

# PETITS TESTS DE STRINGS
"""
defined_word = "TEST"
print(defined_word)
print(defined_word[1])

word_to_create = "_ " * len(defined_word)
print(word_to_create)

guess = str(input("Entrez une lettre : "))

if guess in defined_word :
    for i in range(len(defined_word)) :
        if defined_word[i] == guess :
            word_to_create.replace("_ ", guess)

print(word_to_create)

"""

defined_word = "TEST"
print(defined_word)
print(defined_word[1])

word_to_create = "_ " * len(defined_word)
print(word_to_create)

guess = str(input("Entrez une lettre : "))

if guess in defined_word:
    for i in range(len(defined_word)):
        if defined_word[i] == guess:
            word_to_create = word_to_create[0:i] + guess + word_to_create[i+1:]

print(word_to_create)
