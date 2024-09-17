# Modo difícil:

num = int(input("Digite um número:"))

tabuada1 = num*1
tabuada2 = num*2
tabuada3 = num*3
tabuada4 = num*4
tabuada5 = num*5
tabuada6 = num*6
tabuada7 = num*7
tabuada8 = num*8
tabuada9 = num*9
tabuada10 = num*10

print('A tabuada do seu número é:')
print(f'{num} x 1 = {tabuada1}')
print(f'{num} x 2 = {tabuada2}')
print(f'{num} x 3 = {tabuada3}')
print(f'{num} x 4 = {tabuada4}')
print(f'{num} x 5 = {tabuada5}')
print(f'{num} x 6 = {tabuada6}')
print(f'{num} x 7 = {tabuada7}')
print(f'{num} x 8 = {tabuada8}')
print(f'{num} x 9 = {tabuada9}')
print(f'{num} x 10 = {tabuada10}')

# Modo simplificado:

numero = int(input('Digite um número: '))
controlador = 1
while controlador <= 10:
    print(f'{controlador} x {numero} = {controlador * numero}')
    # controlador = controlador + 1
    controlador += 1