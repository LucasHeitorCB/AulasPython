# 🔁 Conversão de tipos (typecasting / coerção)
# str, int, float, bool → são tipos primitivos e imutáveis

print(int("7") + 3, type(int("7")))        # 🔢 converte string para inteiro e soma
print(type(float("5.5") + 2.5))            # 🌊 converte string p/ float e soma
print(bool("texto"))                       # ✅ qualquer string não vazia vira True
print("ID:" + str(99))                     # 🧵 concatena string com número convertido
