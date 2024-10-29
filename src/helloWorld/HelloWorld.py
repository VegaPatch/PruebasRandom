from greetings import greet

print("Welcome user, please let me know your name to continue")

def main():
    user_name = input("Introduce your name: ")
    greet(user_name)

if __name__ == "__main__":
    main()