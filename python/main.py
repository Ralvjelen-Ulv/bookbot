from pathlib import Path



def get_book_text(book_filepath):
    
    with open(book_filepath) as f:
        book_content = f.read()
        return book_content 
    
def main():

    frankenstein = Path(__file__).parent.parent/"books"/"frankenstein.txt"   
    print(get_book_text(frankenstein))

main()
