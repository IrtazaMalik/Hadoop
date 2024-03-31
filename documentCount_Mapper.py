# Mapper function
import sys

def mapper():
    # Read each line from standard input
    for line in sys.stdin:
        # Split the line into document ID and words
        doc_id, document = line.strip().split(',', 1)
        # Split the document into words
        words = document.split()
        # Emit each word along with the document ID
        for word in words:
            print(word.lower(), doc_id, sep='\t')

if __name__ == "__main__":
    mapper()
