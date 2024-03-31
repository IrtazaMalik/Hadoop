# Mapper function for relevance calculation
def mapper(query_vector):
    for line in sys.stdin:
        doc_id, tf_idf_representation = line.strip().split('\t')
        tf_idf_representation = eval(tf_idf_representation)  # Convert string representation to dictionary
        relevance = sum(tf_idf_representation.get(word_id, 0) * query_vector.get(word_id, 0) for word_id in query_vector)
        print(doc_id, relevance, sep='\t')
