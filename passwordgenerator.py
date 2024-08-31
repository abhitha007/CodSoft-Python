import string
import random

def generate_password(length):
    
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits_chars = string.digits
    special_chars = string.punctuation

    all_chars = lowercase_chars + uppercase_chars + digits_chars + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
