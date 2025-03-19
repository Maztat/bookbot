def get_book_text(book):
    path = "books/" + book
    with open(path) as f:
        return f.read()
    return

def wordcount(book:str):
    word_num = len(get_book_text(book).split())
    return word_num
