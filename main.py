#!/bin/python3


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

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

if __name__ == '__main__':
    main()