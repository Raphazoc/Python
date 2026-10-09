class MaquinaDeCafe:
    def __moer_graos(self):
        print("Moendo os grãos de café...")

    def __aquecer_agua(self):
        print("Aquecendo a água...")
    
    def __extrair_cafe(self):
        print("Extraindo o café...")
        
    def preparar_cafe(self):
        self.__moer_graos()
        self.__aquecer_agua()
        self.__extrair_cafe()
        print("\nCafé pronto!")
        
# Usando um if para verificar se o cliente pagou ou não. Se sim, a máquina de café será acionada para preparar o café. Caso contrário, uma mensagem será exibida informando que não é possível preparar o café.

cliente_pagou = input("O cliente pagou? (s/n): ") 
if cliente_pagou.lower() == 's':
        print("\nO cliente pagou. Preparando o café...")
        maquina = MaquinaDeCafe()
        maquina.preparar_cafe()
        
else: 
    print("O cliente não pagou. Não é possível preparar o café.")
    



# Abstração é um conceito de programação que permite ocultar os detalhes de implementação de uma classe e expor apenas a interface necessária para o usuário interagir com ela. No exemplo acima, a classe `MaquinaDeCafe` possui métodos privados (`__moer_graos`, `__aquecer_agua`, `__extrair_cafe`) que não são acessíveis diretamente pelo usuário da classe. O método público `preparar_cafe` é a interface que o usuário utiliza para preparar o café, sem precisar se preocupar com os detalhes internos do processo.

