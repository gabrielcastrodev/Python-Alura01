print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
print()

numero_secreto = 42
total_tentativas = 3

<<<<<<< HEAD
while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite o seu número: "))
    print()
    
=======
for rodada in range (1, total_tentativas + 1):
    print("Tentativa, {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
>>>>>>> c505983b58ebc6c601b650df19de0c5cffeb3522
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        print()
        continue

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
