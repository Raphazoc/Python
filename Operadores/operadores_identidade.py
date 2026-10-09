# Operadores de identidade (is, is not)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# 'is' verifica se as variáveis apontam para o mesmo objeto na memória
print(a is c)     # True (mesmo objeto)
print(a is b)     # False (objetos diferentes, mesmo tendo o mesmo conteúdo)

# 'is not' verifica se as variáveis apontam para objetos diferentes
print(a is not b) # True
