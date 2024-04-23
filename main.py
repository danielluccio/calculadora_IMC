# Importando os módulos necessários
import os  # Para interagir com o sistema operacional
from colorama import Fore  # Para adicionar cores ao texto no terminal
from PIL import Image  # Para lidar com imagens
import time  # Para pausar a execução do programa por alguns segundos

# Limpa a tela do terminal
os.system("cls")

# Definindo as cores para uso posterior
colors = {'red': Fore.RED,
          'reset': Fore.RESET,
          'magenta': Fore.MAGENTA}

# Definindo a função para calcular o IMC
def imc():
    # Solicita ao usuário que insira seu peso em KG
    peso = float(input("Digite seu peso em KG: "))
    # Solicita ao usuário que insira sua altura
    altura = float(input("Digite sua altura: "))
    
    # Limpa a tela do terminal
    os.system("cls")
    # Exibe o peso inserido pelo usuário
    print(f"Esse é o seu peso {peso} KG")
    # Exibe a altura inserida pelo usuário
    print(f"Essa é a sua altura: {altura}")

    # Calcula o IMC
    imc = (peso / (altura * altura))
    # Exibe o IMC calculado com duas casas decimais, com a cor vermelha
    print(f"O seu IMC é: {colors['red']}{imc:.2f}{colors['reset']}")

    # Classifica o IMC com base nos valores padrão
    if imc < 18.5:
        print(f"CLASSIFICAÇÃO: MAGREZA")
    elif imc <= 24.9:
        print(f"CLASSIFICAÇÃO: NORMAL")
    elif imc <= 29.9:
        print("CLASSIFICAÇÃO: SOBREPESO")
    elif imc <= 39.9:
        print("CLASSIFICAÇÃO: OBESIDADE")
    else:
        print("CLASSIFICAÇÃO: OBESIDADE GRAVE")

# Chama a função para calcular o IMC
imc()

# Pausa a execução do programa por 2 segundos
time.sleep(2)

# Define uma função para exibir um painel informativo
def painel():
    print("-" * 100)
    print(f"{colors['magenta']}VEJA A SEGUIR UMA IMAGEM INFORMATIVA{colors['reset']}".center(100))
    print("-" * 100)

# Chama a função para exibir o painel informativo
painel()

# Pausa a execução do programa por 5 segundos
time.sleep(5)

# Abre e exibe uma imagem informativa sobre obesidade
imagem = Image.open(r"obesidade.jpg")
imagem.show()



