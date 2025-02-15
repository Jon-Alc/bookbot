from collections import defaultdict

def read_text() -> str:

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return file_contents



def count_words(file_contents: str):
    print(len(file_contents.split()))



def count_characters(file_contents: str):
    
    lowercase_contents = file_contents.lower()
    char_count = defaultdict(int)

    for chr in lowercase_contents:
        char_count[chr] += 1
    
    print(char_count)



if __name__ == "__main__":
    file_contents = read_text()
    print(type(file_contents))
    count_words(file_contents)
    count_characters(file_contents)