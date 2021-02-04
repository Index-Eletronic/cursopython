from random import randint
lista = list()
cont = 0
while True:
num = randint(1, 60)
    if num in lista:
        lista.append(num)
        cont +=1

