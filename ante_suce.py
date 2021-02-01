#Desafio: Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite o numero aqui !!'))
ant = int(n-1)
suc = int(n+1)
print('O numero digitado é: {}''\n E seu antecessor è: {}''\n E seu sucessor é: {}'.format(n, ant, suc))
print ('O numero digitado é: {}''\n E seu antecedor é: {}''\n E seu sucessor é: {}'.format(n, n-1, n+1)) # Não precisa criar mais 2 variaveis

#Media Aritmetica: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota do aluno'))
n2 = float(input('Digite a segunda nota do aluno'))
m = (n1+n2)/2
print('A média é: {:.1f}'.format(m))# Depois do ponto flutuante coloque 1 digito.

#Conversor de medidas; Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n3 = float(input('Digite um valor em mentros'))
print('A valor digitado é: {}metros''\n Em centimetros é: {:.0f}cm''\n Em milimetros é: {:.0f}mm'.format(n3, n3*100, n3*1000))

