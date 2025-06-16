"""
📚 DICIONÁRIOS EM PYTHON (TIPO dict)
------------------------------------
Dicionários são estruturas de dados que armazenam pares de chave-valor.
- Chaves devem ser tipos imutáveis (strings, números, tuplas)
- Valores podem ser de qualquer tipo (incluindo outros dicionários)
- Extremamente versáteis para organizar dados estruturados
"""

# 👤 Criando um dicionário de pessoa
pessoa = {
    'nome': 'Lucas Heitor',      # 🏷️ String como chave
    'sobrenome': 'Barbosa',      # 🏷️ Outra string
    'idade': 18,                 # 🔢 Número inteiro
    'altura': 1.8,               # 📏 Número decimal
    'endereços': [               # � Lista de dicionários
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

# 🔍 Acessando valores específicos
print(pessoa['nome'])       # 🖨️ 'Luiz Otávio'
print(pessoa['sobrenome'])  # 🖨️ 'Miranda'

print()  # 👈 Linha em branco para separar

# 🔄 Iterando sobre todas as chaves e valores
for chave in pessoa:
    print(chave, pessoa[chave])  # 🖨️ Cada par chave-valor

"""
💡 OPERAÇÕES COMUNS EM DICIONÁRIOS:
1. Acessar valores: pessoa['chave'] ou pessoa.get('chave')
2. Adicionar/Modificar: pessoa['nova_chave'] = valor
3. Verificar existência: 'chave' in pessoa
4. Remover: del pessoa['chave'] ou pessoa.pop('chave')

📌 MÉTODOS ÚTEIS:
- .keys(): retorna as chaves
- .values(): retorna os valores
- .items(): retorna pares (chave, valor)
- .update(): mescla dicionários
- .copy(): cria cópia superficial

⚠️ CUIDADOS:
- Acessar chave inexistente com [] causa KeyError
- Prefira .get() quando não tem certeza da existência
- Chaves devem ser únicas (última definição prevalece)
"""

"""
📚 EXEMPLOS AVANÇADOS:
# Criação alternativa
pessoa = dict(nome='Maria', idade=25)

# Dict comprehension
quadrados = {x: x*x for x in range(5)}

# Aninhamento
estoque = {
    'produtos': {
        'camisa': {'preco': 50, 'qtd': 10},
        'calca': {'preco': 100, 'qtd': 5}
    }
}
"""

"""
✨ BOAS PRÁTICAS:
1. Use nomes descritivos para chaves
2. Mantenha estrutura consistente quando possível
3. Para dicionários grandes, considere usar classes
4. Documente a estrutura quando trabalhar em equipe
"""