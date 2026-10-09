def apresentar(nome, cargo="Desenvolvedor(a)"):
    return(f"Olá! Meu nome é {nome} e eu sou {cargo}.")

print(apresentar("João", "Engenheiro de Software")) 
print(apresentar("Maria"))  # Usando o valor padrão para o parâmetro cargo e ja que não foi fornecido um valor para ele, o valor padrão "Desenvolvedor(a)" será usado.

# Funções podem ter parâmetros com valores padrão. No exemplo acima, a função apresentar() tem dois parâmetros: nome e cargo. O parâmetro cargo tem um valor padrão definido como "Desenvolvedor(a)". Se nenhum valor for fornecido para o parâmetro cargo ao chamar a função, o valor padrão será usado. No exemplo, chamamos a função com os argumentos "João" e "Engenheiro de Software", e o resultado é exibido no terminal usando o comando print().