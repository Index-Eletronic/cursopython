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

'''cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')'''

#==========================================================================================================================================================

#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

'''nome = str(input('Qual e seu nome completo')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))'''

#==========================================================================================================================================================

#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

'''frase = str(input('Digite uma frase')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format((frase.rfind('A')+1)))'''

#==========================================================================================================================================================

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo')).strip()
nome = n.split()
print('Seu primeiro nome: '.format(nome[0]))
print('Seu ultimo nome: '.format(nome[len(nome)-1]))

