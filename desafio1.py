'''Crie em programa que leia um numero Real qulauqer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
num = float(input('Digite um valor0'))
print('O Valor digite fo {} e a sua ´porção inteira é{}'.format(num, trunc(num)))'''
#==========================================================================================================================================================
'''#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
#--------------------Outra maneira ------------------------------------
'''from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)'''

#==========================================================================================================================================================
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que você deseja'))
seno = sin(radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o angulo de {} tem a TANGENTE de {;.2f}'.format(angulo, tangente))'''
#==========================================================================================================================================================
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''
#==========================================================================================================================================================
#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)'''
#==========================================================================================================================================================
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()
pygame.event.wait()










