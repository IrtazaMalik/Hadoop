# Mapper function
import sys
import csv

def mapper():
    # Read each line from standard input
    for line in sys.stdin:
        # Split the line into words
        words = line.strip().split()
        # Emit each word along with a count of 1
        for word in words:
            print(word.lower(), 1, sep='\t')

if __name__ == "__main__":
    mapper()
