lista = (input('Insira uma série de números, podendo ter repetição, separdos por vírgula: '))
lista = [int(numero) for numero in lista.split(",")]

contagem = {}
for numero in lista:
    if numero not in contagem:
        contagem[numero] = 1
    else:
        contagem[numero] +=1
        
numero_repetido = [numero for numero in contagem if contagem[numero] > 1]

        
print('Números replicados: ', numero_repetido)