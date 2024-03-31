# Mapper function
import sys

def mapper(word_id_idf_file):
    # Load word-ID IDF mapping from file
    word_id_idf = {}
    with open(word_id_idf_file, 'r') as f:
        for line in f:
            word_id, idf = line.strip().split('\t')
            word_id_idf[word_id] = float(idf)

    # Read each line from standard input
    for line in sys.stdin:
        # Split the line into document ID and words
        doc_id, document = line.strip().split(',', 1)
        # Split the document into words
        words = document.split()
        # Calculate TF for each word and emit TF/IDF along with doc ID
        tf = {}
        total_words = len(words)
        for word in words:
            word_id = hashlib.sha256(word.encode()).hexdigest()  # Calculate word ID
            if word_id in word_id_idf:
                if word_id not in tf:
                    tf[word_id] = 1 / total_words
                else:
                    tf[word_id] += 1 / total_words
        for word_id, tf_value in tf.items():
            print(word_id, tf_value * word_id_idf[word_id], doc_id, sep='\t')

if __name__ == "__main__":
    word_id_idf_file = sys.argv[1]
    mapper(word_id_idf_file)
