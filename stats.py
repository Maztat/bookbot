def get_book_text(book:str):
    with open(book) as f:
        return f.read()
    return NotADirectoryError

def word_count(book:str):
    word_num = len(get_book_text(book).split())
    return word_num

def char_counts(book:str):
    char_count = dict()
    book = get_book_text(book)
    for letter in book:
        letter = letter.lower()
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

def sorted_char_counts(book:str):
    char_count = char_counts(book)
    sorted_char_count = dict()
    while len(sorted_char_count) < len(char_count):
        biggest = str(list(char_count.keys())[0])
        for key in char_count:
            if not key in sorted_char_count:
                if char_count[key] > char_count[biggest]:
                    biggest = key
        sorted_char_count[biggest] = char_count.pop(biggest)
    return sorted_char_count