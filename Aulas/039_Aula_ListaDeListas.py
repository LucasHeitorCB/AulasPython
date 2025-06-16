"""
📚 LISTAS DE LISTAS E ÍNDICES EM PYTHON
---------------------------------------
Estruturas multidimensionais permitem organizar dados complexos.
Cada lista interna pode ser acessada através de índices consecutivos.
"""

# 🏫 Exemplo: Lista de salas de aula com alunos
salas = [
    # 0        1
    ['Maria', 'Helena'],    # Sala 0 (índice 0)
    # 0
    ['Elaine'],             # Sala 1 (índice 1)
    # 0       1        2
    ['Luiz', 'João', 'Eduarda']  # Sala 2 (índice 2)
]

"""
🔍 ACESSANDO ELEMENTOS:
print(salas[1][0])   # 'Elaine' (sala 1, aluno 0)
print(salas[0][1])   # 'Helena' (sala 0, aluno 1)
print(salas[2][2])   # 'Eduarda' (sala 2, aluno 2)

❌ ERRO COMUM:
print(salas[2][3][3])  # IndexError (não existe aluno 3 na sala 2)
"""

# 🔄 Iterando pelas salas e alunos
for indice_sala, sala in enumerate(salas):
    print(f'\n🏠 Sala {indice_sala}: {sala}')
    for indice_aluno, aluno in enumerate(sala):
        print(f'  👶 Aluno {indice_aluno}: {aluno}')

"""
💡 TÉCNICAS AVANÇADAS:
1. Desempacotamento:
for sala, *alunos in salas:
    print(f'Sala com {len(alunos)} alunos')

2. List Comprehension:
todos_alunos = [aluno for sala in salas for aluno in sala]

3. Acesso seguro:
ultimo_aluno = salas[-1][-1] if salas else None
"""

"""
📌 CASOS DE USO COMUNS:
- Matrizes e grids
- Dados tabulares antes de usar pandas
- Organização hierárquica de informações
- Sistemas de coordenadas
"""

"""
⚠️ CUIDADOS:
1. Índices inválidos causam IndexError
2. Listas internas podem ter tamanhos diferentes
3. Mutabilidade requer atenção em cópias
"""

"""
📚 APRENDIZADOS:
1. Acesso multidimensional com [i][j]
2. Iteração aninhada com for
3. Técnicas para manipulação segura
4. Padrões comuns de aplicação
"""