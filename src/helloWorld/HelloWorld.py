from greetings import greet  
from farewell import goodbye
from validate import *

print("Welcome user, please let me know your name to continue")

def main():
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
            goodbye(user_name)
            break
        else:
            print("Invalid characters in your username")

if __name__ == "__main__":
    main()
