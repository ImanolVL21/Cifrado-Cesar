2
def E(x, y):
    resultado = ""
    for i in range(len(x)):
        # Solo funciona correctamente con letras mayúsculas A-Z
        letra_cifrada = chr((((ord(x[i]) - ord('A')) + y) % 26) + ord('A'))
        resultado += letra_cifrada
    return resultado

def D(x, y):
    resultado = ""
    for i in range(len(x)):
        # Solo funciona correctamente con letras mayúsculas A-Z
        letra_cifrada = chr(((( ord(x[i]) - ord('A')) - y) % 26) + ord('A'))
        resultado += letra_cifrada
    return resultado



def main():
    print("1. Cifrar")
    print("2. Descifrar")

    opcion = int(input("Opcion: "))
    texto = input("Ingrese el texto(mayusculas): ")
    clave = int(input("Ingrese la clave (desplazamiento): "))

    if opcion == 1:
        resultado = E(texto, clave)
        print("Texto cifrado:", resultado)
    elif opcion == 2:
        resultado = D(texto, clave)
        print("Texto descifrado:", resultado)
    else:
        print("Opcion invalida")


if __name__ == "__main__":
    main()
