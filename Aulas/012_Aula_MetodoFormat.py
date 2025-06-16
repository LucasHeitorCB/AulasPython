x = 'XXXXX'
y = 'YYYYYY'
z = 3.14159

# 🧩 Criando uma string com placeholders nomeados
frase = 'y={valor_y} x={valor_x} x={valor_x} z={valor_z:.2f}'

# 🎯 Usando .format() para substituir os placeholders
resultado = frase.format(
    valor_x=x, valor_y=y, valor_z=z
)

print(resultado)
