def identificar_animal(caracteristica1, caracteristica2, caracteristica3):
    if caracteristica1 == "vertebrado":
        if caracteristica2 == "mamífero":
            if caracteristica3 == "onívoro":
                return "Homem"
            elif caracteristica3 == "herbívoro":
                return "Vaca"
        elif caracteristica2 == "ave":
            if caracteristica3 == "carnívoro":
                return "Águia"
            elif caracteristica3 == "onívoro":
                return "Pomba"
    elif caracteristica1 == "invertebrado":
        if caracteristica2 == "anelídeo":
            if caracteristica3 == "onívoro":
                return "Minhoca"
        elif caracteristica2 == "inseto":
            if caracteristica3 == "herbívoro":
                return "Lagarta"

def main():
    caracteristica1 = input("Digite a primeira característica: ")
    caracteristica2 = input("Digite a segunda característica: ")
    caracteristica3 = input("Digite a terceira característica: ")
    animal = identificar_animal(caracteristica1, caracteristica2, caracteristica3)
    print(f"O animal é: {animal}")

main()