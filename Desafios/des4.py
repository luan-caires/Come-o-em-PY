#Crie um programa que leia um valor em metros e o exiba convertido em centímetros e em milimetros

valor =  float(input("Digite um valor qualquer(em metros): "))
cent = valor * 100
mil = valor * 1000
print("O valor em metros foi de: {},".format(valor) + "a sua conversão para centímetros é de: {:0f} centímetros".format(cent) + " e para milímetros é de: {:0f} milímetros".format(mil))
    