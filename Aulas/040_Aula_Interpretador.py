"""
🐍 INTERPRETADOR PYTHON: USOS AVANÇADOS
---------------------------------------
O interpretador Python oferece várias opções de execução:

1. Execução direta:
   python mod.py       → Roda o script mod.py

2. Modo unbuffered (útil para logs em tempo real):
   python -u mod.py    → Desativa buffer de saída

3. Execução como módulo (import path correto):
   python -m mod       → Roda __main__ do módulo

4. Comando direto:
   python -c 'print("Olá")' → Executa código inline

5. Modo interativo pós-execucão:
   python -i mod.py    → Mantém terminal aberto após rodar
"""

"""
📜 THE ZEN OF PYTHON (POR TIM PETERS)
-------------------------------------
Princípios filosóficos da linguagem Python.
Acesse com: import this

1. Bonito é melhor que feio.
2. Explícito é melhor que implícito.
3. Simples é melhor que complexo.
4. Complexo é melhor que complicado.
5. Plano é melhor que aglomerado.
6. Esparso é melhor que denso.
7. Legibilidade conta.
8. Casos especiais não são especiais o bastante para quebrar as regras.
9. Embora a praticidade vença a pureza.
10. Erros nunca devem passar silenciosamente.
11. A menos que sejam explicitamente silenciados.
12. Diante da ambiguidade, recuse a tentação de adivinhar.
13. Deve haver um -- e só um -- modo óbvio para fazer algo.
14. Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
15. Agora é melhor que nunca.
16. Embora nunca frequentemente seja melhor que *exatamente* agora.
17. Se a implementação é difícil de explicar, é uma má ideia.
18. Se a implementação é fácil de explicar, pode ser uma boa ideia.
19. Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""

"""
💡 COMO APLICAR NA PRÁTICA:
1. Prefira código legível a "esperto"
2. Trate erros explicitamente (try/except)
3. Mantenha funções simples e especializadas
4. Use namespaces (módulos, classes) para organização
5. Documente decisões complexas

🛠️ EXEMPLO DE BOAS PRÁTICAS:
"""
# Ruim (implícito, difícil de ler)
x = [i for i in range(10) if i%2==0]

# Bom (explícito, legível)
def get_even_numbers(max_num):
    """Retorna lista de números pares até max_num"""
    even_numbers = []
    for num in range(max_num):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

"""
🔍 PARA SABER MAIS:
- python --help (todas opções)
- PEP 20 (The Zen of Python)
- Documentação: python.org/doc/
"""