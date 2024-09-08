def evaluar(numero1, numero2, numero3, numero4):

    numeros = [numero1, numero2, numero3, numero4]

    numeros.sort()
    return str(numeros)

numero1 = 7
numero2 = 0
numero3 = 6
numero4 = 1
resultado = evaluar(numero1, numero2, numero3, numero4)
print(resultado)


if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
