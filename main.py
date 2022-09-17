import openai

from secret import api_OpenAI

openai.api_key = api_OpenAI

print('\n\n -------------------------- Programa que gera perguntas para entrevistar alguém --------------------------\n')
pessoa = input('Para quem você fará as perguntas?\nR: ')
qtde_perguntas = input('Quantas perguntas?\nR: ')


response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Cria uma lista de " +qtde_perguntas + "perguntas complexas para a minha entrevista com um " + pessoa +" em Português",
  temperature=0.5,
  max_tokens=500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response['choices'][0]['text'])
