from funcoes import *

objeto=input("digite nomes de objetos separados por virgula:").lower()
objetos=objeto.split(",")

print(contarObjetos(objetos))
