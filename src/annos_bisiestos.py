def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos

    if (anno % 4)  != 0:

        return ' El año no es Biciesto'
    else:
        if (anno % 100) == 0:
            if (anno % 400) == 0:
                return ' El año es Biciesto'
            else:
                return ' El año no es Biciesto'
        else:
            return ' El año es Biciesto'

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)


