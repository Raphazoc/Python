# 1. range(fim): Gera de 0 até fim-1
print("Exemplo 1 (0 a 4):")
for i in range(5):
    print(i, end=" ")
print("\n")

# 2. range(inicio, fim): Gera de 'inicio' até 'fim-1'
print("Exemplo 2 (5 a 9):")
for i in range(5, 10):
    print(i, end=" ")
print("\n")

# 3. range(inicio, fim, passo): Define o incremento (salto)
# Útil para números pares, ímpares ou contagens regressivas
print("Exemplo 3 (Pulando de 2 em 2):")
for i in range(0, 11, 2):
    print(i, end=" ")
print("\n")

# 4. range com passo negativo (Contagem regressiva)
print("Exemplo 4 (Contagem regressiva):")
for i in range(10, 0, -1):
    print(i, end=" ")