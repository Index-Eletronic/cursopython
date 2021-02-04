#Porgrama pyton para conferir dados da mega sena sem Banco de Dados.
from random import sample
from time import sleep
jogos = list()
print('-' *30)
print(' JOGA NA MEGA SENA')
print('-' *30)
nome = str(input('DIGITE SEU NOME: ')).upper()
n= int(input('Quantos jgos você quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {n} JOGOS', '-='*3)
for c in range(n):
  a=sorted(sample(range(1, 61), 6))
  jogos.append(a[:])
  print(f'Jogo {c+1}: {a}')
  sleep(0.5)
print('-='*5, '<BOA SORTE! {} >'.format(nome).upper(),'-='*5)
sair = input('ENTER PARA SAIR')




