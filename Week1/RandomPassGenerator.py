import random
import string

def generate_password(length, uppercase=False, lowercase=False, digits=False, special_chars=False):
    characters = []

    #checking if we say yes to uppercase
    if uppercase:
        characters.extend(string.ascii_uppercase)
        #adding upper case letters

    #checking if we say yes to uppercase    
    if lowercase:
        characters.extend(string.ascii_lowercase)
        #adding lower case letters

    #checking if we say yes to uppercase
    if digits:
        characters.extend(string.digits)
        #adding digits 

    #checking if we say yes to uppercase
    if special_chars:
        characters.extend(string.punctuation)
        #adding Special case 

    #checking we did't select yes to any then by default it will give letters in alphabet
    if not any([uppercase, lowercase, digits, special_chars]):
        # If no character types are selected, default to lowercase and uppercase letters
        characters = list(string.ascii_letters)

    #by using random.choice() method of random module we will get random character in out password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def menu():

    #menu
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    #checking we did't select yes to any then it will ask to select any or terminate the code
    if not any([uppercase, lowercase, digits, special_chars]):
        print("At least one character type must be specified.")
        return

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    menu()
