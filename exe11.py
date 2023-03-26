numeros = (input('Insira uma série de números, separando-os por vírgula: '))
numeros = numeros.split(",")
soma = 0
for numero in numeros:
 if int(numero) % 2 == 1:
  soma+= int(numero)

print('A soma é ', soma)
    
