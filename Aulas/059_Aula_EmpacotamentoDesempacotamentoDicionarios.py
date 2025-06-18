"""
📦 EMPACOTAMENTO E DESEMPACOTAMENTO EM PYTHON
---------------------------------------------
Este código demonstra técnicas avançadas de manipulação de dicionários:
1. Desempacotamento de itens
2. Operador ** para combinar dicionários
3. Uso de **kwargs em funções
"""

# 🔄 Trocando valores entre variáveis
a, b = 1, 2
a, b = b, a  # 🎯 Troca os valores sem variável temporária
# print(a, b)  # 2 1

# 📍 Dicionários de exemplo
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',  # 👩 Dados pessoais básicos
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,  # 📏 Dados adicionais
}

# ✨ Combinando dicionários com **
pessoas_completa = {**pessoa, **dados_pessoa}  # 🆕 Novo dict com todos dados
# print(pessoas_completa)  # {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}

"""
💡 FUNÇÃO COM ARGS E KWARGS
*args coleta argumentos posicionais em uma tupla
**kwargs coleta argumentos nomeados em um dicionário
"""

def mostro_argumentos_nomeados(*args, **kwargs):
    """Exibe argumentos posicionais e nomeados recebidos"""
    print('ARGUMENTOS POSICIONAIS (args):', args)  # 🖨️ Argumentos não nomeados
    
    print('\nARGUMENTOS NOMEADOS (kwargs):')  # 🖨️ Argumentos nomeados
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

# 🧪 Testando a função
print("\n👉 Chamada com argumentos explícitos:")
mostro_argumentos_nomeados(1, 2, 3, nome='Lucas', idade=25)

print("\n👉 Chamada com desempacotamento de dicionário:")
mostro_argumentos_nomeados(**pessoas_completa)  # 📦 Desempacota o dicionário

print("\n👉 Chamada com configurações:")
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)  # 🛠️ Configurações como kwargs

"""
📌 CASOS DE USO COMUNS:
1. Combinação de configurações padrão e personalizadas
2. Funções que aceitam argumentos flexíveis
3. Encadeamento de chamadas de função
4. Herança de dicionários

✨ BOAS PRÁTICAS:
1. Documente sempre os kwargs esperados
2. Use nomes descritivos para argumentos nomeados
3. Prefira kwargs para parâmetros opcionais
4. Use type hints para melhorar a legibilidade
"""

"""
📚 APRENDIZADOS:
1. Como desempacotar dicionários com **
2. Diferença entre *args e **kwargs
3. Técnicas para combinar dicionários
4. Padrões para funções flexíveis
"""