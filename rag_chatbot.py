############part 1, create knowledge base#######
#
# step 1 get  documents
#
import requests
url = 'http:/xxxx/text_demo"
resp = requests.get(f"{url}/mydoc.txt"}
mytext = resp.text if resp.status_code == 200 else ""

import os
if.os.path.exists("mydoc.txt"):
    with.open("mydoc.txt", "r", encoding=utf8") as file:
       mytext = ""
       for line in file.readLines():
           mytext += line

#
# step 2 splitting and embedding
#
from langchain.text_splitter import CharacterTextSplitter

test_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size-700,
    chunk_overlag=120, #hope relevant info fall in one split
    length_function=len
)
chunks = text_splitter.split-text(mytext)
print(len(chunks)

from langchain.embeddings import OpenAIEmbeddings
   # langchain has many embedding models. some of them do not require API keys.
   # google "langchain text embedding modles"
embeddings_model = OpenAIEmbeddings()
embeddings = embeddings_model.embed_documents(chunks)
print(len(embeddings)) #30 for example
print(len(embeddings[0]) #1536  vector dimensions
      
#
# step 3 store embeddings
#
# Use Vector Store DB, optimized to store vector and chunks. 
# Vector store DB also do vectgor space search 
# google "Langchain vector stores"
# ex: pinecone, mongodb, chroma, elasticsearch...

from langchain.vectorstores import Chroma
db = Chroma.from_texts(chunks, OpenAIEmbeddings())

####### part 2, query knowledge base #######
#
# step 1 create question embedding
#
import numpy as np

myquestion = "xxxxx"
question_embedding = np.array(embedding_model.embed_query(myquestion))

#
# step 2 Search for similar embeddings
#
distances=[]
for embedding in embeddings:
    distances.append(np.linalg.norm(embedding - quesiton_embedding))
k = 3
sorted_indices = np.argsort(distances)
top_three = sorted_indices[:k]
similar_chunks = [chunks[index] for index in top_three]

PURPLE = '\033[95m'
BOLD = '\033[1m'
RESET = '\033[0m' #reset text color to default
for doc in  similar_chunks:
    text = doc[:200]
    text = text.replace("eggs", BOLD + PURPLE + 'eggs' + RESET)
    print(text)

#
# step 2 generate response from GPT 
#
import openai
context = "\n\n".join([doc for doc in similar_chunks])
parameters = {
    'model': 'gpt-4'
    'messages': [
        {"role": "system", "content": "you are an assistant. When answer this question \
                                      use the first person (ex. we"}
        {"role": "user", "content": "myquestion"}
        {"role": "assistant", "content": f"only use informatoin from {context}, \
                                          do not use any other knowledge you might have"}
    ]
}
response = openai.ChatCompletion.create(
    model=parameters['model'],
    messages=parameters['messages'].
    max_tokens=1000,
    n=1 #only give one answer
)
answer = response.choices[0]['message']['content'].replace(".", ".\n\t")
print("question: ", myquestion)
print("answer:: ", answer)

#inspect what we sent to openai
import re
print(re.sub(" +", " ", parameters['messages'][2]['content']))






      





