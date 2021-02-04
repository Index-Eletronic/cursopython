#Porgrama pyton para conferir dados da mega sena sem Banco de Dados.

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' *30)
print(' JOGA NA MEGA SENA')
print('-' *30)
nome = str(input('Qual seu nome?')).strip()
quant = int(input('Quantos jgos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont +=1
    if cont >= 6:
        break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(2)
print('-='*5, '<BOA SORTE!> {}','-=*5'.format(nome))



