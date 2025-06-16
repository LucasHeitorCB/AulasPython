"""
🔄 RETORNO DE VALORES EM FUNÇÕES PYTHON
---------------------------------------
A instrução `return` encerra a função e retorna um valor ao chamador.
Funções sem return explícito retornam `None`.
"""

def soma(x, y):
    """
    Retorna a soma de x e y, exceto quando x > 10.
    
    Args:
        x (int): Primeiro valor
        y (int): Segundo valor
        
    Returns:
        int/list: Soma dos valores ou lista [10, 20] se x > 10
    """
    if x > 10:
        return [10, 20]  # 📌 Retorna lista se condição for verdadeira
    return x + y  # ➕ Retorna a soma dos valores

# 🧪 Testando diferentes casos de retorno
soma1 = soma(2, 2)    # 👉 4 (int)
soma2 = soma(3, 3)     # 👉 6 (int)
resultado = soma(11, 55)  # 👉 [10, 20] (list)

print(soma1)    # 🖨️ 4
print(soma2)    # 🖨️ 6
print(resultado)  # 🖨️ [10, 20]

"""
💡 PRINCÍPIOS IMPORTANTES:
1. Return encerra imediatamente a execução da função
2. Uma função pode ter múltiplos returns com tipos diferentes
3. Sem return → None é retornado automaticamente

✨ BOAS PRÁTICAS:
1. Documente os tipos de retorno na docstring
2. Prefira retornar sempre o mesmo tipo quando possível
3. Use type hints para esclarecer retornos:
   def soma(x: int, y: int) -> int | list: ...
"""

"""
⚠️ CUIDADO COM:
1. Retornos inconsistentes (dificultam o uso da função)
2. Efeitos colaterais (modificar variáveis globais)
3. Funções muito longas com múltiplos returns
"""

"""
📚 APRENDIZADOS:
1. Como controlar o fluxo com return
2. Tipos múltiplos de retorno
3. Documentação de funções
4. Padrões de retorno consistentes
"""