"""
🔤 ITERAÇÃO EM STRINGS COM WHILE
--------------------------------
Este código demonstra como percorrer cada caractere de uma string
usando um loop while e constrói uma nova string formatada.
"""

# 📍 String original que será iterada
nome = 'Maria Helena'  # Poderia ser qualquer string iterável

indice = 0          # 🏁 Inicializa o contador de posição
novo_nome = ''      # 🆕 String vazia para construir o resultado

# 🔄 Loop enquanto o índice for menor que o tamanho da string
while indice < len(nome):
    letra = nome[indice]      # 🔍 Pega a letra na posição atual
    novo_nome += f'*{letra}'  # ✨ Adiciona a letra com * antes
    indice += 1               # ➕ Avança para a próxima posição

novo_nome += '*'              # 🏁 Adiciona * final
print(novo_nome)              # 🖨️ Exibe o resultado formatado

"""
💡 ENTENDENDO O CÓDIGO:
1. Inicializamos um índice em 0 (primeira posição)
2. Criamos uma string vazia para acumular o resultado
3. Enquanto o índice for menor que o comprimento da string:
   - Pegamos o caractere na posição atual
   - Adicionamos o caractere precedido por * à nova string
   - Incrementamos o índice
4. Finalmente adicionamos um * no final

📌 RESULTADO ESPERADO:
*M*a*r*i*a* *H*e*l*e*n*a*

🔍 DETALHES IMPORTANTES:
- Strings são sequências imutáveis, mas podemos construir novas
- len(nome) retorna o comprimento da string (12 no caso)
- Acessamos caracteres individualmente com nome[indice]

🆚 ALTERNATIVA COM FOR:
novo_nome = ''
for letra in nome:
    novo_nome += f'*{letra}'
novo_nome += '*'
print(novo_nome)

✨ VERSÃO PYTHÔNICA:
print('*' + '*'.join(nome) + '*')
"""

"""
📚 APRENDIZADOS:
1. Como iterar strings caractere por caractere
2. Construção de novas strings a partir de existentes
3. Controle preciso de loops com while
4. Formatação de strings com f-strings
"""