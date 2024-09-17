# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule o salário total e exiba o resultado.
# Considere que você trabalha 20 dias no mês.

qnt_hora = float(input('Digite quanto você ganha por hora: '))
num_horas = int(input('Digite as horas trabalhadas por dia: '))
dias_trabalhados = 20 
num_horas_mes = dias_trabalhados * num_horas

salario_total = (qnt_hora * num_horas) * dias_trabalhados

print(f'Quantidade por horas: {qnt_hora}')
print(f'Número de horas trabalhadas no mês: {num_horas_mes}')
print(f'Seu salário total é de: {salario_total}:.2f')