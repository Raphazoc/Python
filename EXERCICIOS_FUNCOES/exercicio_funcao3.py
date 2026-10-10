def contar_caracteres(string): # Função que conta a quantidade de cada caractere em uma string
    
    contador = {} # Dicionário para armazenar a contagem de cada caractere
    
    for char in string: # Itera sobre cada caractere na string
        
        if char in contador: # Verifica se o caractere já está no dicionário
            
            contador[char] += 1 # Incrementa a contagem do caractere 
            
        else: # Se o caractere não estiver no dicionário, adiciona-o com contagem inicial de 1
            
            contador[char] = 1 # Inicializa a contagem do caractere no dicionário
            
    return contador

entrada = input()

# Chama a função contar_caracteres passando a string de entrada e armazena o resultado no dicionário 'resultado'
resultado = contar_caracteres(entrada) 

print(resultado) # Imprime o dicionário contendo a contagem de cada caractere na string de entrada

# Exercicio feito com auxilio parcial de I.A para melhor entendimento do código e explicação do funcionamento do dicionário e da função contar_caracteres. (Parcial = )