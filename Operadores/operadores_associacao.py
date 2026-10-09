# Operadores de associação (in, not in)

frutas = ["maçã", "banana", "laranja"]

print("maçã" in frutas)      # True
print("uva" in frutas)       # False
print("uva" not in frutas)   # True

# Exemplo com string
nome = "Python"
print("P" in nome)        # True
print("py" in nome)       # False (diferencia maiúsculas/minúsculas)

# Exemplo com dicionário
dados = {"nome": "Alice", "idade": 25}
print("nome" in dados)    # True (verifica apenas as chaves)
print("Alice" in dados)   # False
print("idade" not in dados) # False
