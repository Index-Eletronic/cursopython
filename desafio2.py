# Manipulação de Textos.
'''operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String,
 Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join(). '''

frase = 'Curso em Video Python'
print(frase[3]) # Quarta letra
print(frase[3:13])
print(frase[:13]) # Do inico até o 12
print(frase[1:15:2])
print(frase[1::2])
print(frase.upper().count()) # frase é uma cadeia de caracteres mas NO PYTHON TUDO É UM OBJETO. Qualquer coisa (.) alguma coisa
print(frase.replace('Python, Android')) # Não salva o resultado da troca.
frase = frase.replace('Puthon, Android') # Salva a nova frase.
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[2]) # Dividido e uma lista
print(dividido[2][3]) # qual letra esta na posição 3 da palavra 2.







