algo = input("Digite alguma coisa: ")
print("O tipo primitivo desse valor é:",type(algo))
print("Só tem espaços??  ", algo.isspace())
print("Só tem números?? ", algo.isnumeric())
print("É alfabético??", algo.isalpha())
print("É alfanumérico??", algo.isalnum())
print("Está em maiúsculas??", algo.isupper())
print("Está em minúsculas??", algo.islower())
print("Está capitalizado??", algo.istitle()) 