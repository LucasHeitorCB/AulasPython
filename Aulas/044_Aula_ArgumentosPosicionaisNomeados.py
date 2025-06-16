"""
🎯 ARGUMENTOS NOMEADOS VS POSICIONAIS EM PYTHON
-----------------------------------------------
Em funções Python, argumentos podem ser passados de duas formas:
1. Posicional (não nomeado): ordem determina o parâmetro
2. Nomeado (keyword argument): explicita o nome do parâmetro
"""

def soma(x, y, z):
    """Demonstra diferença entre argumentos nomeados e posicionais"""
    # 📌 f-strings com = mostram nome e valor da variável
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)

# 🧪 Chamadas com diferentes combinações de argumentos
soma(1, 2, 3)       # 👈 Todos posicionais
soma(1, y=2, z=5)   # 👈 Misto (posicional + nomeados)

# 🖨️ Exemplo com print (que usa argumentos nomeados)
print(1, 2, 3, sep='-')  # sep é argumento nomeado

"""
💡 REGRAS IMPORTANTES:
1. Argumentos posicionais devem vir antes dos nomeados
   soma(x=1, 2, 3) → Inválido!
   
2. Parâmetros após * devem ser nomeados
   def func(a, b, *, c, d): ...

3. Não pode repetir parâmetros
   soma(1, x=2, z=3) → Erro (x duplicado)

✨ BOAS PRÁTICAS:
1. Use nomeados para parâmetros booleanos/flags
2. Prefira nomeados quando houver muitos parâmetros
3. Documente parâmetros opcionais com valores padrão
"""

"""
📌 EXEMPLO AVANÇADO (PARÂMETROS SOMENTE NOMEADOS):
"""
def configurar(*, host, port, timeout=10):
    print(f'Config: {host}:{port} (timeout={timeout})')

# configurar('localhost', 8080)  # Erro!
configurar(host='localhost', port=8080)  # OK

"""
⚠️ CUIDADO COM:
1. Ordem incorreta de parâmetros
2. Nomes de parâmetros errados
3. Argumentos obrigatórios não fornecidos
"""

"""
📚 APRENDIZADOS:
1. Diferença entre argumentos posicionais e nomeados
2. Regras de combinação de argumentos
3. Quando usar cada abordagem
4. Parâmetros obrigatórios vs opcionais
"""