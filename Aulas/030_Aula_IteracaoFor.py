"""
🔤 ITERAÇÃO EM STRINGS COM FOR
--------------------------------
Este código demonstra como percorrer cada caractere de uma string
usando um loop for e constrói uma nova string formatada com asteriscos.
"""

# 📍 String original que será iterada
texto = 'Python'  # Poderia ser qualquer string iterável

novo_texto = ''      # 🆕 String vazia para construir o resultado

# 🔄 Loop for que itera sobre cada caractere da string
for letra in texto:
    novo_texto += f'*{letra}'  # ✨ Adiciona a letra com * antes
    print(letra)               # 🖨️ Exibe cada letra individualmente

# 🏁 Adiciona * final e exibe o resultado completo
print(novo_texto + '*')  

"""
💡 ENTENDENDO O CÓDIGO:
1. Definimos a string original 'Python'
2. Criamos uma string vazia novo_texto para acumular o resultado
3. Usamos for para iterar cada letra na string original:
   - Adicionamos a letra precedida por * à nova string
   - Imprimimos cada letra individualmente
4. Finalmente adicionamos um * no final e imprimimos o resultado

📌 RESULTADO ESPERADO:
P
y
t
h
o
n
*P*y*t*h*o*n*

🔍 DETALHES IMPORTANTES:
- O loop for é mais pythonico para iterar strings que while
- Strings são iteráveis, então podemos usar for diretamente
- A cada iteração, letra assume o valor do próximo caractere

🆚 COMPARAÇÃO COM WHILE (código anterior):
- Mais simples e legível que a versão com while
- Não precisa controlar manualmente o índice
- Menos propenso a erros (como loops infinitos)

✨ VERSÃO MAIS PYTHÔNICA:
print('\n'.join(texto))  # Para imprimir letras separadas
print('*' + '*'.join(texto) + '*')  # Para o formato com asteriscos
"""

"""
📚 APRENDIZADOS:
1. Como iterar strings caractere por caractere com for
2. Construção de novas strings a partir de existentes
3. Diferenças entre for e while para iteração
4. Métodos mais pythonicos para manipulação de strings
"""