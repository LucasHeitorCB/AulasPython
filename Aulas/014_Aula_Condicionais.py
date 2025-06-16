# 🧭 Pede ao usuário uma escolha
acao = input('Deseja "ligar" ou "desligar" o sistema? ')

# ✅ Verifica a ação escolhida
if acao == 'ligar':
    print('Sistema iniciado com sucesso! 🚀')
    print('Executando operações...')
elif acao == 'desligar':
    print('Sistema finalizado. 🛑')
else:
    print('Comando inválido. Digite "ligar" ou "desligar". ⚠️')

# 🔚 Esse print está fora dos blocos condicionais
print('Fim do programa.')
