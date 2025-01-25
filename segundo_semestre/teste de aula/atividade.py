
def receberNumeros():
    
    num1 = float(input("Digite o número: "))
    num2 = float(input("Digite o número: "))

    return num2 + num1

print(receberNumeros())


def receberNumeros(num1, num2):
    soma = num1 + num2
    return soma

num1 = float(input("Digite o número: "))
num2 = float(input("Digite o número: "))
print(receberNumeros(num1, num2))

