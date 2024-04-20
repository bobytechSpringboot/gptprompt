import openai

context = "section from my long doc"
how_to_respond = f"use this context to response to question: {context}. \
    please stick to this context when answering the question. "
background = "You are an assistant."
question = input("entery a sample question: ")

required_parameters = {
  'model': "gpt-4",
  'messages' : [ #how GPT interact with us
     {"role": "system", "content": background} #optional, default: generic assistant
     {"role": "user", "content": background}
     {"role": "assistant", "content": how_to_respond} # this role also store previous assistant responses. 
    ]
}

response = openai.ChatCompletion.create (
  model = required_parameters['model'],
  messages = required_parameters['messages'],
  max_tokens=200, # num of tokens to return
  n=1, #how many responses to generate
)

answer = response.choices[0]['message']['content'].replace('.', '.\n\t')
print(answer)
