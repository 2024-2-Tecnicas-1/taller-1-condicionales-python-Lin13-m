def evaluar(caracter):
    if not (caracter.isalpha() or caracter.isdigit()):
         return "No es letra ni número";
    elif caracter.isdigit():
         return "Es número";

    elif caracter.isupper():
         return "Es letra mayúscula";
    
    elif caracter.islower():
       return "Es letra minúscula";


if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
