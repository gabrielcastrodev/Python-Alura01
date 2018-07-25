print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
print()

numero_secreto = 42
total_tentativas = 3

while(total_tentativas > 0):
    chute = int(input("Digite o seu número: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    if(acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Seu chute foi maior do que o número secreto!")
        elif (menor):
            print("Seu chute foi menor do que o número secreto!")
    total_tentativas = total_tentativas -1

print("Fim de jogo!")
