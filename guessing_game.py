# Importando biblioteca
import random

def jogo_adivinhacao():
    """Inicia o Jogo da Adivinhação."""
    print("=== Bem vindo ao Jogo da Adivinhação! ===")
    print("Tente adivinhar o número que estou pensando.")

    # Definindo o intervalo do número a ser adivinhado
    limite_inferior = int(input("Digite o limite inferior: "))
    limite_superior = int(input("Digite o limite superior: "))

    # Gerando o número aleatório 
    numero_secreto = random.randint(limite_inferior, limite_superior)
    tentativas = 0
    acertou = False

    print(f"\nEstou pensando em um número entre {limite_inferior} e {limite_superior}. Boa Sorte!")

    # Loop principal do jogo
    while not acertou:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
                acertou = True
        except ValueError:
            print("Por favor, insira um número válido.")

    print("\n=== Fim do jogo! ===")


if __name__ == "__main__":
    jogo_adivinhacao()