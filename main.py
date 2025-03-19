from stats import word_count, sorted_char_counts
import sys

def main(book):
    if len(book) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        book = book[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book)} total words")
        print("--------- Character Count -------")
        sorted_char_count = sorted_char_counts(book)
        for key in sorted_char_count:
            if key == "\n":
                print("\\n: " + str(sorted_char_count[key]))
            else:
                print(str(key) + ": " + str(sorted_char_count[key]))
        print("============= END ===============")
    return

print(sys.argv)
main(sys.argv)
