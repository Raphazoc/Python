# Estrutura de Repetição: fo
# O laço `for` em Python é utilizado para percorrer sequências (como listas, tuplas, strings ou intervalos de números). É ideal quando sabemos de antemão quantas vezes queremos repetir um bloco de código.


### Exemplo 1: Iterando sobre uma lista
# python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}")


### Exemplo 2: Usando a função range(). A função `range()` gera uma sequência de números, muito útil para repetir ações um número específico de vezes.


# Repete 5 vezes (de 0 a 4)
for i in range(5):
    print(f"Contagem: {i}")


### Exemplo 3: Percorrendo uma string. Como strings são sequências de caracteres, você também pode iterar sobre elas:


palavra = "Python"

for letra in palavra:
    print(letra)

