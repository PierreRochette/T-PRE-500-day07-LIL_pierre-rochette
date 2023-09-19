word = "HELLO"
blank = list(word)
for i in range(len(blank)) :
    blank[i] = "_"
print(blank)


while "_" in blank : 
    guess = str(input("Entrez une lettre : "))
    if len(guess) > 1 : 
        print("Veuillez n'entrer qu'une seule lettre à la fois")

    found = False

    for j in range(len(word)) :
        if word[j] == guess and blank[j] == "_" :
            blank[j] = guess
            found = True
            print(blank)

    if not found :
        print("Lettre incorrecte veuillez réessayer.")

print("Vous avez trouvé le mot : ", "".join(blank))
