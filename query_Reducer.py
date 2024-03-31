# Reducer function for relevance calculation
def reducer():
    top_results = []
    for line in sys.stdin:
        doc_id, relevance = line.strip().split('\t')
        top_results.append((doc_id, float(relevance)))

    # Sort the documents based on relevance
    top_results.sort(key=lambda x: x[1], reverse=True)

    # Output the top results
    for doc_id, relevance in top_results:
        print(doc_id, relevance, sep='\t')
