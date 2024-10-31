def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    print("--- Begin report of book/frankenstein.txt ---")
    print(f"{num_words} worlds found in the document")
    print ()
    alpha_chars = [chars for chars in chars_dict if chars.isalpha()]
    for chars in alpha_chars:
        numm = chars_dict[chars]
            
        print (f"The {chars} character was found {numm} times")

    print("--- End report ---")





def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
        


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

    





