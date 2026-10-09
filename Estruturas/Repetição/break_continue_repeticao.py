# O 'break' encerra completamente o loop.
# Quando a condição é atingida, o Python sai do laço e ignora as repetições restantes.
print("Exemplo de break:")
for i in range(10):
    if i == 5:
        print("Loop interrompido no 5!")
        break  # Interrompe o laço totalmente
    print(f"Valor: {i}")

# O 'continue' pula apenas a iteração atual.
# Quando a condição é atingida, o Python ignora o que vem abaixo e pula para a próxima volta do laço.
print("\nExemplo de continue:")
for i in range(10):
    if i % 2 == 0:
        # Se for par, o código abaixo deste 'if' não será executado nesta rodada
        continue 
    print(f"Número ímpar: {i}")