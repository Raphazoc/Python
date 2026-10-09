# 1. Inicialização: Define o ponto de partida
contador = 1 

# 2. Condição: O laço verifica: "contador é menor ou igual a 5?"
# Se sim, executa o bloco. Se não, encerra o programa.

while contador <= 5:
    print(f"Contagem: {contador}")
    
    
    
    # 3. Incremento/Atualização: 
    # Fundamental para evitar o "loop infinito". 
    # Sem isso, contador seria sempre 1 e o laço nunca terminaria.
    contador += 1 
