def evaluar(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido."
    if a == b == c:
        return "Triángulo equilátero (tres lados iguales)."
    elif a == b or b == c or a == c:
        return "Triángulo isósceles (dos lados iguales)."
    else:
        return "Triángulo escaleno (tres lados diferentes)."


if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
