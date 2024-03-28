#Desenvolva um programa que pegue 2 notas de um aluno e calcule a média entre elas

n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))
print("A nota 1 foi: {:2f}".format(n1) + ", a nota 2 foi: {:2f}".format(n2) + ", a média entre elas é: {:2f}".format((n1+n2)/2))