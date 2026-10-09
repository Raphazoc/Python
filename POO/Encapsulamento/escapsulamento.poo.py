# Exemplo de encapsulamento em Python. 

# A classe Cofre representa um cofre que armazena um conteúdo confidencial protegido por uma palavra-passe.
class Cofre: 
    
     # O método __init__ é o construtor da classe Cofre. Ele recebe a palavra-passe como argumento e a armazena em um atributo privado chamado __palavra_passe. Além disso, define o conteúdo do cofre como "Documento Confidencial", que também é armazenado em um atributo privado chamado __conteudo.
    def __init__(self, palavra_passe):
        self.__palavra_passe = palavra_passe
        self.__conteudo = "Documento Confidencial"
        
    def tentar_abrir(self, tentativa):
        if tentativa == self.__palavra_passe:
            print("Acesso concedido! Conteúdo do cofre:", self.__conteudo)
        else:
            print("Acesso negado! Palavra-passe incorreta.")
# ===============================Fim da Classe==============================================
            
meu_cofre = input("Digite a palavra-passe para criar o cofre: ") # input chamado fora da classe Cofre, para que o usuário possa definir a palavra-passe do cofre.

meu_cofre = Cofre(meu_cofre)  # meu_cofre = Cofre(meu_cofre), =A variável meu_cofre é uma instância da classe Cofre, criada com a palavra-passe fornecida pelo usuário.

meu_cofre.tentar_abrir("senha123")  # meu_cofre.tentar_abrir("senha123") = O método tentar_abrir é chamado com a tentativa de senha "senha123". Se a senha estiver correta, o conteúdo do cofre será exibido; caso contrário, uma mensagem de acesso negado será mostrada.

# tentar_abrir recebe a senha "senha123" como argumento e compara com a senha armazenada no atributo privado __palavra_passe. Se a senha estiver correta, o conteúdo do cofre é exibido; caso contrário, uma mensagem de acesso negado é mostrada.


# O encapsulamento é uma característica da programação orientada a objetos que permite proteger os dados de uma classe, tornando-os inacessíveis diretamente de fora da classe. No exemplo acima, os atributos __palavra_passe e __conteudo são privados, o que significa que não podem ser acessados diretamente de fora da classe Cofre. Isso garante que apenas métodos da própria classe possam manipular esses dados, promovendo segurança e integridade das informações armazenadas no cofre.

# Métodos criandos dentro da classe podem ser exportados para interagir com os atributos privados, como o método tentar_abrir, que permite verificar a senha e acessar o conteúdo do cofre de forma controlada.