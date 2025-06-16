"""
🔑 MANIPULAÇÃO DE CHAVES E VALORES EM DICIONÁRIOS
--------------------------------------------------
Este código demonstra operações essenciais para trabalhar com dicionários:
- Adição de pares chave-valor
- Modificação de valores
- Remoção de chaves
- Verificação segura de existência de chaves
"""

# 📦 Criando um dicionário vazio
pessoa = {}  # Também pode ser pessoa = dict()

# 🏷️ Definindo a chave dinamicamente
chave = 'nome'

# ➕ Adicionando pares chave-valor
pessoa[chave] = 'Luiz Otávio'  # Adiciona 'nome': 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'  # Adiciona 'sobrenome': 'Miranda'

# 🔍 Acessando valor através de variável chave
print(pessoa[chave])  # 🖨️ 'Luiz Otávio'

# ✏️ Modificando um valor existente
pessoa[chave] = 'Maria'  # Altera 'nome' para 'Maria'

# 🗑️ Removendo uma chave
del pessoa['sobrenome']  # Remove a chave 'sobrenome'
print(pessoa)  # 🖨️ {'nome': 'Maria'}

# ⚠️ Acessando chave removida (geraria KeyError se não comentado)
# print(pessoa['sobrenome'])  # Removido para evitar erro

# 🛡️ Verificação segura com .get()
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')  # 🖨️ Chave não existe
else:
    print(pessoa['sobrenome'])

"""
💡 PRINCIPAIS APRENDIZADOS:
1. Podemos usar variáveis como chaves (pessoa[chave])
2. del remove permanentemente uma chave-valor
3. .get() é seguro para verificar existência de chaves
4. Tentar acessar chave inexistente com [] causa KeyError

📌 MÉTODOS ÚTEIS PARA MANIPULAÇÃO:
- .pop(): remove e retorna o valor
- .setdefault(): retorna valor ou cria padrão
- .update(): atualiza múltiplos valores

🔍 EXEMPLO AVANÇADO:
dados = {}
chave = input('Digite a chave: ')
valor = input('Digite o valor: ')
dados[chave] = valor  # Adiciona com inputs do usuário
"""

"""
⚠️ CUIDADOS IMPORTANTES:
1. Chaves são case-sensitive ('Nome' ≠ 'nome')
2. Evite modificar dicionário enquanto itera sobre ele
3. Prefira .get() quando não tem certeza da existência
4. Dicionários mantêm ordem de inserção (Python 3.7+)
"""

"""
✨ BOAS PRÁTICAS:
1. Use nomes descritivos para chaves
2. Documente a estrutura do dicionário
3. Considere defaultdict para valores padrão
4. Para dados complexos, avalie usar classes
"""