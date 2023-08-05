import random
import art
import words


print(art.logo)

chosen_word = random.choice(words.word_list)
chosen_word_length = len(chosen_word)
display_word = []
lives = 6
current_string = ""
for i in range(chosen_word_length):
    display_word += "_"

while current_string != chosen_word and lives > 0:
    guessed_right = False
    guess_letter = input("Guess a letter ").lower()
    print("------------------------------------------------------------")
    for i in range(chosen_word_length):
        if chosen_word[i] == guess_letter:
            display_word[i] = guess_letter
            guessed_right = True
    if not guessed_right:
        print("Chosen letter is not in the word! Keep trying")
        lives -= 1
    print(art.stages[lives])
    print(display_word)
    current_string = "".join(display_word)

if lives > 0:
    print(f"You win! The chosen word is {chosen_word}")
else:
    print("You lose!")
