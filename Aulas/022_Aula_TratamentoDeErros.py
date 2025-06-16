"""
🛡️ TRATAMENTO DE ERROS COM TRY/EXCEPT
---------------------------------------
O bloco try/except é usado para lidar com exceções (erros) que podem ocorrer
durante a execução do código, evitando que o programa quebre.

Estrutura básica:
try:
    # Código que pode gerar erro
except:
    # O que fazer se ocorrer erro
"""

# 🔢 Solicitando entrada do usuário
numero_str = input('Vou dobrar o número que vc digitar: ')
# 📌 Captura entrada como string (pode ser qualquer texto)

try:
    # 🎯 Tentativa de conversão e cálculo
    numero_float = float(numero_str)  # 🔄 Converte para float (pode falhar)
    print('FLOAT:', numero_float)  # 🖨️ Mostra a conversão bem-sucedida
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')  
    # 💡 Mostra o dobro formatado com 2 decimais

except:
    # ❌ Se ocorrer qualquer erro no try
    print('Isso não é um número')  # 🚨 Mensagem de erro amigável

"""
💡 ALTERNATIVA COMENTADA:
Usando isdigit() (menos robusta que try/except)
if numero_str.isdigit():  # ✅ Verifica se string contém apenas dígitos
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é um número')

Problemas da abordagem com isdigit():
- Não aceita números negativos
- Não aceita números com ponto decimal
- Menos flexível que try/except
"""

"""
📌 BOAS PRÁTICAS:
1. Especificar o tipo de exceção (except ValueError:)
2. Usar múltiplos except para diferentes erros
3. Incluir mensagens de erro descritivas
4. Usar else (executa se não houver erro) e finally (sempre executa)

Exemplo avançado:
try:
    num = float(input('Digite um número: '))
except ValueError as e:
    print(f'Entrada inválida: {e}')
else:
    print(f'Dobro: {num*2}')
finally:
    print('Processo concluído')
"""