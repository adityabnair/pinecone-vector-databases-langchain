# Vector Databases for LangChain

This is a functional project that aims to demonstrate what a vector database is and its usage to read and query a Medium article stored in a .txt file. The project splits the data from the txt file containing thousands of tokens into chunks. Then LangChain's embeddings are used to convert relevant information into approximately 19 vectors (can be understood as arrays) of numbers matching the textual content. Finally, using chaining a query is made to the declared LLM in order to fetch the correct answer contained within the .txt file which is then displayed as the output. 
Pinecone's serverless vectorstore was used in this project and the vector similarity used was eucilidean in the database. 

## Screenshots

![image](https://github.com/adityabnair/vector-databases-langchain/assets/64246274/5af37069-54c2-4033-b3af-abf4d174e514)
![image](https://github.com/adityabnair/vector-databases-langchain/assets/64246274/3059b036-d291-43e3-92ab-1b86497abf6c)
![image](https://github.com/adityabnair/vector-databases-langchain/assets/64246274/1ef4b431-cfaa-4b04-805e-313d5e3ac99a)


## Main Prerequisites

1. At least Python 3.10
2. Access to OpenAI's API credits for usage of gpt-3.5
3. Access to Pinecone's API and index creation 

### Running

1. Use pipenv to install python libraries from requirements.txt
2. Add environment variable in a .env file to hold Pinecone's and OpenAI's API keys
3. Run main.py
4. Observe results and can re-reun using a different query pertaining to article


## Acknowledgments

Thanks to @emarco177 for the langchain development course
