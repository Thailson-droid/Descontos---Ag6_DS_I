#Thailson_Ag6_DS_I
valor_total_compra = float(input("Digite o valor total da compra: "))

if valor_total_compra < 200:
    valor_com_desconto = valor_total_compra * 0.95
    print(f"O valor com desconto é: R$ {valor_com_desconto:.2f}")
if valor_total_compra >= 200 and valor_total_compra < 300:
    
    valor_com_desconto = valor_total_compra * 0.90
    print(f"O valor com desconto é: R$ {valor_com_desconto:.2f}")

if valor_total_compra >= 300:
    valor_com_desconto = valor_total_compra * 0.85
    print(f"O valor com desconto é: R$ {valor_com_desconto:.2f}")
    
