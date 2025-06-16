"""
📚 TIPOS IMUTÁVEIS EM PYTHON
-----------------------------
Tipos imutáveis são aqueles que não podem ser alterados após sua criação.
Os principais tipos imutáveis são:
- str (texto)
- int (números inteiros)
- float (números decimais)
- bool (True/False)

Quando "modificamos" uma string, na verdade criamos uma nova string.
"""

string = '1000'  # 🏷️ Criando uma string (tipo imutável)

# 🧪 Tentativa de modificação (comentada)
# outra_variavel = f'{string[:3]}ABC{string[4:]}'  
# 📌 Isso criaria uma NOVA string combinando partes
# string original permanece inalterada

# 🖨️ Resultados (comentados)
# print(string)          # '1000' (original intacta)
# print(outra_variavel)  # '100ABC' (nova string)

# 🔢 Preenchimento com zeros
print(string.zfill(10))  
# 📌 zfill() preenche com zeros à esquerda
# 📌 Retorna NOVA string: '0000001000'
# 📌 String original permanece '1000'

"""
💡 CARACTERÍSTICAS DA IMUTABILIDADE:
1. Segurança: dados não são alterados acidentalmente
2. Eficiência: permite otimizações pelo Python
3. Previsibilidade: comportamento consistente

🔍 MÉTODOS COMUNS DE STRING QUE RETORNAM NOVOS VALORES:
- .upper()/.lower() - maiúsculas/minúsculas
- .strip() - remove espaços
- .replace() - substitui partes
- .zfill() - preenchimento com zeros

⚠️ IMPORTANTE:
Todos esses métodos RETORNAM novas strings, 
não modificam a original.
"""

# 🆚 DEMONSTRAÇÃO DE IMUTABILIDADE
print(f"String original: {string} (id: {id(string)})")
nova_string = string.zfill(10)
print(f"Nova string: {nova_string} (id: {id(nova_string)})")
print(f"Original após zfill(): {string} (id: {id(string)})")

"""
📌 SAÍDA ESPERADA:
0000001000
String original: 1000 (id: 140...)
Nova string: 0000001000 (id: 140... diferente)
Original após zfill(): 1000 (id: 140... mesmo)
"""