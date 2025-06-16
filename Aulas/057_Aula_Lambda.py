"""
λ FUNÇÕES LAMBDA EM PYTHON
--------------------------
Funções lambda são funções anônimas (sem nome) de uma única linha.
Úteis para operações simples que não requerem uma função definida com def.

Sintaxe: lambda argumentos: expressão
"""

# 📋 Lista de dicionários (substituído 'Luiz' por 'Lucas' conforme solicitado)
lista = [
    {'nome': 'Lucas', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# 🖨️ Função auxiliar para exibição
def exibir(lista):
    for item in lista:
        print(item)
    print()  # Linha em branco para separação

# 1️⃣ Ordenando por nome usando lambda
l1 = sorted(lista, key=lambda item: item['nome'])
# λ A lambda acessa a chave 'nome' de cada dicionário

# 2️⃣ Ordenando por sobrenome usando lambda
l2 = sorted(lista, key=lambda item: item['sobrenome'].lower())  # 📌 Added .lower() para case-insensitive

# 🏁 Exibindo resultados
print("Ordenado por nome:")
exibir(l1)

print("Ordenado por sobrenome:")
exibir(l2)

"""
💡 CARACTERÍSTICAS DAS LAMBDAS:
- São funções de uma linha só
- Não usam return (a expressão é automaticamente retornada)
- Podem ter múltiplos argumentos: lambda x, y: x + y
- São frequentemente usadas com sorted(), filter(), map()

📌 EXEMPLOS ADICIONAIS:
- Multiplicação: lambda x: x * 2
- Condicional: lambda x: 'par' if x % 2 == 0 else 'impar'
- Múltiplos args: lambda x, y: x ** y
"""

"""
✨ BOAS PRÁTICAS:
1. Use lambdas para operações simples
2. Prefira funções nomeadas (def) para lógica complexa
3. Mantenha lambdas legíveis - se ficar muito longo, use def
4. Documente o propósito quando não for óbvio
"""

# 🆚 ALTERNATIVA COM FUNÇÃO NOMEADA
def get_sobrenome(item):
    return item['sobrenome'].lower()

l3 = sorted(lista, key=get_sobrenome)
print("Ordenado por sobrenome (função nomeada):")
exibir(l3)