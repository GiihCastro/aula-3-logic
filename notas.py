# Objetivo: Criar um Programa que Peça as 4 Notas Bimestrais e Mostre a Média

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))

media_final = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Média das notas: {media_final}')