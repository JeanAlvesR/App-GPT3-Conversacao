import openai

from secret import api_OpenAI
openai.api_key = api_OpenAI
print('\n\n -------------------------- Programa que gera o que você pedir --------------------------\n')

while True:

  entrada = input('O que você quer??\nR: ')

  try:
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt = entrada + 'em Português',
      temperature=0.5,
      max_tokens=500,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    print(response['choices'][0]['text']+'\n\n-----------Nova Pergunta ----------\n\n')
  except Exception:
    print('Não deu certo')
