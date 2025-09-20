import sys
from stats import count_words, count_characters



def read_text(path: str) -> str:

    with open(path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    return file_contents



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    file_contents = read_text(path)
    char_count = count_characters(file_contents)

    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words\n")

    print("--------- Character Count -------")
    for key in char_count.keys():
        print(f"{key}: {char_count[key]}")

    print("============= END ===============")

