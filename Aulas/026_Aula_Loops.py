"""
🔄 ESTRUTURA DE REPETIÇÃO WHILE EM PYTHON
-----------------------------------------
O while executa um bloco de código repetidamente ENQUANTO 
uma condição for verdadeira.

Cuidado com loops infinitos! Sempre garanta uma condição de saída.
"""

condicao = True  # 🏁 Flag para controlar o loop

while condicao:  # 🔄 Repete enquanto condicao for True
    # 👤 Solicita entrada do usuário
    nome = input('Qual o seu nome: ')
    
    # 🖨️ Exibe o nome digitado
    print(f'Seu nome é {nome}')
    
    # 🚪 Condição de saída do loop
    if nome == 'sair':
        break  # ✋ Interrompe imediatamente o loop

print('Acabou')  # 🏁 Mensagem final após sair do loop

"""
💡 APRIMORAMENTOS SUGERIDOS:

1. Adicionar validação de entrada:
while True:
    nome = input('Digite seu nome (ou "sair" para terminar): ').strip()
    if not nome:  # Se string vazia
        print('Por favor digite um nome válido')
        continue
    if nome.lower() == 'sair':
        break

2. Contador de iterações:
contador = 0
while contador < 5:
    print(f'Iteração {contador}')
    contador += 1

3. Loop com else:
while condicao:
    # código
else:
    print('Loop terminado naturalmente')
"""

"""
⚠️ CUIDADO COM LOOPS INFINITOS:
Exemplo perigoso:
while True:
    print('Loop infinito!')

Sempre garanta uma condição de saída:
- break para saída imediata
- condição de controle no while
- timeout para operações demoradas
"""

"""
📌 BOAS PRÁTICAS:
1. Nomeie variáveis de controle claramente
2. Documente a condição de saída
3. Evite loops muito longos
4. Prefira for quando souber o número de iterações
5. Use break e continue com moderação
"""