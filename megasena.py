#Jogos da mega sena.
import random

num1 = random.randint(1, 10)
num2 = random.randint(11, 20)
num3 = random.randint(21, 30)
num4 = random.randint(31, 40)
num5 = random.randint(41, 50)
num6 = random.randint(51, 60)
nome = str(input('Digite seu nome: '))

print('Hoje é seu dia de sorte {} seu jogo é: '.format(nome))
print('Jogo 1: {} {} {} {} {} {}'.format(num1, num2, num3, num4, num5, num6))
stop = input()
