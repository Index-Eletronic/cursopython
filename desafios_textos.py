#Crie um programa que leia o nome completo de uma pessoa e mostre:

'''nome = str(input('Digete se nome completo: ')).strip() #Elimina os espaços
print('Analisando seu nome...')
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem  {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))'''

#==========================================================================================================================================================

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

'''num = int(input('Informe um numero'))
n = str(num)
print ('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

#==========================================================================================================================================================

#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
