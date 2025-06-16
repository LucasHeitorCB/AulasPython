"""
🔄 CONTROLE DE LOOPS COM WHILE, CONTINUE E BREAK
------------------------------------------------
Este código demonstra o uso de:
- while: repete enquanto a condição for verdadeira
- continue: pula para a próxima iteração
- break: interrompe completamente o loop
"""

contador = 0  # 🏁 Inicializa o contador

while contador <= 100:  # 🔄 Repete até 100
    contador += 1  # ➕ Incrementa o contador a cada iteração

    # 🚫 Pula o número 6
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue  # ⏭️ Pula para próxima iteração

    # 🚫 Pula números entre 10 e 27 (inclusive)
    if 10 <= contador <= 27:  # 🆕 Sintaxe mais limpa
        print(f'Não vou mostrar o {contador}')  # 🆕 f-string
        continue

    print(contador)  # 🖨️ Mostra os números não pulados

    # 🛑 Interrompe ao chegar no 40
    if contador == 40:
        break  # ✋ Sai completamente do loop

print('Acabou')  # 🏁 Mensagem final

"""
📊 FLUXO DO PROGRAMA:
1. Conta de 1 a 100 (teoricamente)
2. Pula completamente o número 6
3. Pula todos números entre 10 e 27
4. Para completamente no número 40
5. Mostra todos outros números

⚠️ CUIDADO COM:
1. Loops infinitos - sempre garantir condição de saída
2. Uso excessivo de continue/break pode dificultar a leitura
3. Esquecer de incrementar o contador (causaria loop infinito)

🔁 ALTERNATIVA COM FOR:
for contador in range(1, 101):
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue
    # ... resto similar
    if contador == 40:
        break
"""

"""
📌 BOAS PRÁTICAS:
1. Use while quando não souber o número exato de iterações
2. Prefira for quando souber o limite de repetições
3. Evite muitos níveis de aninhamento com continue/break
4. Nomeie variáveis de controle de forma significativa
"""