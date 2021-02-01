#Tabuada:Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
num = int(input('Digite a tabuada'))
print('-'*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12)

#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, defina o redimento de litro de tinta por metros quadrados.

larg = float(input('Lardura da parede: '))
alt = float(input('Altura da parede: '))
rend = float(input('Rendimento da tinta por m²: '))
area = larg*alt
print('Sua parede tem a dimensão de  {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area/rend
print('Para pintar essa parede, você irá precisar de {}l de tinta'.format(tinta))

