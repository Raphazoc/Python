# Operadores lógicos em Python

# AND: Retorna True se ambas as condições forem verdadeiras
print(True and True)    # True
print(True and False)   # False

# OR: Retorna True se pelo menos uma condição for verdadeira
print(True or False)    # True
print(False or False)   # False

# NOT: Inverte o valor booleano
print(not True)         # False
print(not False)        # True

# Exemplo com variáveis
idade = 20
tem_permissao = True

if idade >= 18 and tem_permissao:
    print("Acesso concedido")
else:
    print("Acesso negado")
