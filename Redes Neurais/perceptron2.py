# importa a biblioteca numpy e utiliza np para ser o nome quando incrementada 
import numpy as np

entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def Soma(e,p):
    return e.dot(p)
#dot = dot product / produto escalar: Faz a soma da multiplicação das entradas pelos pesos
s= Soma(entradas,pesos)
print(s)
def StepFunction(soma):
    if(soma>=1):
        return 1
    return 0
r = StepFunction(s)
print(r)