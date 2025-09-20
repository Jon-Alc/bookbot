from collections import defaultdict



def count_words(file_contents: str) -> int:
    return len(file_contents.split())



def count_characters(file_contents: str) -> defaultdict[str]:
    
    lowercase_contents = file_contents.lower()
    char_count = defaultdict(int)

    for chr in lowercase_contents:
        if (chr.isalpha()):
            char_count[chr] += 1
    
    return char_count