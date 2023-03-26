nomes = input('Digite uma lista de nomes separados por vírgula: ')
nomes = [nome.strip() for nome in nomes.split(',')]
lista_nova = []

for nome in nomes:
    if (len(nome))%2==1:
        lista_nova.append(nome)
print(lista_nova)