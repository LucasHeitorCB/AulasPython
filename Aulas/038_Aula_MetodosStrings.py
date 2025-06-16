"""
✂️ DIVIDINDO E JUNTANDO STRINGS EM PYTHON
-----------------------------------------
split() e join() são métodos essenciais para manipulação de strings:
- split(): divide uma string em partes, retornando uma lista
- join(): une elementos de uma lista em uma string única
"""

# 📍 String com espaços extras para demonstração
frase = '   Olha só que   , coisa interessante          '

# 1️⃣ DIVIDINDO A STRING
lista_frases_cruas = frase.split(',')  # ✂️ Divide no caractere ','
# Resultado: ['   Olha só que   ', ' coisa interessante          ']

# 2️⃣ LIMPANDO OS ELEMENTOS
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())  # 🧹 Remove espaços extras
# Resultado: ['Olha só que', 'coisa interessante']

# 3️⃣ JUNTANDO NOVAMENTE
frases_unidas = ', '.join(lista_frases)  # 🧵 Une com ', ' entre elementos
print(frases_unidas)  # 🖨️ Saída: "Olha só que, coisa interessante"

"""
💡 VERSÃO PYTHÔNICA (LIST COMPREHENSION):
lista_frases = [frase.strip() for frase in frase.split(',')]
"""

"""
📌 PARÂMETROS IMPORTANTES:
- split(sep=None, maxsplit=-1):
  sep: separador (padrão é whitespace)
  maxsplit: número máximo de divisões

- join(iterable): recebe qualquer iterável de strings

✨ EXEMPLOS ADICIONAIS:
"""
# Dividindo por espaços (padrão)
palavras = 'Python é incrível'.split()  # ['Python', 'é', 'incrível']

# Unindo com diferentes separadores
caminho = '/'.join(['usr', 'local', 'bin'])  # 'usr/local/bin'

"""
⚠️ CUIDADOS:
1. join() só funciona com strings - converter números primeiro
2. split() sem argumentos remove todos os whitespaces consecutivos
3. Strings vazias geram listas vazias com split()

🔍 DICA AVANÇADA:
Para textos complexos, considere:
- re.split() para expressões regulares
- StringIO para manipulação em memória
"""

"""
📚 APRENDIZADOS:
1. Como dividir strings em partes úteis
2. Técnicas para limpar dados textuais
3. Formas eficientes de juntar strings
4. Padrões comuns de manipulação de texto
"""