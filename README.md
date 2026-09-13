Codigo:
 
valor_total_compra = float(input("Digite o valor total da compra: "))
 
if valor_total_compra < 200:
valor_com_desconto = valor_total_compra * 0.95
print(f"O valor com desconto é: R\( {valor_com_desconto:.2f}")
 
elif valor_total_compra < 300:
valor_com_desconto = valor_total_compra * 0.90
print(f"O valor com desconto é: R\) {valor_com_desconto:.2f}")
 
else:
valor_com_desconto = valor_total_compra * 0.85
print(f"O valor com desconto é: R$ {valor_com_desconto:.2f}")

Calculadora de Descontos

Programa em Python que calcula o valor final de uma compra com base em faixas de desconto.

Regras de desconto
Compras abaixo de R$ 200: desconto de 5%.
Compras entre R 200 e menos de R 300: desconto de 10%.
Compras de R$ 300 ou mais: desconto de 15%.


Como funciona

O programa recebe o valor da compra usando float(). Em seguida, verifica em qual faixa o valor se encaixa:
if: verifica se a compra é menor que R\( 200.
elif: verifica se a compra é menor que R\) 300.
else: representa todos os valores a partir de R$ 300.

O valor final é calculado multiplicando o preço original por:
0.95 para desconto de 5%;
0.90 para desconto de 10%;
0.85 para desconto de 15%.

A estrutura if, elif e else garante que apenas uma faixa de desconto seja aplicada.
