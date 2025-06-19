"""
🔍 VERIFICAÇÃO DE TIPOS COM isinstance() EM PYTHON
------------------------------------------------
A função isinstance() verifica se um objeto é instância de um tipo específico.
É mais robusta que type() pois considera herança e pode verificar múltiplos tipos.
"""

lista = [
    'a',         # str
    1,           # int
    1.1,         # float
    True,        # bool (subclasse de int)
    [0, 1, 2],   # list
    (1, 2),      # tuple
    {0, 1},      # set
    {'nome': 'Lucas'},  # dict (substituído 'Luiz' por 'Lucas')
]

for item in lista:
    if isinstance(item, set):
        # 🎯 Conjuntos (set)
        print('✔️ SET - Conjunto mutável')
        item.add(5)  # ✅ Adiciona elemento ao conjunto
        print(item, isinstance(item, set))  # 🖨️ Confirma o tipo

    elif isinstance(item, str):
        # 🔤 Strings
        print('✔️ STR - Sequência de caracteres')
        print(item.upper())  # 🖨️ Versão maiúscula

    elif isinstance(item, (int, float)):
        # 🔢 Números (int ou float)
        print('✔️ NUM - Valor numérico')
        print(item, item * 2)  # 🖨️ Valor e seu dobro

    else:
        # 🎭 Outros tipos
        print('➡️ OUTRO - Tipo não especificado')
        print(item)  # 🖨️ O próprio item

"""
💡 POR QUE USAR isinstance() EM VEZ DE type()?
1. Considera herança (bool é considerado int)
2. Aceita tupla de tipos para verificação
3. Padrão recomendado pela comunidade Python

📌 EXEMPLOS ADICIONAIS:
"""
valor = True
print(isinstance(valor, int))  # True (bool herda de int)
print(isinstance(valor, (int, float, str)))  # True

"""
⚠️ CUIDADOS:
1. Verifique sempre os tipos mais específicos primeiro
2. Evite verificar muitos tipos diferentes
3. Documente as verificações de tipo complexas

✨ BOAS PRÁTICAS:
1. Use para validação de entradas
2. Combine com tratamento de exceções
3. Prefira duck typing quando possível
4. Documente os tipos esperados
"""

"""
📚 APRENDIZADOS:
1. Como verificar tipos de objetos
2. Diferença entre isinstance() e type()
3. Padrões para tratamento de múltiplos tipos
4. Quando usar verificações de tipo
"""