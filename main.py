#!/bin/python3

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    unique_characters = count_num_letters(text)
    character_count = count_characters(text)
    report = generate_report(num_words, character_count)
    print(report)

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
    unique_characters = set(text.lower())
    return len(unique_characters)

# count the number of each character in the text ignoring case and special characters and spaces
def count_characters(text):
    character_count = {}
    for character in text.lower():
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

# create a report that aggrfegate all the word and character data into a nice report and print it to the console
def generate_report(num_words, character_count):
    report = f"{num_words} words found in the document\n"
    report += "Character count: \n"
    for character, count in character_count.items():
        report += f"The '{character}' character appears {count} times\n"
    return report

if __name__ == '__main__':
    main()