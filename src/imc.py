def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    imc = peso / (estatura * estatura);
    if imc < 18.5 :
        condicion = "bajo";
    elif  (imc >=18.5 and imc < 24.9) :
        condicion = "medio"
    else :
        condicion = "alto"
    return condicion;


if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
