print("\nOrdenação e Reversão") 

pontuacoes = [45, 12, 89, 33, 67]

pontuacoes.sort(reverse=True)  # Ordena a lista em ordem decrescente    

print(f"\nLista original alterada: {pontuacoes}")
## Resultado: [89, 67, 45, 33, 12]


## Métodos usados: .sort() - Ordena a lista em ordem crescente por padrão. O parâmetro reverse=True inverte a ordem para decrescente.


print("\n===========================================")


print("\nCriando uma cópia ordenada, sem tonar na original")

letras = ['z', 'a', 'c']

letras_ordenadas = sorted(letras)

print(f"\nLista original: {letras}")
print(f"Lista ordenada: {letras_ordenadas}")

## Metodos usados: sorted() - Retorna uma nova lista ordenada, sem alterar a lista original.
