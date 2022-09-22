import openai
import pyttsx3
from secret import api_OpenAI

openai.api_key = api_OpenAI
marquinhos = pyttsx3.init()

print('\n\n -------------------------- Programa que gera o que você pedir --------------------------\n\nPara sair é só digitar: --sair\n')
def bem_vindo():
    marquinhos_fala("Bem vindo!")

def teste_saida(entrada):
  if entrada.lower() == '--sair':
    exit(0)

def pergunta_ai(entrada):
  try:
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=entrada + '. Responda em Português',
      temperature=0.5,
      max_tokens=500,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    print('\nIA: ' + response['choices'][0]['text'].strip() + '\n')
    return response['choices'][0]['text'].strip()
  except Exception:
    print('Não deu certo')
def marquinhos_fala(entrada):
    marquinhos.say(entrada)
    marquinhos.runAndWait()

def verifica_se_quer_voz(x: str = "não"):
    x = input("\033[0;31mGostaria de utilizar o comando de voz? (sim/não)\nR:\033[m ")
    teste_saida(x)
    if x.lower() == "nao" or x.lower() == "não":
        return False
    elif x.lower() == "sim":
        return True
    return verifica_se_quer_voz()

if __name__ == "__main__":
    bem_vindo()
    tem_voz = verifica_se_quer_voz()
    print("----------------Conversa Iniciada-------------------\n\n")
    while True:
        entrada: str = input("Humano: ")
        teste_saida(entrada)
        resposta = pergunta_ai(entrada)
        if tem_voz:
            marquinhos_fala(resposta)
