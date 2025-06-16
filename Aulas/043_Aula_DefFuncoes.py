"""
📌 INTRODUÇÃO A FUNÇÕES (DEF) EM PYTHON
----------------------------------------
Funções são blocos de código reutilizáveis que:
1. Organizam o código em lógicas separadas
2. Evitam repetição
3. Podem receber parâmetros
4. Podem retornar valores (None por padrão)
"""

# 🏗️ Exemplo básico de definição de função
def saudacao(nome='Sem nome'):  # 📝 Parâmetro com valor padrão
    """Documentação: Exibe saudação personalizada"""  # 📚 Docstring
    print(f'Olá, {nome}!')  # 🖨️ Saída formatada

# 🚀 Chamadas da função com diferentes argumentos
saudacao('Guiana')       # 👤 Argumento fornecido
saudacao('Maria')        # 👩 Argumento fornecido
saudacao('Helena')       # 👵 Argumento fornecido
saudacao()               # 👻 Usando valor padrão

"""
💡 PRINCÍPIOS FUNDAMENTAIS:
1. Definição: usa a palavra-chave `def`
2. Nomeação: siga snake_case e seja descritivo
3. Parâmetros: entre parênteses, com valores opcionais
4. Corpo: indentado com 4 espaços
5. Docstring: documentação entre aspas triplas

📌 EXEMPLOS COMENTADOS:
"""
# Função sem retorno explícito (retorna None)
def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)  # 🖨️ 1 2 3
imprimir(4, 5, 6)  # 🖨️ 4 5 6

# Função com múltiplos prints
def mostrar_mensagens():
    print('Mensagem 1')
    print('Mensagem 2')
    print('Mensagem 3')

"""
✨ BOAS PRÁTICAS:
1. Funções devem fazer UMA coisa bem feita
2. Nomes verbosos (ex: calcular_imc())
3. Limite de 3-4 parâmetros (use *args se necessário)
4. Type hints para melhor documentação
   Ex: def saudacao(nome: str = 'Sem nome') -> None:
"""

"""
⚠️ ARMADILHAS COMUNS:
1. Efeitos colaterais não óbvios
2. Parâmetros mutáveis como padrão (ex: listas)
3. Funções muito longas (mais de 10-15 linhas)
"""

"""
📚 APRENDIZADOS:
1. Sintaxe básica de definição
2. Uso de parâmetros e argumentos
3. Valores padrão
4. Organização de código em funções
5. Princípios de funções bem escritas
"""