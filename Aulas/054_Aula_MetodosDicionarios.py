"""
📚 MÉTODOS ÚTEIS PARA DICIONÁRIOS EM PYTHON
-------------------------------------------
Dicionários possuem vários métodos embutidos para manipulação eficiente.
Aqui estão os principais com exemplos práticos:
"""

# 👤 Criando um dicionário de exemplo
pessoa = {
    'nome': 'Lucas Heitor',
    'sobrenome': 'Barbosa',
    'idade': 900,  # 🧙 Valor intencionalmente alto para exemplo
}

# 1️⃣ setdefault() - Define valor padrão se chave não existir
pessoa.setdefault('idade', 0)  # ❌ 'idade' já existe, não altera
pessoa.setdefault('altura', 1.75)  # ✅ Adiciona 'altura': 1.75
print(pessoa['idade'])  # 🖨️ 900 (valor original mantido)

# 2️⃣ len() - Número de pares chave-valor
print(len(pessoa))  # 🖨️ 4 (nome, sobrenome, idade, altura)

# 3️⃣ keys() - Retorna visão das chaves
print(list(pessoa.keys()))  # 🖨️ ['nome', 'sobrenome', 'idade', 'altura']

# 4️⃣ values() - Retorna visão dos valores
print(list(pessoa.values()))  # 🖨️ ['Lucas Heitor', 'Barbosa', 900, 1.75]

# 5️⃣ items() - Retorna visão de pares (chave, valor)
print(list(pessoa.items()))  # 🖨️ [('nome', 'Lucas...'), ('sobrenome', 'Barbosa'), ...]

# 🔄 Iterando com values()
for valor in pessoa.values():
    print(valor)  # 🖨️ Cada valor do dicionário

# 🔄 Iterando com items()
for chave, valor in pessoa.items():
    print(chave, valor)  # 🖨️ Cada par chave-valor

"""
💡 MÉTODOS ADICIONAIS:

6️⃣ copy() - Cópia superficial
copia = pessoa.copy()

7️⃣ get() - Acesso seguro
print(pessoa.get('peso', 'Não especificado'))  # 🖨️ 'Não especificado'

8️⃣ pop() - Remove por chave
idade = pessoa.pop('idade')  # Remove e retorna 900

9️⃣ popitem() - Remove último item
ultimo = pessoa.popitem()  # Remove ('altura', 1.75)

🔟 update() - Atualiza com outro dict
pessoa.update({'peso': 70, 'altura': 1.80})
"""

"""
📌 CARACTERÍSTICAS IMPORTANTES:
- As visões (keys(), values(), items()) refletem alterações no dicionário
- setdefault() é atômico e thread-safe
- popitem() útil para processar itens em ordem LIFO
- update() pode receber qualquer iterável de pares chave-valor
"""

"""
✨ BOAS PRÁTICAS:
1. Use get() para acessos seguros a chaves opcionais
2. Prefira update() para múltiplas atualizações
3. Use dict comprehension para transformações
4. Documente a estrutura esperada do dicionário
"""