import subprocess
import platform

# SO answer for clearing console in terminal
# only tested with bash
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python


def clear_console():
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()  # I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine
    else:  # Linux and Mac
        print("\033c", end="")


def is_one_single_character(character):
    return character.isalpha() and len(character) == 1


def only_characters_in_input(player_input):
    return player_input.isalpha()


def ask_player_for_secret_word():
    print("Please input secret passphrase:", end="")
    secret_passphrase = input().lower()
    if only_characters_in_input(secret_passphrase):
        return secret_passphrase
    else:
        print("Input must consist only of letters.")
        return ask_player_for_secret_word()


def ask_player_for_guess():
    print("Please guess: ", end='')
    character = input().lower()
    if is_one_single_character(character):
        return character
    else:
        print("Input must be a single character. Please retry.")
        return ask_player_for_guess()


def has_player_won(already_guessed, secret):
    ret = True
    for character in secret:
        if character in already_guessed and ret:
            ret = True
        else:
            ret = False
    return ret


def hangman_game():
    secret = ask_player_for_secret_word()
    letters_already_guessed = []
    clear_console()

    while not has_player_won(letters_already_guessed, secret):
        player_guess = ask_player_for_guess()
        letters_already_guessed.append(player_guess)

        for letter in secret:
            if letter in letters_already_guessed:
                print(letter, end="")
            else:
                print("*", end="")
        print("\n")

    print("Game finished.")

    if has_player_won(letters_already_guessed, secret):
        print("Congratulations player has won.")
    else:
        print("Player lost.")  # player can't lose atm as difficulty isn't implemented yet.

    print("Press Y and enter for retry: ", end="")
    retry = input().lower()
    if retry == "y":
        clear_console()
        hangman_game()


def main():
    hangman_game()


if __name__ == "__main__":
    main()
