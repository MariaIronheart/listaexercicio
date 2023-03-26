#comando split e strip
lista_palavra = input('Digite uma lista de palavras: ')
lista_palavra = [nome.strip() for nome in lista_palavra.split(', ')]

nomes_com_e = [nome for nome in lista_palavra if "e" in nome.lower()]
print('Nomes com a letra E: ', nomes_com_e)



    