defined_word = "HELLO"
displayed_blank = list(defined_word)
print(displayed_blank)

for i in range(len(displayed_blank)):
    displayed_blank[i] = "_"

print(displayed_blank)

user_guess = str(input("Proposez une lettre : "))

if user_guess in defined_word :
    for j in range(len(defined_word)) :
        if defined_word[j] == user_guess :
            displayed_blank[j] = user_guess

print(displayed_blank)

while "_" in displayed_blank :

    user_guess = str(input("Proposez une lettre : "))

    if user_guess in defined_word :
        for j in range(len(defined_word)) :
            if defined_word[j] == user_guess :
                displayed_blank[j] = user_guess