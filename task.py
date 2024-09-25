import time

def task_1():
    password = "Password123"
    guess = input("Guess the password: ")
    while guess != password:
        print("Password incorrect, try again!")
        guess = input("Guess the password: ")
    print("Password cracked!")


def task_2():
    times_table = int(input("Enter the times table number: "))
    terms = int(input("Enter the number of terms to calculate: "))
    count = 1
    while count <= terms:
        print(times_table * count)
        count += 1

def task_3():
    count = 1
    while count <= 5:
        print(f"{count} Mississippi")
        time.sleep(1)
        count += 1
