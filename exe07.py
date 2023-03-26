strings = list()
strings = (input('Digite uma lista de palavras: '))
strings = strings.split(', ')

mais_longo = max(strings, key=len)
mais_curto = min(strings, key=len)

print(mais_longo)
print(mais_curto)