"""
🎯 FUNÇÕES DE ALTA ORDEM E LAMBDA EM PYTHON
-------------------------------------------
Este código demonstra o uso de:
1. Funções que retornam funções (closure)
2. Funções lambda aninhadas
3. Execução genérica de funções com *args
"""

def executa(funcao, *args):
    """Executa uma função com os argumentos fornecidos"""
    return funcao(*args)  # 📌 Desempacota os argumentos na chamada

# 🔄 Exemplo 1: Criação de função multiplicadora via lambda
duplica = executa(
    lambda m: lambda n: n * m,  # 🏭 Função que retorna função
    2  # 🎯 Argumento para o multiplicador
)
print(duplica(2))  # 🖨️ 4 (2 * 2)

# ➕ Exemplo 2: Soma simples com lambda
print(executa(
    lambda x, y: x + y,  # ➕ Função de soma
    2, 3  # 🎯 Argumentos
))  # 🖨️ 5

# 🔢 Exemplo 3: Soma de múltiplos argumentos
print(executa(
    lambda *args: sum(args),  # 🧮 Soma qualquer quantidade de números
    1, 2, 3, 4, 5, 6, 7  # 🎯 Argumentos variáveis
))  # 🖨️ 28

"""
💡 ENTENDENDO O CÓDIGO:

1. A função executa() recebe:
   - Uma função como primeiro argumento
   - Argumentos variáveis (*args) para passar para a função

2. O exemplo mais complexo:
   lambda m: lambda n: n * m
   - É uma função que recebe 'm' e retorna outra função
   - A função retornada recebe 'n' e retorna n * m

3. Uso de *args permite:
   - Receber qualquer número de argumentos
   - Passá-los adiante para a função alvo

📌 VERSÃO ALTERNATIVA SEM LAMBDA:
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
"""

"""
✨ APLICAÇÕES PRÁTICAS:
1. Criação de funções especializadas sob demanda
2. Processamento genérico de dados
3. Implementação de decoradores
4. Cálculos matemáticos dinâmicos

⚠️ CUIDADOS:
1. Lambdas complexas podem reduzir legibilidade
2. *args requer documentação clara
3. Closure mantém referências aos valores externos
"""

"""
📚 APRENDIZADOS:
1. Como funções podem retornar outras funções
2. Uso de lambdas para criar funções rápidas
3. Flexibilidade do *args
4. Diferença entre parâmetros e argumentos
"""