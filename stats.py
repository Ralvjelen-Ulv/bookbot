def get_num_words(book_text):
    
    num_words = len(book_text.split())

    return num_words

def get_char_number(book_text) :
    
    letters_dict = {}

    for letters in range(len(book_text)) :
        letter = (book_text[letters]).lower()
        if letter != ' ' :        
            if letter not in letters_dict :
                letters_dict[letter] = 0
            letters_dict[letter] += 1
    
    return letters_dict

def sort_on(items) :
    return items["num"]

def sort_char_dict(letters_dict) :
    
    characters = []
    for chars in letters_dict :
        letter_dict = {"char": chars, "num": letters_dict[chars]}
        characters.append(letter_dict)
        characters.sort(reverse=True, key=sort_on)
    return characters
