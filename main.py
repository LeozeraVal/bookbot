def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"-- BEGIN REPORT OF BOOK {book_path} --")
    print(f"{word_count} words found in the document.")
    alpha_characters = count_alpha_characters(book_text)
    for character in alpha_characters:
        char = character["character"]
        num = character["num"]
        print(f"The character '{char}' appeared {num} times.")
    print("-- END REPORT --")

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return(f.read())

def sort_on(dict):
    return dict["num"]

def count_characters(text):
    count = {}
    standard = text.lower()
    for character in standard:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    count_list = [{"character": k, "num": v} for k, v in count.items()]
    count_list.sort(reverse=True, key=sort_on)
    return count_list

def count_alpha_characters(text):
    count_list = count_characters(text)
    filtered_count_list = [x for x in count_list if x["character"].isalpha()]
    return filtered_count_list
main()