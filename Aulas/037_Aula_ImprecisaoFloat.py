"""
🔄 ENTENDENDO A IMPRECISÃO DE PONTO FLUTUANTE
--------------------------------------------
Números de ponto flutuante (float) em Python seguem o padrão IEEE 754,
o que pode causar pequenas imprecisões em cálculos. O módulo decimal
oferece uma alternativa mais precisa para operações críticas.
"""

import decimal  # 📦 Módulo para cálculos decimais precisos

# 🎯 Criando números decimais de alta precisão
numero_1 = decimal.Decimal('0.1')  # 🏷️ Usando string para precisão absoluta
numero_2 = decimal.Decimal('0.7')  # 🔢 Evitando problemas de representação binária

# ➕ Operação precisa
numero_3 = numero_1 + numero_2  # 💯 Resultado exato: 0.8
print(numero_3)  # 🖨️ Saída: 0.8 (ao invés de 0.7999999999999999 com float comum)

# 📊 Formatação de saída
print(f'{numero_3:.2f}')  # 🎨 Formatação com f-string: "0.80"
print(round(numero_3, 2))  # 🔄 Arredondamento: Decimal('0.80')

"""
💡 POR QUE USAR DECIMAL?
1. Precisão exata em cálculos financeiros
2. Controle sobre arredondamentos e casas decimais
3. Comportamento consistente em todas as plataformas

⚠️ PROBLEMA COM FLOAT TRADICIONAL:
print(0.1 + 0.7) → 0.7999999999999999 (imprecisão típica)

🔍 AJUSTES NO MÓDULO DECIMAL:
"""
# Configurando precisão global
decimal.getcontext().prec = 4  # 4 dígitos significativos

# Exemplo com arredondamento controlado
resultado = decimal.Decimal('1') / decimal.Decimal('7')
print(resultado)  # 0.1429 (com precisão de 4 dígitos)

"""
📌 QUANDO USAR:
- Sistemas bancários/financeiros
- Cálculos científicos que exigem precisão
- Qualquer aplicação onde erros de arredondamento são inaceitáveis

🚫 QUANDO NÃO USAR:
- Cálculos de alto desempenho (Decimal é mais lento)
- Aplicações que toleram pequenos erros de arredondamento

✨ ALTERNATIVAS:
- math.isclose() para comparações seguras com float
- fractions para representações fracionárias exatas
"""

"""
📚 APRENDIZADOS:
1. Entender a limitação inerente aos floats binários
2. Usar decimal para cálculos precisos
3. Controlar precisão e arredondamento
4. Escolher a ferramenta certa para cada cenário
"""