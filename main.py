from stats import get_num_words
from stats import char_counts
from stats import sort_counts
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Word count section
    print("----------- Word Count ----------")
    num_words = get_num_words(path)
    print(f"Found {num_words} total words")
    
    # Character count section
    print("--------- Character Count -------")
    text = get_book_text(path)
    chars_dict = char_counts(text)
    sorted_chars = sort_counts(chars_dict)
    
    for char_info in sorted_chars:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print_report(sys.argv[1])