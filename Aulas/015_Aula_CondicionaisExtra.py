# =============================================
# 📌 CÓDIGO REESCRITO: TESTANDO MÚLTIPLAS CONDIÇÕES
# =============================================

# 🔄 Variáveis renomeadas para maior clareza
condicao_vermelha = False   # 🔴 Condição A (vermelho)
condicao_verde = True       # 🟢 Condição B (verde) 
condicao_azul = False       # 🔵 Condição C (azul)
condicao_amarela = True     # 🟡 Condição D (amarelo)

# 🔍 Estrutura condicional principal
if condicao_vermelha:  # ❌ Primeira verificação (Falsa)
    print('Condição Vermelha foi ativada 🔴')
elif condicao_verde:  # ✅ Primeira condição verdadeira encontrada
    print('Condição Verde foi ativada 🟢')  # 🎯 Será executado
elif condicao_azul:  # ⏭️ Não será verificado (já encontramos uma condição True)
    print('Condição Azul foi ativada 🔵')
elif condicao_amarela:  # ⏭️ Também não será verificado
    print('Condição Amarela foi ativada 🟡')
else:  # ⏹️ Bloco opcional para quando nenhuma condição é atendida
    print('Nenhuma condição foi atendida. ❌')

# 💡 Exemplo simples de condicional independente
if 5 > 3:  # 🧠 Expressão sempre verdadeira
    print('A verificação é verdadeira! ✅')  # ✔️ Sempre será executado

# 🌐 Mensagem fora de qualquer bloco condicional
print('Fora do bloco de decisão.')  # 🏁 Execução final

# =============================================
# 📝 EXPLICAÇÃO DOS CONCEITOS:
# =============================================
# O Python avalia as condições na ordem até encontrar a primeira verdadeira:
# 1. O 'elif' só é verificado se todos os 'if/elif' anteriores forem falsos
# 2. Quando um 'elif' é verdadeiro, os demais são ignorados
# 3. O 'else' captura todos os casos restantes
# 4. Cada 'if' independente é avaliado separadamente

# ⚠️ Curiosidade: Se usássemos vários 'if' em vez de 'elif',
# todas as condições verdadeiras seriam executadas!
