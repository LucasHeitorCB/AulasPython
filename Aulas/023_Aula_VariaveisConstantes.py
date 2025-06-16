"""
🚦 SIMULAÇÃO DE RADAR VIÁRIO (BOAS PRÁTICAS)
--------------------------------------------
Este código demonstra o uso de constantes e como evitar condições complexas.
Constantes em Python são convencionadas com UPPER_CASE, indicando que não devem ser alteradas.
"""

# 🚗 DADOS DO VEÍCULO
velocidade = 61        # km/h - velocidade atual do carro
local_carro = 100      # km - posição na estrada

# 📡 CONFIGURAÇÕES DO RADAR 1 (constantes)
RADAR_1 = 60           # km/h - velocidade máxima permitida
LOCAL_1 = 100          # km - localização do radar na estrada
RADAR_RANGE = 1        # km - alcance de detecção do radar

# 🧠 CÁLCULOS SEMÂNTICOS (melhor legibilidade)
carro_acima_velocidade = velocidade > RADAR_1
carro_na_area_radar = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_sera_multado = carro_na_area_radar and carro_acima_velocidade

# 🚨 LÓGICA DE NOTIFICAÇÕES
if carro_acima_velocidade:
    print('⚠️ Velocidade do carro excedeu o limite do radar 1')

if carro_na_area_radar:
    print('📡 Carro passou na área de cobertura do radar 1')

if carro_sera_multado:
    print('💸 Carro multado no radar 1!')

"""
📌 MELHORIAS IMPLEMENTADAS:
1. Nomes de variáveis mais descritivos
2. Eliminação da contrabarra (\) usando comparação encadeada
3. Separação clara entre configurações, cálculos e lógica
4. Adição de emojis para melhor visualização
5. Comentários explicativos para cada seção

💡 DICAS DE BOAS PRÁTICAS:
- Use constantes para valores fixos que têm significado especial
- Evite condições complexas - divida em variáveis intermediárias
- Prefira nomes que expliquem o "porquê" ao invés do "como"
- Organize seu código em "blocos lógicos" (dados, configurações, processamento, saída)

🆚 VERSÃO ANTIGA COMENTADA:
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

# Código menos legível com condições complexas
if velocidade > RADAR_1 and \
   (local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)):
    print('carro multado')
"""