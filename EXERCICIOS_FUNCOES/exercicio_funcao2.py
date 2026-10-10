def elementos_comuns(lista1, lista2):
    
    # Converte os elementos das listas para inteiros antes de criar os conjuntos
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todos os elementos das listas podem ser convertidos para inteiros
if all(item.lstrip('-').isdigit() for item in lista1) and all(item.lstrip('-').isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")



#USO DE I.A PARA AJUDAR NA RESOLUÇÃO DO EXERCÍCIO E EXPLICAÇÃO DO .lstrip E .isdigit.
#POIS EU NÃO SABIA DO USO DESSES ELEMENTOS.