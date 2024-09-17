# Objetivo: Peça ao usuário para digitar seu nome, idade e cidade natal. 
# Use uma f-string para formatar e exibir uma mensagem com essas informações.

nome_usuario = input('Digite seu nome: ')
idade_usuario = int(input('Digite sua idade: '))
cidade_natal = input('Digite sua cidade natal: ')

print(f'Nome: {nome_usuario}')
print(f'Idade: {idade_usuario}')
print(f'Cidade natal: {cidade_natal}')