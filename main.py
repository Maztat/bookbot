def main():
    print(get_book_text("frankenstein.txt"))
    return

def get_book_text(book):
    path = "books/" + book
    with open(path) as f:
        return f.read()
    return

main()