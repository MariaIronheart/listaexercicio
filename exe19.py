numeros = input('Digite uma série de números separados por vírgula: ')
divisor = input('Digite um número para ser o divisor: ')
divisor = int(divisor)
numeros = [int(numero) for numero in numeros.split(",")]
nova_lista = []

for numero in numeros:
    if numero % divisor == 0:
        nova_lista.append(numero)
print(nova_lista)