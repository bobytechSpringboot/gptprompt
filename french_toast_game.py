from langchain.embeddings import OpenAIEmbeddings

embedding_module = OpenAIEmbeddings(openai_api_key = mykey)
# register an account with openai and get the key

def french_toast_game(word1, word2):
   if secretword == word1 or secretword == word2:
       return "It is " + secretword + "."
   distance1 = distance(text_embedding(secretword), test_embedding(word1)
   distance2 = distance(text_embedding(secretword), test_embedding(word2)
   return "it is more like " + word1 if distance < distance2 else word2

def query_embedding(question_str):
   return np.array(embedding_module.embed_query(question_str))

def document_embedding(doc_str):
   return np.array( embedding_module.embed_documents([doc_str])[0] )

def distance(vec1, vec2):
    return np.linalg.norm(vec1 - vec2)
