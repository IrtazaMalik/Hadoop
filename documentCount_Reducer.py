# Reducer function
import sys

def reducer():
    word_doc_count = {}

    # For each line from standard input
    for line in sys.stdin:
        # Split the line into word and document ID
        word, doc_id = line.strip().split('\t')

        # Count the number of documents in which each word appears
        if word not in word_doc_count:
            word_doc_count[word] = set()
        word_doc_count[word].add(doc_id)

    # Output each word along with its document frequency
    for word, doc_set in word_doc_count.items():
        doc_count = len(doc_set)
        print(word, doc_count, sep='\t')

if __name__ == "__main__":
    reducer()
