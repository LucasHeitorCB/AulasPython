"""
🌟 FUNÇÕES DE PRIMEIRA CLASSE E HIGHER-ORDER FUNCTIONS
---------------------------------------------------
Em Python, funções são cidadãos de primeira classe (first-class citizens), 
o que significa que podem ser:
1. Atribuídas a variáveis
2. Passadas como argumentos
3. Retornadas de outras funções

Higher-order functions são funções que:
- Recebem outras funções como argumentos, e/ou
- Retornam funções como resultado
"""

def saudacao(msg, nome):
    """Retorna uma mensagem de saudação formatada"""
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    """
    Executa uma função com os argumentos fornecidos
    
    Args:
        funcao (function): Função a ser executada
        *args: Argumentos posicionais para a função
        
    Returns:
        Qualquer: Resultado da função executada
    """
    return funcao(*args)  # 📌 Chama a função recebida com os argumentos

# 🚀 Chamando executa() com diferentes argumentos
print(executa(saudacao, 'Bom dia', 'Luiz'))  # 🖨️ "Bom dia, Luiz!"
print(executa(saudacao, 'Boa noite', 'Maria'))  # 🖨️ "Boa noite, Maria!"

"""
💡 EXEMPLOS ADICIONAIS:
"""
# 1. Atribuindo função a variável
saudar = saudacao
print(saudar('Olá', 'João'))  # 🖨️ "Olá, João!"

# 2. Função que retorna função
def criar_saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}!'
    return saudar

boa_tarde = criar_saudacao('Boa tarde')
print(boa_tarde('Carlos'))  # 🖨️ "Boa tarde, Carlos!"

"""
📌 ONDE ISSO É USADO?
1. Funções map(), filter(), reduce()
2. Decoradores (@decorator)
3. Callbacks em programação assíncrona
4. Estratégia pattern em OOP

✨ BOAS PRÁTICAS:
1. Documente sempre o tipo esperado para funções callback
2. Use type hints para maior clareza:
   def executa(funcao: Callable[..., Any], *args) -> Any:
3. Mantenha as funções pequenas e especializadas
"""

"""
📚 APRENDIZADOS:
1. Conceito de first-class functions
2. Como criar higher-order functions
3. Aplicações práticas
4. Padrões avançados com funções
"""