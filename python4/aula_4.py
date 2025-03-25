salario = float(input("diga seu salario:  "))

if salario <= 1903.08:
    aliquota = 0

elif salario > 1903.08:
    aliquota = 0.075


elif salario > 2826.65:
    aliquota = 0.15

elif salario > 3751.05:
    aliquota = 0.225

else:
    aliquota = 0.275

desconto = salario * aliquota
salario = salario - desconto
print(f'apos desconto de R${desconto:.2f} voce recebera R${salario:.2f}')