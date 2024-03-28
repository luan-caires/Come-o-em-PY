#Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada
import math

num = int(input("Informe um número inteiro qualquer: "))
dobro =  num * 2
triplo = num * 3
raiz = math.sqrt(num)

print("O número escolhido foi: {},".format(num) + " o dobro dele é: {},".format(dobro) + " o triplo dele é: {},".format(triplo) + " a raiz quadrada dele é: {}".format(raiz))