import string


def clean_text_file(filename="text.txt"):
    """
    Cleans a text file by lowercasing, removing punctuation,
    and correcting extra whitespace.
    """
    try:
        with open(filename) as file:
            content = file.read().lower()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    # Getting rid of the punctuations
    for charachter in string.punctuation:
        content = content.replace(charachter, "")

    # removing spaces/tabs/newlines from the very start and end.
    content = content.strip()

    # breaking the string into a list of words.
    list_of_words = content.split()

    # Putting the words back together
    content = " ".join(list_of_words)

    cleaned_filename = f"cleaned_{filename}"

    with open(cleaned_filename, "w") as file:
        file.write(content)

    print(f"\n✅ Successfully cleaned text and saved to '{cleaned_filename}'")


clean_text_file()
