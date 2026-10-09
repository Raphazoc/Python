precos = [10, 20, 30, 40, 50]


#Aplica um aumento de 10% nos preços da lista 
precos_com_impostos = [valor * 1.10 for valor in precos]

#Preços originais e preços com impostos
print(f"\nPreços originais: {precos}")
print(f"Preços com impostos: {precos_com_impostos}")


print ("\n===========================================")


print("\nFiltrando valores: cria uma lista so com os numeros pares")


pares = [num for num in range(1, 11) if num % 2 == 0]
print(f"\nNúmeros pares de 1 a 10: {pares}")    