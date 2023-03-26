
numero = (input('Insira uma série de números, separando-os por vírgula: '))
lista = numero.split(",")

for numero in lista:
 numero = int(numero)
 if numero % 2 == 0:
    print(numero)
