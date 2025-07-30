import sys
from pathlib import Path
import stats
from stats import get_num_words
from stats import get_char_number
from stats import sort_char_dict


def get_book_text(book_filepath):

    with open(book_filepath) as f:
        book_content = f.read()
        return book_content 

#def enumerate_words(book_text):
#    return len(book_text.split())
    

def main():
    #frankenstein = Path(__file__).parent/"books"/"frankenstein.txt"   
    #book_text = get_book_text(frankenstein)
    
    book = sys.argv[1]
    
    
    
    book_text = get_book_text(book)
    number_of_words = get_num_words(book_text)
    chars_dict = get_char_number(book_text)
    chars_list = sort_char_dict(chars_dict)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print(f"--------- Character Count -------")
    for dicts in chars_list :
        
        char = dicts["char"]
        num = dicts["num"]
        if char.isalpha() :
            print(f"{char}: {num}")
    print(f"============= END ===============")

    
    
    
#    print(f"{number_of_words} words found in the document")
#    print(chars_list)
    
if len(sys.argv) < 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else : main()
