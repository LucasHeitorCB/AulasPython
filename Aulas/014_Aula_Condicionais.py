# =============================================
# 📌 CÓDIGO REESCRITO: CONDICIONAIS IF/ELIF/ELSE
# =============================================

# 🔄 Renomeando variáveis para maior clareza e usando emojis para organização visual

# 🎤 Solicitação de entrada do usuário
opcao_usuario = input('Deseja "ligar" ou "desligar" o sistema? ')

# 🔍 Verificação da opção escolhida com estrutura condicional
if opcao_usuario.lower() == 'ligar':  # 📥 .lower() para aceitar maiúsculas/minúsculas
    print('Sistema iniciado com sucesso! 🚀')  # ✅ Mensagem positiva
    print('Executando operações...')  # ⚙️ Feedback adicional
elif opcao_usuario.lower() == 'desligar':  # 🔄 Segunda condição
    print('Sistema finalizado. 🛑')  # ⏹️ Mensagem de encerramento
else:  # 🚨 Caso padrão para entradas inválidas
    print('Comando inválido. Digite "ligar" ou "desligar". ⚠️')  # ❌ Mensagem de erro

# 🌐� Linha executada independentemente das condições (fora do bloco if/elif/else)
print('Fim do programa.')  # 🏁 Mensagem final

# =============================================
# 📝 EXPLICAÇÃO DOS CONCEITOS:
# =============================================
# Estruturas condicionais permitem executar diferentes blocos de código 
# baseado em condições. Neste caso:
# - if: primeira condição verificada
# - elif: condições subsequentes (pode ter vários)
# - else: executa quando nenhuma condição anterior foi atendida
# O .lower() padroniza a entrada para evitar erros com maiúsculas/minúsculas
