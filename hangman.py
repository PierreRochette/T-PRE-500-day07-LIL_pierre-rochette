import random

words_list = ['HELLO', 'GOODBYE', 'WORLD', 'MARS', 'EARTH', 'PLEASE']
word = words_list[random.randint(0, len(words_list) - 1)]
blank_word = list(word)
print(blank_word)
player_count = len(blank_word)
for i in range(len(blank_word)) :
    blank_word[i] = "_"

# Tout fait l'effet attendu jusqu'ici. 

while player_count < 0 : 

    while "_" in blank_word :

        user_guess = str(input("Entrez une lettre : "))
        if len(user_guess) > 1 :
            print("Veuillez n'entrer qu'une seule lettre à la fois. ")



















