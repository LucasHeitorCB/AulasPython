"""
🎯 VALORES PADRÃO PARA PARÂMETROS EM FUNÇÕES
--------------------------------------------
Parâmetros com valores padrão tornam argumentos opcionais.
Se não fornecidos, usam o valor definido na função.
"""

def soma(x, y, z=None):
    """
    Calcula a soma de 2 ou 3 valores.
    
    Args:
        x (int/float): Primeiro valor obrigatório
        y (int/float): Segundo valor obrigatório
        z (int/float, optional): Terceiro valor opcional. Defaults to None.
    """
    if z is not None:
        print(f'{x=} {y=} {z=} | Soma =', x + y + z)
    else:
        print(f'{x=} {y=} | Soma =', x + y)

# 🧪 Testando diferentes combinações de argumentos
soma(1, 2)          # 👉 Usa valor padrão z=None
soma(3, 5)          # 👉 Usa valor padrão z=None  
soma(100, 200)      # 👉 Usa valor padrão z=None
soma(7, 9, 0)       # 👉 Fornece todos os valores
soma(y=9, z=0, x=7) # 👉 Argumentos nomeados

"""
💡 PRINCÍPIOS IMPORTANTES:
1. Parâmetros com valor padrão devem vir DEPOIS dos obrigatórios
2. None é comum como valor padrão para mutáveis
3. Evite usar listas/dicionários como valores padrão (são mutáveis)

⚠️ EXEMPLO PERIGOSO:
def func(items=[]):  # ❌ Mesma lista compartilhada!
    items.append(1)
    print(items)

func()  # [1]
func()  # [1, 1] (não reinicia)
"""

"""
✨ BOAS PRÁTICAS:
1. Use type hints para documentação:
   def soma(x: int, y: int, z: int | None = None) -> None:
   
2. Documente comportamentos com docstrings
3. Para valores mutáveis, use None e crie dentro da função
"""

"""
📚 APRENDIZADOS:
1. Como definir parâmetros opcionais
2. Uso adequado de None como padrão
3. Ordem correta dos parâmetros
4. Armadilhas com valores mutáveis
"""