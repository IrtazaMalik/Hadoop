# Reducer function
import sys

def reducer():
    current_doc_id = None
    current_tf_idf = {}

    # For each line from standard input
    for line in sys.stdin:
        # Split the line into word ID, TF/IDF value, and document ID
        word_id, tf_idf, doc_id = line.strip().split('\t')

        # If new document ID, save the previous document's TF/IDF representation
        if doc_id != current_doc_id:
            if current_doc_id is not None:
                # Output document ID along with TF/IDF representation
                print(current_doc_id, current_tf_idf, sep='\t')
            current_doc_id = doc_id
            current_tf_idf = {}

        # Save TF/IDF value for the current document
        current_tf_idf[word_id] = float(tf_idf)

    # Output the last document's TF/IDF representation
    if current_doc_id is not None:
        print(current_doc_id, current_tf_idf, sep='\t')

if __name__ == "__main__":
    reducer()
