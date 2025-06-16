"""
🔢 ITERAÇÃO COM FOR E RANGE EM PYTHON
-------------------------------------
A função range() gera uma sequência numérica e é frequentemente usada com for.
Sintaxe: range(start, stop, step)
- start: início (inclusivo, padrão=0)
- stop: fim (exclusivo, obrigatório)
- step: passo/incremento (padrão=1)
"""

# 📊 Gerando uma sequência de 0 a 100 pulando de 8 em 8
numeros = range(0, 100, 8)  # 0, 8, 16, 24,..., 96

# 🔄 Iterando sobre cada número da sequência
for numero in numeros:
    print(numero)  # 🖨️ Imprime cada número da sequência

"""
💡 ENTENDENDO MELHOR:
1. range(0, 100, 8) gera: 0, 8, 16, 24,..., 96
   - Para em 96 porque 104 já seria >= 100 (stop)
2. O objeto range é eficiente em memória - não armazena todos valores
3. Podemos converter para lista: list(numeros)

📌 EXEMPLOS ADICIONAIS:
- range(10) → 0 a 9
- range(5, 10) → 5 a 9
- range(0, 10, 2) → 0, 2, 4, 6, 8

🆚 VERSÃO ALTERNATIVA:
for numero in range(0, 100, 8):
    print(numero)

✨ USOS COMUNS:
1. Loops com número controlado de repetições
2. Gerar índices para acessar listas
3. Criar sequências numéricas específicas

🔍 CURIOSIDADE:
Em Python 2, range() gerava uma lista real.
Em Python 3, range() é um gerador mais eficiente.
"""

"""
📚 APRENDIZADOS:
1. Como usar range() para gerar sequências
2. Controle preciso de loops com for
3. Eficiência de memória do range
4. Padrão start-stop-step
"""