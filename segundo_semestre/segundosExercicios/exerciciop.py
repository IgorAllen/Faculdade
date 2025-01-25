# 1. Função que verifica se um valor é positivo
def eh_positivo():

    return valor > 0

valor = int(input("Digite um valor: "))
if eh_positivo():
    print("O valor é positivo!")
else:
    print("O valor é negativo.")

# 2. Função que imprime mensagem sobre o valor

def imprimir_valor(valor):

    if valor > 0:
        print(f"O valor {valor} informado é positivo")
    else:
        print(f"O valor {valor} informado é negativo")

valor = int(input("Digite um valor: ")) #O parametro tem que ficar fora
print("Imprimindo mensagem sobre o valor...")
imprimir_valor(valor)

# 3. Função que verifica se um valor é par ou ímpar
def eh_par_ou_impar(valor):

    if valor % 2 == 0:
        return f"O valor {valor} é par" #O return faz com que a função vire uma variavel com o valor à frente dele.
    else:
        return f"O valor {valor} é ímpar"

valor = int(input("Digite um valor: "))
print(eh_par_ou_impar(valor)) #print sempre na função debaixo.


# 4. Função que calcula a média de notas

def calcular_media(nota1, nota2, nota3, tipo_media):

    media = 0
    if tipo_media == 'A':
        media - (nota1 + nota2 + nota3)/3
    elif tipo_media == "P":
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2)/10
        
    return media

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
tipo_media = input("Digite o tipo de média (A ou P): ")
print(calcular_media(nota1, nota2, nota3, tipo_media))

# 5. Função que converte idade em dias
def idade_em_dias():
    anos = int(input("Digite a idade em anos: "))
    meses = int(input("Digite a idade em meses: "))
    dias = int(input("Digite a idade em dias: "))
    return anos * 360 + meses * 30 + dias

print("Convertendo idade em dias...")
idade_em_dias = idade_em_dias()
print(f"A idade em dias é: {idade_em_dias}")

# 6. Função que ordena valores em ordem crescente
def ordenar_valores():
    v1 = int(input("Digite o valor 1: "))
    v2 = int(input("Digite o valor 2: "))
    v3 = int(input("Digite o valor 3: "))
    valores = [v1, v2, v3]
    valores.sort()
    return ",".join(map(str, valores))

print("Ordenando valores em ordem crescente...")
valores_ordenados = ordenar_valores()
print(f"Os valores ordenados são: {valores_ordenados}")

# 7. Função que converte tempo em horas, minutos e segundos
def tempo_em_hms():
    segundos = int(input("Digite o tempo em segundos: "))
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f"{horas}:{minutos}:{segundos}"

print("Convertendo tempo em horas, minutos e segundos...")
tempo_em_hms = tempo_em_hms()
print(f"O tempo é: {tempo_em_hms}")

# 8. Função que verifica se um valor é perfeito
def eh_perfeito():
    valor = int(input("Digite um valor: "))
    soma_divisores = 0
    for i in range(1, valor):
        if valor % i == 0:
            soma_divisores += i
    return soma_divisores == valor

print("Verificando se um valor é perfeito...")
if eh_perfeito():
    print("O valor é perfeito!")
else:
    print("O valor não é perfeito.")

# 9. Função que calcula o peso ideal
def peso_ideal():
    altura = float(input("Digite a altura: "))
    sexo = input("Digite o sexo (M ou F): ")
    if sexo == 'M':
        return 72.7 * altura - 58
    elif sexo == 'F':
        return 62.1 * altura - 44.7
    else:
       

       # 10. Função que verifica se valores formam um triângulo
def eh_triângulo():
    x = float(input("Digite o lado X: "))
    y = float(input("Digite o lado Y: "))
    z = float(input("Digite o lado Z: "))
    if x + y > z and x + z > y and y + z > x:
        if x == y == z:
            return "Triângulo Equilátero"
        elif x == y or x == z or y == z:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não é um triângulo"

print("Verificando se valores formam um triângulo...")
resultado = eh_triângulo()
print(f"O resultado é: {resultado}")