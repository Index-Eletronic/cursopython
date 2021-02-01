# Operadores Aritiméticos
# 5**2 = potencia -> 5x5
#5 // 2 = Divisão inteira ->2
#5 % 2 = Resto da divisão -> 1

# Ordem de precedencia: 1( ), 2**, 3 * / // %, 4 + -.

nome = str(input('Qual seu nome? '))
print('Eu um prazer te conhecer {:^20}!'.format(nome))
print('Eu um prazer te conhecer {:>20}!'.format(nome))
print('Eu um prazer te conhecer {:<20}!'.format(nome))
print('Eu um prazer te conhecer {:=^20}!'.format(nome), end='')
# End é para não quebrar a linha
# Se utilizar \n cria uma nova linha



