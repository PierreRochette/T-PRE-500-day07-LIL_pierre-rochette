import random

player_count = 0
words_list = ["WAREHOUSE", "SHARINGAN", "LILLE", "PARIS", "ROUBAIX"]

def select_random_word(words_list) :
    return words_list[random.randint(0, (len(words_list) - 1))]

word_to_guess = select_random_word(words_list)
print(word_to_guess)

blank = "_" * len(word_to_guess)
print(blank)

user_proposition = str(input("Proposez une lettre :"))

if user_proposition in word_to_guess :
    blank.replace("_", user_proposition)
else :
    print("Non.")

print(blank)