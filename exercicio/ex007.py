#Calcule desconto de 5% de um valor qualquer 

valorInicial = float(input("Digite o preço de um produto: "))
valorDesconto = valorInicial * (5 / 100)
valorFinal = valorInicial - valorDesconto
print("O produto que custava R${} reais, após o desconto de 5% passou a custar R${:.2f} reais".format(valorInicial,valorFinal))