import random

player_count = 0
words_list = ["WAREHOUSE", "SHARINGAN", "LILLE", "PARIS", "ROUBAIX"]
word_to_guess = words_list[random.randint(0, len(words_list) - 1)]

print(words_list)
print(word_to_guess)

def guessing_word (word_to_guess) :

    displayed_blank = "_ " * len(word_to_guess)
    print(displayed_blank)

    user_guess = str(input("Proposez une lettre : "))

    if user_guess in word_to_guess :
        for i in range(len(word_to_guess)) :
            if word_to_guess[i] == user_guess :
                displayed_blank[i] = user_guess

    return None

guessing_word(word_to_guess)



















