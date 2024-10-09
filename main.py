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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    
    print(character_count)
    #print(len(word_count))
    #print(file_contents)

main()