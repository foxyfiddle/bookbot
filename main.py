def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    character_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for character in string.lower():
        for key in character_counts:
            if character == key:
                character_counts[key] += 1
    return character_counts

def convert_to_list(to_convert):
    new_list = [{"character": key, "num": value} for key, value in to_convert.items()]

    return new_list

def sort_by(dict):
    return dict['num']

def display_report(character_count, word_count):
    character_list = convert_to_list(character_count)
    character_list.sort(reverse=True, key=sort_by)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for i in range(0, len(character_list)):
        print(f"The '{character_list[i]['character']}' character was found {character_list[i]['num']} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    
    display_report(character_count, word_count)

main()