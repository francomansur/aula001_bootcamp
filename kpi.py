# 1) Solicita ao usuário que digite seu nome
nome = input('Digite seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = input('Qual seu salário? ')
salario = round(float(salario), 2)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = input('Qual o bônus recebido? ')
bonus = float(bonus)
print('')

# 4) Calcule o valor do bônus final
total = salario + bonus

# 5) Imprima cálculo do KPI para o usuário
print('O cálculo da KPI é: salário + bônus')

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'{nome}, seu salário com bônus é de: {salario} + {bonus} = {total}')
print('')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?