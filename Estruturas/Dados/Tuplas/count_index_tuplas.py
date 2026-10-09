sorteio = (15, 8, 23, 8, 42, 8)

# Conta quantas vezes o número 8 aparece
quantidade_oito = sorteio.count(8)

# Descobre em qual posição (índice) o número 42 está
posicao_quarenta_e_dois = sorteio.index(42)

print(f"O número 8 saiu {quantidade_oito} vezes.")
print(f"O 42 está no índice {posicao_quarenta_e_dois}.")
# Resultado: O número 8 saiu 3 vezes. | O 42 está no índice 4.