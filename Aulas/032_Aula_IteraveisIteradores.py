"""
🔄 ENTENDENDO ITERÁVEIS E ITERADORES EM PYTHON
---------------------------------------------
Em Python, iteráveis são objetos que podem ser percorridos (como strings, listas, ranges),
enquanto iteradores são os objetos que realizam a iteração de fato.

Principais conceitos:
- Iterável: objeto com método __iter__() que retorna um iterador
- Iterador: objeto com método __next__() que retorna o próximo item
- for internamente usa iter() e next() até StopIteration
"""

texto = 'Luiz'  # 📍 String é um objeto iterável

# 🧠 Versão explícita usando iter() e next() (comentada)
# iterador = iter(texto)  # 📦 Cria um iterador a partir do iterável
# 
# while True:
#     try:
#         letra = next(iterador)  # 🎯 Pega o próximo item
#         print(letra)
#     except StopIteration:  # 🛑 Quando não há mais itens
#         break

# 🔄 Versão simplificada com for (equivalente à versão acima)
for letra in texto:
    print(letra)  # 🖨️ Imprime cada caractere

"""
💡 COMO O FOR FUNCIONA POR BAIIXO DOS PANOS:
1. Chama iter() no objeto iterável para obter um iterador
2. Chama next() repetidamente no iterador
3. Captura StopIteration para encerrar o loop

📌 DIFERENÇA ENTRE ITERÁVEL E ITERADOR:
- Iterável: contém os dados (string, lista, tupla, dicionário, etc)
- Iterador: mantém o estado da iteração (posição atual)

🔍 PODEMOS VERIFICAR:
print(hasattr(texto, '__iter__'))  # True - é iterável
print(hasattr(texto, '__next__'))  # False - não é iterador
print(hasattr(iter(texto), '__next__'))  # True - é iterador

✨ OUTROS EXEMPLOS DE ITERÁVEIS:
- listas: [1, 2, 3]
- tuplas: (1, 2, 3)
- dicionários: {'a': 1, 'b': 2}
- arquivos: open('arquivo.txt')
"""

"""
📚 APRENDIZADOS:
1. Diferença entre iteráveis e iteradores
2. Como o for funciona internamente
3. Uso de iter() e next()
4. Tratamento de StopIteration
5. Verificação de capacidades de iteração
"""