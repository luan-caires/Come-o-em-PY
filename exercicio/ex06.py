#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos Dólares ela pode comprar . Considere o Dólar = 3.27
import numpy
real = float(input("Informe quanto você tem na carteira: R$ "))
dolar = real / 3.27
print("Com R${} reais, você consegue comprar US${:.2f} dólar".format(real, dolar))