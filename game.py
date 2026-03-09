import random
from mots import mots
import string


def get_valid_word(words): 
    word = random.choice(words) 
    return word.upper()

def game():
    word = get_valid_word(mots)
    word_letters = set(word)
    word_length = len(word)
    alphabet = set(string.ascii_uppercase) 
    guessed_letters = set() 
    lives = 6

    print("Votre mot comporte", word_length, "caractères.")

    while len(word_letters) > 0 and lives > 0: 
        print("Vous avez déjà utilisé ces lettres :", " ".join(guessed_letters), "et il vous reste", lives, "vies")

        word_list = [letter if letter in guessed_letters else '-' for letter in word]

        print("Mot actuel: ", " ".join(word_list))
        print("")
        
        guessed_letter = input("Devinez une lettre : ").upper()
        print("")

        if guessed_letter in alphabet - guessed_letters:
            guessed_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)

            else:
                lives = lives - 1 
                print("Cette lettre n'est pas dans le mot")

        elif guessed_letter in guessed_letters:
            print("Vous avez déjà deviné cette lettre. Veuillez réessayer.")

        else:
            print("Caractère invalide. Veuillez réessayer.") 


    if lives == 0:
        print("Vous avez perdu. Le mot était", word)
    else:    
        print("Félicitations! Vous avez deviné le mot", word)



if __name__ == "__main__":
    game()

