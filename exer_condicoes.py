#==========================================================================================================================================================
# Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#Programa deverá escrever na tela se o usuario vendeu ou perdeu.
'''from random import  randint
from time import sleep
computador = randint(0, 5) # Faz o computador pensar num numero
print('-=-' * 20 )
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))# Jogador tenta adivinhar
print('Processando')
sleep(2) # A função faz o computador esperar.
if computador == jogador:
    print('Você ACERTOU !!!')
else:
    print('Eu pensei no numero {} e não no numero {}'.format(computador, jogador))'''

#==========================================================================================================================================================
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendoq ue ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
'''velomax = 80
velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade-velomax)*7
if velocidade > velomax:
    print('MULTADO ! Você excedeu o limite permitido que é de 80km/h')
    print('Você será multado em R$ {:.2f} reais.'.format(multa))
else:
    print('Bom dia dirija com segurança !!')'''
#==========================================================================================================================================================
#Escreva um programa que leia um numero inteiro e mostre na tela se ele é Par ou Impar.
'''numero = int(input(' Digite um numero inteiro qualquer: '))
resultado = numero % 2 # O resto da divisão de qualuqer numero por 2 se for 0 é par se for 1 é impar.
if resultado == 0:
    print(' Este numero {} é par'.format(numero))
else:
    print('Este numero {} é impar'.format(numero))'''
#==========================================================================================================================================================
#Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200km
#e R$0,45 para viagens mais longas
'''distancia = int(input('Digite a distancia da viagem? '))
if distancia <= 200:
    passagem = distancia*0.50
else:
    passagem = distancia * 0.45
print('O valor da sua passagem é: R${:.2f}'.format(passagem))

 preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45'''



#==========================================================================================================================================================
#Faça um programa que leia um ano quaolquer e mostre se ele é bissexto.
'''from datetime import date
ano = int(input('Qual ano você quer analisar ou coloque 0 para analisar a data atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # and (e tambem)  != (diferente)  or(ou então
    print('O ano {} é BISSEXTO'.format((ano)))
else:
    print('O Ano {} não é BISSEXTO'.format(ano))'''

#==========================================================================================================================================================
#Faça um programa que leia tres numeros e mostre qual é o maior e qual o menor.
'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando o maior Valor
menor = a
if b<a and c<a:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi: {}'.format(menor))
#Verificando o maior Valor:
maior = a
if b>a and c>a:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi: {}'.format(maior))
'''
#==========================================================================================================================================================
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00 calcule um aumento de 10 %
#Para inferiores ou iguais o aumento pe de 15 %.
'''
salario = float(input('Qual ´o salario do colaborador? '))
if salario > 1250:
    aumento = salario*1.10
else:
    aumento = salario*1.15

diferenca = aumento-salario

print('o colaborador teve R$ {:.2f} reais de aumento e seu salario passa a ser R$ {:.2f} reais'.format(diferenca, aumento))
'''

#==========================================================================================================================================================
#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triangulo.
print('-=-' * 20)
print('Analisando o triangulo')
print('-=-' * 20)
r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3  and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um trinângulo')
else:
    print('Os seguimentos acima não podem formar um triangulo')


