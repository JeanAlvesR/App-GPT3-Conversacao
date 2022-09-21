import openai

from secret import api_OpenAI
openai.api_key = api_OpenAI
print('\n\n -------------------------- Programa que gera o que você pedir --------------------------\n\nPara sair é só digitar: --sair\n')

def teste_saida(entrada):
  if entrada.lower() == '--sair':
    exit(0)

def pergunta_ai(entrada):
  try:
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=entrada + '. responda em Português',
      temperature=0.5,
      max_tokens=500,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    print('\nIA: ' + response['choices'][0]['text'].strip() + '\n')
  except Exception:
    print('Não deu certo')


while True:
  entrada: str = input('Humano: ')
  teste_saida(entrada)
  pergunta_ai(entrada)

