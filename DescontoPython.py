# Script para calcular desconto de 10% em produtos

# Entrada de dados
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))

# Cálculo do desconto
desconto = preco * 0.10  # 10% de desconto
preco_com_desconto = preco - desconto

# Exibição dos resultados
print("\n" + "="*40)
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto (10%): R$ {desconto:.2f}")
print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
print("="*40)
