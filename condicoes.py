#Estruturas com if...else

#Exemplo 1
#Quantos anos tem seu carro?
'''tempo = int(input('Quantos anor tem seu carro?'))
if tempo<=3:
    print('Carro novo')
else:
    print('Carro velho')

print('FIM')'''

#==========================================================================================================================================================
#Notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim! Estude mais!!')

#print('Parabens' if m >=6 else 'Estude mais') Condição simplificada