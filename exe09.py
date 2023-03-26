numero = (input('Insira uma série de números, separando-os por vírgula: '))
lista = numero.split(",")

for numero in lista:
 numero = int(numero)
 if numero < 5:
    print(numero)