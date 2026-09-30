# Programming Exercise 9-4

def main():
    try:
        input_name = input('Enter the name of the input file: ')

        with open(input_name, 'r') as input_file:
            text = input_file.read()
            words = text.split()

            # Remove punctuation from the beginning/end of words.
            clean_words = []
            for word in words:
                word = word.strip('.,!?;:"()')
                clean_words.append(word)

            # Create set of unique words.
            unique_words = set(clean_words)

            print('These are the unique words in the text:')
            for word in sorted(unique_words):
                print(word)

    except FileNotFoundError:
        print('Error: The file was not found.')


if __name__ == '__main__':
    main()
