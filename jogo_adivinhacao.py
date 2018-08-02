print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
print()

numero_secreto = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite o seu número: "))
    print()
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    if(acertou):
        print("Você acertou!")
        print()
        break
    else:
        if (maior):
            print("Seu chute foi maior do que o número secreto!")
            print()
        elif (menor):
            print("Seu chute foi menor do que o número secreto!")
            print()
    rodada = rodada + 1

print("Fim de jogo!")
