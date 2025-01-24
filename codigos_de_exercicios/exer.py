#questão 01

quantidade_produtos = int(input("Digite a quantidade de produtos: "))
valor_unitario_produto = float(input("Digite o valor unitário do produto: "))

    # Valor sem desconto

    valor_sem_desconto = quantidade * valor_unitario

    # Aplica o desconto de 10% se o valor total for superior a R$ 1000,00

    desconto_aplicado = valor_sem_desconto > 1000 and 0.10 or 0

    valor_com_desconto = valor_sem_desconto - (desconto_aplicado * valor_sem_desconto)

    if desconto_aplicado:
        print(f"Desconto aplicado: R$ {desconto_aplicado * valor_sem_desconto:.2f}")
        print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")
    else:
        print("Sem desconto aplicado.")



#questão 04


# Solicitar entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Função para calcular o resultado com base nas condições dadas
def calcular_resultado(num1, num2, num3):
    if num1 != 0 and num2 != 0 and num3 != 0:
        print("Todos os números são diferentes de zero")
        
        if num1 > 0 and num2 > 0 and num3 > 0:
            resultado = num1 * num2 * num3
            print(f"Resultado: Produto dos números = {resultado}")
        elif num1 > 0 or num2 > 0 or num3 > 0:
            resultado = num1 + num2 + num3
            print(f"Resultado: Soma dos números = {resultado}")
        else:
            resultado = (num1 + num2 + num3) / 3
            print(f"Resultado: Média dos números = {resultado}")
    else:
        print("Todos os números devem ser diferentes de zero.")

#questão 05

print(triangle_type(3, 4, 5))  # Scalene triangle.
print(triangle_type(3, 3, 3))  # Equilateral triangle.
print(triangle_type(3, 3, 4))  # Isosceles triangle.
print(triangle_type(1, 2, 3))  # The sides cannot form a triangle.

def triangle_type(a, b, c):
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "The sides cannot form a triangle."
    else:
        # Check the type of triangle
        if a == b == c:
            return "Equilateral triangle."
        elif a == b or a == c or b == c:
            return "Isosceles triangle."
        else:
            return "Scalene triangle."