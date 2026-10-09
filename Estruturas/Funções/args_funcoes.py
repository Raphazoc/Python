# Funções args podem receber um número variável de argumentos. No exemplo abaixo, a função somar_tudo() recebe um número indefinido de argumentos usando o operador * antes do parâmetro numeros. Isso permite que a função aceite qualquer quantidade de números como entrada e os some usando a função sum(). O resultado é então retornado e exibido no terminal usando o comando print().


def somar_tudo(*numeros):
    return sum(numeros)

resultado = somar_tudo(1, 2, 3, 4, 5)
print(resultado)  # Saída: 15


# Funções kwargs podem receber um número variável de argumentos nomeados. No exemplo abaixo, a função apresentar_info() recebe um número indefinido de argumentos nomeados usando o operador ** antes do parâmetro info. Isso permite que a função aceite qualquer quantidade de informações adicionais como entrada e as exiba no terminal usando o comando print().

def apresentar_info(**info):
    for chave, valor in info.items(): # Itera sobre os itens do dicionário info, onde chave é a chave do argumento nomeado e valor é o valor correspondente.
        print(f"{chave}: {valor}")

apresentar_info(nome="João", idade=30, cidade="São Paulo")