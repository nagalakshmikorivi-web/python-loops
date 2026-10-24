# Python Loops Practice Project
# This project contains 10 Python loop programs.

def print_numbers():
    n = int(input("Enter N: "))
    for i in range(1, n + 1):
        print(i)


def sum_numbers():
    n = int(input("Enter N: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum:", total)


def multiplication_table():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def count_vowels():
    text = input("Enter a word or sentence: ").lower()
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    print("Number of vowels:", count)


def factorial():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Enter a non-negative integer.")
        return

    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Factorial:", result)


def sum_digits():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Enter a non-negative integer.")
        return

    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    print("Sum of digits:", total)


def guess_number():
    secret = 7
    attempts = 0

    while True:
        guess = int(input("Guess the number (1-10): "))
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct!")
            print("Attempts:", attempts)
            break


def reverse_number():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Enter a non-negative integer.")
        return

    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    print("Reversed number:", rev)


def collatz_sequence():
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Enter a positive integer.")
        return

    steps = 0
    print("Sequence:", end=" ")

    while n != 1:
        print(n, end=" ")

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        steps += 1

    print(1)
    print("Steps:", steps)


def star_triangle():
    rows = int(input("Enter the number of rows: "))
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()


while True:
    print("\n===== PYTHON LOOPS PRACTICE =====")
    print("1. Print numbers from 1 to N")
    print("2. Sum of first N numbers")
    print("3. Multiplication table")
    print("4. Count vowels")
    print("5. Factorial")
    print("6. Sum of digits")
    print("7. Guess the number")
    print("8. Reverse a number")
    print("9. Collatz sequence")
    print("10. Star triangle")
    print("0. Exit")

    choice = input("Choose a program (0-10): ")

    if choice == "1":
        print_numbers()
    elif choice == "2":
        sum_numbers()
    elif choice == "3":
        multiplication_table()
    elif choice == "4":
        count_vowels()
    elif choice == "5":
        factorial()
    elif choice == "6":
        sum_digits()
    elif choice == "7":
        guess_number()
    elif choice == "8":
        reverse_number()
    elif choice == "9":
        collatz_sequence()
    elif choice == "10":
        star_triangle()
    elif choice == "0":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice. Please select 0-10.")
