def count_words(string):
    words = string.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    
    #print(len(word_count))
    #print(file_contents)

main()