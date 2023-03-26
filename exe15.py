lista = (input('Insira uma série de números, podendo ter repetição, separdos por vírgula: '))
lista = lista.split(",")
lista_nova = []

while lista:
    elemento = lista.pop(0)  
    if elemento not in lista_nova:
        lista_nova.append(elemento)
        
print('A lista sem duplicatas é: ', lista_nova)