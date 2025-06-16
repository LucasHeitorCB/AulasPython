"""
🌍 ESCOPO DE VARIÁVEIS EM PYTHON
--------------------------------
Escopo define a visibilidade de uma variável no código:
- Global: Acessível em todo o programa
- Local: Acessível apenas dentro da função/classe
"""

# Variável global (escopo do módulo)
x = 1

def escopo():
    # Variável local (sobrescreve a global apenas aqui)
    x = 10  # 🔄 Esta é uma nova variável x, diferente da global

    def outra_funcao():
        # Variável local mais interna
        x = 11  # 📌 Outra variável x diferente
        y = 2   # 📌 Variável local apenas desta função
        print(x, y)  # 🖨️ 11 2 (usa o x local)

    outra_funcao()
    print(x)  # 🖨️ 10 (usa o x da função escopo())

print(x)     # 🖨️ 1 (variável global)
escopo()     # 🖨️ 11 2 (da outra_funcao) e 10 (do escopo)
print(x)     # 🖨️ 1 (global permanece inalterada)

"""
💡 COMO ALTERAR A VARIÁVEL GLOBAL (NÃO RECOMENDADO):
def escopo():
    global x  # 🚨 Aviso: Isso modifica a variável global
    x = 10
"""

"""
📌 REGRAS DE ESCOPO:
1. Variáveis são buscadas nesta ordem:
   - Escopo local → função externa → global → built-ins
2. Atribuição cria variáveis locais por padrão
3. global força uso da variável global

⚠️ PROBLEMAS COM global:
1. Dificulta a depuração
2. Causa efeitos colaterais inesperados
3. Viola o princípio de encapsulamento

✨ ALTERNATIVAS MELHORES:
1. Passar valores como parâmetros
2. Retornar valores das funções
3. Usar classes para estado compartilhado
"""

"""
📚 APRENDIZADOS:
1. Hierarquia de escopos (LEGB rule)
2. Por que evitar modificar escopo global
3. Boas práticas para compartilhamento de estado
4. Diferença entre atribuição e referência
"""