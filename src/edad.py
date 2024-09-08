from datetime import date
def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edadz
    fecha_actual = date.today()

    # Crear la fecha de nacimiento
    fecha_nacimiento = date(anno, mes, dia)

    # Calcular la diferencia de años entre la fecha actual y la de nacimiento
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    print(f"Usted tiene {edad} años.")

    return "";

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
