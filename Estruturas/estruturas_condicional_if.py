idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Acabou de atingir a maioridade")
else:
    print("Maior de idade")
    
    
# 1. Operador Ternário (Condicional de uma linha)
# É uma forma concisa de escrever uma atribuição baseada em uma condição. 

status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)


