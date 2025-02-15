from collections import defaultdict



def read_text(path: str) -> str:

    with open(path) as f:
        file_contents = f.read()
    
    return file_contents



def count_words(file_contents: str) -> int:
    return len(file_contents.split())



def count_characters(file_contents: str) -> defaultdict[str]:
    
    lowercase_contents = file_contents.lower()
    char_count = defaultdict(int)

    for chr in lowercase_contents:
        if (chr.isalpha()):
            char_count[chr] += 1
    
    return char_count



if __name__ == "__main__":

    path = "books/frankenstein.txt"
    
    file_contents = read_text(path)

    char_count = count_characters(file_contents)

    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_contents)} words were found in the document\n")

    for key in char_count.keys():
        print(f"The '{key}' character was found {char_count[key]} times")

    print("--- End report ---")

