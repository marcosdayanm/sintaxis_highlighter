import random

def lanzar_dados(num_dados, num_caras):
    resultados = [random.randint(1, num_caras) for _ in range(num_dados)]
    return resultados

def main():
    print("Simulador de lanzamiento de dados")
    num_dados = int(input("Número de dados a lanzar: "))
    num_caras = int(input("Número de caras de los dados: "))

    resultados = lanzar_dados(num_dados, num_caras)
    print("Resultados de los dados:", resultados)
    print("Suma total:", sum(resultados))

if __name__ == "__main__":
    main()
