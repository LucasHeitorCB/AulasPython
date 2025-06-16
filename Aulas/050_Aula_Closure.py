"""
🎭 CLOSURES EM PYTHON: FUNÇÕES QUE RETORNAM FUNÇÕES
---------------------------------------------------
Closure é uma função que:
1. Retorna outra função
2. A função retornada "lembra" do ambiente onde foi criada
3. Mantém acesso às variáveis locais mesmo após o término da execução
"""

def criar_saudacao(saudacao):
    """
    Factory function que gera funções de saudação personalizadas
    
    Args:
        saudacao (str): Tipo de saudação ('Bom dia', 'Boa noite', etc)
        
    Returns:
        function: Função de saudação que recebe um nome
    """
    def saudar(nome):
        """Saudação personalizada que usa o contexto da função externa"""
        return f'{saudacao}, {nome}!'
    return saudar  # 📌 Retorna a função interna (com memória do contexto)

# 🏭 Criando funções especializadas
falar_bom_dia = criar_saudacao('Bom dia')    # 🌅
falar_boa_noite = criar_saudacao('Boa noite') # 🌃

# 🚀 Usando as funções criadas
for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))    # 🖨️ "Bom dia, Maria!", etc
    print(falar_boa_noite(nome))  # 🖨️ "Boa noite, Maria!", etc

"""
💡 COMO FUNCIONA O CLOSURE?
1. criar_saudacao('Bom dia') executa e retorna saudar
2. saudar mantém uma referência ao escopo onde foi criada
3. Por isso lembra do valor do parâmetro saudacao

✨ APLICAÇÕES PRÁTICAS:
1. Factory functions (como no exemplo)
2. Decoradores
3. Callbacks com estado
4. Implementação de estratégias

🛠️ EXEMPLO AVANÇADO (CONTADOR COM CLOSURE):
"""
def contador(inicial=0):
    valor = inicial
    def incrementar():
        nonlocal valor  # Permite modificar a variável do escopo externo
        valor += 1
        return valor
    return incrementar

contador1 = contador(10)
print(contador1())  # 11
print(contador1())  # 12

"""
⚠️ CUIDADOS:
1. Não abuse de closures - podem dificultar a legibilidade
2. Use nonlocal para modificar variáveis do escopo externo
3. Documente sempre o comportamento esperado
"""

"""
📚 APRENDIZADOS:
1. Como closures "lembram" do contexto
2. Padrão factory function
3. Diferença entre global e nonlocal
4. Casos de uso reais
"""