# Reducer function
import sys

def reducer():
    current_word = None
    word_count = 0

    # For each line from standard input
    for line in sys.stdin:
        # Split the line into word and count
        word, count = line.strip().split('\t')

        # Convert count to integer
        count = int(count)

        # If the word is same as the previous word, increment count
        if current_word == word:
            word_count += count
        else:
            # If the word is different, output the previous word and its count
            if current_word:
                print(current_word, word_count, sep='\t')
            current_word = word
            word_count = count

    # Output the last word and its count
    if current_word:
        print(current_word, word_count, sep='\t')

if __name__ == "__main__":
    reducer()
