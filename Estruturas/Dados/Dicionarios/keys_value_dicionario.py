carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}

# Extrai apenas as chaves

colunas = list(carro.keys())
print(f"\nCampos disponíveis: {colunas}")

#Extrai apenas os valores

dados = list(carro.values())
print(f"\nDados do carro: {dados}")