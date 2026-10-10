def somar_tupla(tupla):
    return sum(tupla) # Retorna a soma dos elementos da tupla usando a função sum 

if __name__ == "__main__":
    entrada = input("Digite os elementos da tupla separados por espaço: ") # Recebe a entrada do usuário como uma string
    
    elementos = tuple(map(int, entrada.split())) # Converte a string em uma tupla de inteiros usando map e split
    
    resultado = somar_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")