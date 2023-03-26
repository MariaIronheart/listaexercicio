lista_palavra = input('Digite uma lista de palavras: ')
lista_palavra = lista_palavra.split(', ')

for palavra in lista_palavra:
    if palavra.startswith('a') or palavra.startswith('A'):
        print(palavra)
    
    