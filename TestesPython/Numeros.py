salario = input("Salario: ")
comissao = input("Percentual da comissão: ")

valorSalario = float(salario)
valorComissao = int(comissao)
valorComissao = (valorSalario * valorComissao)/100

totalSalario = valorSalario + valorComissao

print("O total do salario é: %.2f" %totalSalario)
print(valorComissao)