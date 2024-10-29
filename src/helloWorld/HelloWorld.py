from greetings import greet  
from validate import *

print("Welcome user, please let me know your name to continue")

def main():
<<<<<<< HEAD
    user_name = input("Introduce your name: ")
    greet(user_name)
=======
    while True:
        user_name = input("¿What is your name? ")       
        if len(user_name) < 3:
            print("The username has to have more than 3 characters")
            continue
        if not user_name[0].isupper():
            print("You cannot enter your name with the first letter in lowercase!")
            continue
        if validate(user_name):
            greet(user_name)
            break
        else:
            print("Invalid characters in your username")
>>>>>>> a7b060e369261ac8377b239c709b2811471a116d

if __name__ == "__main__":
    main()
