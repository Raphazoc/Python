funcionarios = [
    {"id": 1, "nome": "Raphael", "Cargo": "Desenvolvedor"},
    {"id": 2, "nome": "Maria", "Cargo": "Analista"},
    {"id": 3, "nome": "João", "Cargo": "Gerente"} ]

# Percorrendo os registros

for pessoa in funcionarios:
    print(f"\n{pessoa['nome']} trabalha como {pessoa['Cargo']}.")