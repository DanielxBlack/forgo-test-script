#! /opt/homebrew/bin/python3

language_picked = ["en", "es", "jp", "ru"]
language_to_index = {lang: idx for idx, lang in enumerate(language_picked)}
chosen_lang = input(
    "What language do you want to create a list for (en, es, jp, ru)?  "
)
chosen = language_to_index[chosen_lang]  # This gives you the index


with open("wordlist.txt", "r") as inputFile:
    for line in inputFile:
        theLines = line.strip()
        print(f"https://forvo.com/word/{theLines}/#{language_picked[chosen]}")
