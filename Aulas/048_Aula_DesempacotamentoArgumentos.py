"""
📦 *ARGS EM PYTHON: EMPACOTAMENTO DE ARGUMENTOS
----------------------------------------------
O *args permite que funções recebam um número variável de argumentos posicionais.
Os valores são empacotados em uma tupla dentro da função.
"""

# 🎯 Exemplo básico de desempacotamento (comentado)
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)  # 1 2 [3, 4]

def soma(*args):
    """
    Soma um número variável de valores.
    
    Args:
        *args: Números a serem somados (empacotados como tupla)
        
    Returns:
        int/float: Soma total dos valores
    """
    total = 0
    for numero in args:  # args é uma tupla
        total += numero
    return total

# 🧪 Chamadas com diferentes números de argumentos
soma_1_2_3 = soma(1, 2, 3)  # 👉 6
soma_4_5_6 = soma(4, 5, 6)  # 👉 15

# 🎛️ Desempacotando iteráveis com *
numeros = (1, 2, 3, 4, 5, 6, 7, 78, 10)
outra_soma = soma(*numeros)  # 👉 Equivalente a soma(1, 2, 3,...)
print(outra_soma)  # 🖨️ 116

# ⚡ Versão built-in (comparação)
print(sum(numeros))  # 🖨️ 116 (mesmo resultado)

"""
💡 DIFERENÇA ENTRE *ARGS E **KWARGS:
- *args → empacota argumentos posicionais em tupla
- **kwargs → empacota argumentos nomeados em dicionário

✨ PADRÕES ÚTEIS:
1. Combinação com parâmetros obrigatórios:
   def func(a, b, *args): ...
   
2. Forçar argumentos nomeados após args:
   def func(a, b, *args, c, d): ...

3. Encaminhamento de argumentos:
   def wrapper(*args, **kwargs):
       return outra_funcao(*args, **kwargs)
"""

"""
⚠️ CUIDADOS:
1. Não use *args quando um número fixo de parâmetros for esperado
2. Documente o propósito dos argumentos variáveis
3. Evite funções com assinaturas muito complexas
"""

"""
📚 APRENDIZADOS:
1. Como funciona o empacotamento com *
2. Casos de uso para *args
3. Desempacotamento de iteráveis
4. Boas práticas com argumentos variáveis
"""