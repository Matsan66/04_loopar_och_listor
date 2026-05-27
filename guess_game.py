import random

def guess_number():
    print("\nJag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

    random_number = random.randint(1, 100)
    print(random_number)
    guessed_number = None
    number_of_guesses = 0

    while guessed_number != random_number:
        guessed_number = input("\nGissa: ")

        try:
            guessed_number = int(guessed_number)
        except ValueError:
            print("\nDu måste gissa ett heltal.")
            print("Försök igen.")
            continue

        if guessed_number <= 0:
            print("Du måste gissa ett tal större än 0.")
            print("Försök igen.")
            continue

        number_of_guesses += 1

        if guessed_number != random_number:

            for i in range(-5, 6):
                if guessed_number == random_number - i:
                    print("Nu börjar det brännas!")
            if guessed_number < random_number:
                print("Nej, det är för lågt")
            elif guessed_number > random_number:
                print("Nej, det är för högt")

    print(f"\nDet är rätt!! Du gjorde det på {number_of_guesses} gissningar.")


def main():
    print("\n---------------------------")
    print("Välkommen till gissa talet!")
    print("---------------------------")

    guess_number()

    play_again = input("Vill du spela igen (ja/ nej): ")

    while play_again not in ["ja", "nej"]:
        print("Du måste svara ja eller nej!")
        play_again = input("Vill du spela igen? (ja/ nej): ")

    if play_again == "ja":
        guess_number()

if __name__ == "__main__":
    main()