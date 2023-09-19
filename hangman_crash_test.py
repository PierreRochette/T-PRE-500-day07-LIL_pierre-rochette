word = "HELLO"

# attribution d'une valeur à la variable mot. Ici 'Hello'

blank = list(word)

# initialisation de blank, la variable permettant d'afficher les underscores

for i in range(len(blank)) :
    blank[i] = "_"
print(blank)

# remplacement de chaque élément de la liste blank par un underscore

# boucle permettant de réitérer tant qu'il y a des underscore dans la liste blank

while "_" in blank : 
    guess = str(input("Entrez une lettre : "))

    # Tant qu'il y a un underscore dans blank, l'utilisateur est invité à entrer
    # une lettre. 

    if len(guess) > 1 : 
        print("Veuillez n'entrer qu'une seule lettre à la fois")

    # Si l'utilisateur entre plus d'un caractère, affiche un message d'erreur et
    # renvoit à l'input. 

    found = False

    # initialisation de la variable found, permettant de déterminer si l'utilisateur
    # a fait le bon choix ou non. 

    for j in range(len(word)) :

    # La boucle for parcourt chaque lettre du mot "word"

        if word[j] == guess and blank[j] == "_" :
        
        # Si une lettre du mot d'indice 'j' correspond à la lettre entrée par
        # l'utilisateur, ET SI l'lément de la liste blank de même indice 'j'
        # est un underscore : 

            blank[j] = guess

            # ALORS l'élement de la liste blank d'indice 'j' est remplacé par
            # le choix de l'utilisateur 

            found = True

            # la variable found prendra la valeur True 



            # la liste avec les éléments modifiés est affichée. 

    if not found :

        # Si la variable found n'a pas reçu la valeur true dans l'itération
        # précédente, alors on affiche un message 'lettre incorrecte' à l'utilisateur
        # et on revient au début de la boucle. 

        print("Lettre incorrecte veuillez réessayer.")

    print(blank)


# Dès lors qu'il n'y a plus de "_" dans blank, alors on print un message de
# félicitations. 
# La méthode "".join(blank) permet de renvoyer la liste blank sous forme de 
# string. 

print("Vous avez trouvé le mot : ", "".join(blank))
