from random import randint
from time import sleep

print("JOKENPÔ")
print ("-=-" * 20)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)

print('''Suas opções:\n
[0] PEDRA 
[1] PAPEL
[2] TESOURA ''')

jogador = int(input("\nQual sua jogada: "))

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)

print('-=-' * 25)

print("O jogador escolheu {}." .format(itens[jogador]))
print("O computador escolheu {}." .format(itens[computador]))

print('-=-' * 25)

if computador == 0: #COMPUTADOR ESCOLHEU PEDRA
    if jogador == 0:
        print("EMPATE.")

    elif jogador == 1:
        print("JOGADOR VENCEU!")

    elif jogador == 2:
        print("COMPUTADOR VENCEU!")

if computador == 1: #COMPUTADOR ESCOLHEU PAPEL
    if jogador == 1:
        print("EMPATE.")

    elif jogador == 2:
        print("JOGADOR VENCEU!")

    elif jogador == 0:
        print("COMPUTADOR VENCEU!")

if computador == 2: #COMPUTADOR ESCOLHEU TESOURA
    if jogador == 2:
        print("EMPATE.")

    elif jogador == 0:
        print("JOGADOR VENCEU!")

    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
