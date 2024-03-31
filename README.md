# Basic Search Engine Using MapReduce
###By: i211376-Irtaza_i211761-Nabeeha_i211721-Huraida


## Report on Implementing a Basic Search Engine Using MapReduce 
Introduction:
The objective of this project was to develop a basic search engine using the MapReduce paradigm. The project involved several steps including document indexing and query processing. This report outlines the procedures followed and the implementation details for each step.

1. Data Preprocessing:

The project began with obtaining a portion of the English Wikipedia dump provided by Wikimedia. The dataset included around 5 million Wikipedia articles.
The dataset consisted of several columns including ARTICLE_ID, TITLE, SECTION_TITLE, and SECTION_TEXT. For this project, we focused solely on the ARTICLE_ID and SECTION_TEXT columns.
Initial data preprocessing involved cleaning the text to remove any noise or irrelevant information. This ensured that the indexing and query processing steps produced accurate results.
2. Organizing the Project:

Before starting the implementation, the team organized and discussed the specifics of the project. Responsibilities were assigned, and modules were designated to team members.
A public GitHub repository was created to facilitate collaborative development. Incremental commits were made to track progress, ensuring version control benefits were utilized effectively.
3. Word Enumeration:

The first step in the MapReduce implementation was Word Enumeration. This involved generating a set of unique words from the corpus and assigning a unique ID to each word using a hash function.
A Mapper function was implemented to read each document and emit each word along with a count of 1. A Reducer function aggregated the counts for each word and outputted the word along with the total count.
4. Document Count:

Next, a MapReduce job was implemented to calculate the Inverse Document Frequency (IDF) for each term. This involved counting the number of documents in which each term appeared.
Similar to Word Enumeration, a Mapper function read each document and emitted each word along with the document ID. A Reducer function counted the number of documents in which each word appeared and saved the IDF values to a file in HDFS.
5. Indexer:

The Indexer task computed the TF/IDF representation for each document. TF/IDF values were computed using the word-ID mappings and IDF values obtained from the previous steps.
A Mapper function read each document and emitted the word along with the TF/IDF value and document ID. A Reducer function grouped the TF/IDF values by document ID and saved the TF/IDF representation for each document.
6. Query Processing:

Finally, a method to generate the vectorized representation of a query was implemented. A MapReduce job was then written to calculate the relevance function between the query and each document.
The TF/IDF representations generated in the Indexer step were used to rank the documents based on relevance, and the top results were retrieved.
Conclusion:
In conclusion, the project successfully implemented a basic search engine using the MapReduce paradigm. By following the outlined steps and leveraging the capabilities of Apache Hadoop's MapReduce framework, we were able to handle large volumes of text data efficiently and provide relevant search results. The project demonstrated the power of distributed storage and processing in handling big data for information retrieval tasks.
