#!/bin/python3


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    unique_characters = count_num_letters(text)
    character_count = count_characters(text)
    print(f"{num_words} words found in the document")
    print(f"{unique_characters} unique characters found in the document")
    print(f"Character count: {character_count}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"No file found at {path}.")
    except Exception as e:
        print(f"An error has occured: {e}")

# count the number of unique characters in the text
def count_num_letters(text):
    unique_characters = set(text)
    return len(unique_characters)

# count the number of times each character appears in the text
def count_characters(text):
    character_count = {}
    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

if __name__ == '__main__':
    main()