def count_words(text):
    message = text.split()
    number_words = len(message)
    print(number_words)
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

    





