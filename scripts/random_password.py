# random_password.py

"""
Python Script - Generate a secure random password
Command-line Password Generator (CLI)

Generates a password with letters, digits, and special characters.
Includes at least one character from each category for security.
Shuffles characters for unpredictability. Users can specify length,
default is 12.
"""

import random
import string

def generate_password(length: int = 12) -> str:
    """
    Generate a secure random password including letters, digits, and symbols.
    Ensures at least one character from each category is included.
    Shuffles characters for unpredictability.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure password has at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length
    if length > 4:
        all_chars = lowercase + uppercase + digits + special
        # Add remaining random characters (beyond the first 4 mandatory ones) from all character types
        password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable sequences
    random.shuffle(password)
    return ''.join(password)


def run_password_generator():
    """
    CLI interaction for the password generator.
    Keeps asking the user until they choose to quit.
    Handles user input, default length, and error management.
    """
    while True:
        try:
            user_input = input("Enter desired password length (default 12) or 'q' to quit:\n>>> ").strip()
            if user_input.lower() == "q":
                print("Exiting. Bye!")
                break

            length = int(user_input) if user_input else 12
            print(f"Generated password: {generate_password(length)}\n")

            # Ask if the user wants another password
            again = input("Generate another password? (y/N): ").strip().lower()
            if again != 'y':
                print("Done. Bye!")
                break

        except ValueError as e:
            # Handles both int() conversion errors and ValueError from generate_password (length < 4)
            print("Error:", e)
            print("Invalid input. Please enter a number (4 or higher), or type 'q' to quit.\n")


if __name__ == "__main__":
    run_password_generator()
