# projekt_2.py: druhý projekt do Engeto Online Python Akademie
# author: Patrícia Kotrík Iliašová
# email: iliasovap@gmail.com
# discord: discord: iliasovap_54684


import random

divider = "----------------------------------------"

print("Hi there!")
print(divider)


def generate_number() -> int:
    """This function generates a random 4-digit number that consists of unique digits and does not start with 0."""
    numbers = []
    for number in range(1000, 9999):
        digits = []
        for digit in str(number):
            if digit in digits:
                continue
            else:
                digits.append(digit)
        if len(digits) == 4:
            numbers.append(number)
        else:
            continue
    return random.choice(numbers)


def user_input(answer: int) -> str:
    """
    This function handles user input and verifies that the number provided by the user is numeric, does not start with 0 and consists of 4 digits.
    If the number does not comply with these requirements, this function is called again.
    """
    input_digits = []
    number_of_digits = 0

    if answer.isdigit():
        if len(answer) == 4:
            if int(answer) >= 1000:
                for digit in answer:
                    number_of_digits += 1
                    if digit in input_digits:
                        continue
                    else:
                        input_digits.append(digit)
                if number_of_digits == 4:
                    if len(input_digits) == 4:
                        return int(answer)
                    else:
                        print(
                            "Oops, you need to enter a number with unique digits.",
                            divider,
                            sep="\n",
                        )
                        return user_input(input("Enter a number: "))
                else:
                    print(
                        "Oops, you need to enter a number that has 4 digits.",
                        divider,
                        sep="\n",
                    )
                    return user_input(input("Enter a number: "))
            else:
                print("Oops, number cannot start with zero.", divider, sep="\n")
                return user_input(input("Enter a number: "))
        else:
            print(
                "Oops, you need to enter a number consisting of 4 digits. Try again.",
                divider,
                sep="\n",
            )
            return user_input(input("Enter a number: "))
    else:
        print("Oops, you can enter numeric values only.", divider, sep="\n")
        return user_input(input("Enter a number: "))


def user_input_eval(generated_number: int, user_number: int) -> str:
    """
    This function evaluates user input and calls the function bulls_cows_stats to print the number of bulls and cows, then calls the use_input function again.
    If the user guesses the number correctly, this function returns the number of attempts and ends the program.
    """
    wrong_answer = True
    number_of_attempts = 1

    while wrong_answer:

        if generated_number == user_number:

            if number_of_attempts == 1:
                wrong_answer = False
                return print(
                    f"Correct, you've guessed the right number in {number_of_attempts} guess!",
                    divider,
                    "That's amazing!",
                    sep="\n",
                )
            elif number_of_attempts > 1 and number_of_attempts < 8:
                wrong_answer = False
                return print(
                    f"Correct, you've guessed the right number in {number_of_attempts} guesses!",
                    divider,
                    "That's average.",
                    sep="\n",
                )
            else:
                wrong_answer = False
                return print(
                    f"Correct, you've guessed the right number in {number_of_attempts} guesses!",
                    divider,
                    "That's not so good.",
                    sep="\n",
                )
        else:
            number_of_attempts += 1
            bulls_cows_stats(generated_number, user_number)
            user_number = user_input(input("Enter a number: "))


def bulls_cows_stats(generated_number: int, user_number: int) -> str:
    """This function takes the generated number and user number, compares the number provided by the user against the generated number and prints the number of bulls and cows."""
    cows = 0
    bulls = 0

    generated_list = [digit for digit in str(generated_number)]

    user_list = [digit for digit in str(user_number)]

    for digit in user_list:
        if digit in generated_list:
            cows += 1
        else:
            continue

    for i in range(len(generated_list)):
        if generated_list[i] == user_list[i]:
            bulls += 1
        else:
            continue

    cows = cows - bulls

    if cows == 1 and bulls == 1:
        return print(f"{bulls} bull, {cows} cow", divider, sep="\n")
    elif cows == 1:
        return print(f"{bulls} bulls, {cows} cow", divider, sep="\n")
    elif bulls == 1:
        return print(f"{bulls} bull, {cows} cows", divider, sep="\n")
    else:
        return print(f"{bulls} bulls, {cows} cows", divider, sep="\n")


def main():
    generated_number = generate_number()
    print(
        "I've generated a random 4 digit number for you.",
        "Let's play a bulls and cows game.",
        divider,
        sep="\n",
    )

    user_number = user_input(input("Enter a number: "))
    user_input_eval(generated_number, user_number)


main()
