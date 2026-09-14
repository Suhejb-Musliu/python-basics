
while True:

    score = 0

    print("==============================")
    print("       MINI QUIZ GAME")
    print("==============================")

    name = input("What is your name? ")

    print("\nGood luck", name, "!\n")

    print("1. What is the capital of Kosovo?")
    print("A. Prizren")
    print("B. Prishtina")
    print("C. Peja")

    answer = input("Your answer: ")

    if answer.upper() == "B":
        print("Correct! +10 points")
        score += 10
    else:
        print("Wrong!")

    print("\n2. How many days are in a week?")
    print("A. 5")
    print("B. 7")
    print("C. 10")

    answer = input("Your answer: ")

    if answer.upper() == "B":
        print("Correct! +10 points")
        score += 10
    else:
        print("Wrong!")

    print("\n3. Which one is a programming language?")
    print("A. Python")
    print("B. Pizza")
    print("C. Football")

    answer = input("Your answer: ")

    if answer.upper() == "A":
        print("Correct! +10 points")
        score += 10
    else:
        print("Wrong!")

    print("\n4. How many months are in one year?")
    print("A. 10")
    print("B. 11")
    print("C. 12")

    answer = input("Your answer: ")

    if answer.upper() == "C":
        print("Correct! +10 points")
        score += 10
    else:
        print("Wrong!")

    print("\n==============================")
    print("           RESULT")
    print("==============================")

    print("Player:", name)
    print("Score:", score, "/ 40")

    if score == 40:
        print("Perfect score!")
    elif score >= 20:
        print("Good job!")
    else:
        print("Keep practicing!")

    print("\nDo you want to play again?")
    again = input("Type Y for Yes or N for No: ")

    if again.upper() == "N":
        print("Thanks for playing!")
        break

    print("\nStarting a new game...\n")
