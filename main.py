def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counting_characters = count_characters(text)
    print (count_characters(text))

def count_characters(text):
    my_string = text
    lowered_string = my_string.lower()
    number_characters = {}
    for characters in lowered_string:
        if characters in number_characters :
            number_characters[characters] += 1
        else:
            number_characters[characters] = 1
    return number_characters
        


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

    





