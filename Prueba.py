entradas = {}

def verificarCodigo(codigo):
    mayus = 0
    num = 0
    
    if len(codigo) >= 6:
        codigo = str()
        for letra in codigo:
            if letra.isdigit():
                mayus += 1
            
            if letra.isdigit():
                num += 1
            
            if mayus >= 1 and num >= 1:
                return True
        
        print("Código validado. ¡Entrada registrada con éxito!")   
        return True    
    else:
        print("Código no válido. Intente otra vez. ")
        return False
    


def buscarComprador(nombre):
    if nombre in entradas:
        print(nombre[1][2])
    else:
        print("El comprador no se encuentra.")

def cancelarCompra(nom):

    if nom in entradas:
        del entradas[nom]
        print("¡Compra cancelada!")
    else:
        print("No hay Registro de: ", nom)


print("""____________MENU PRINCIPAL____________
Concierto de Trap con el “Conejo Simpático”. 
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.""")

while True:
    try:
        opcion = input("Ingrese Opcion: ")

        match opcion:
            case "1": 
                try:
                    nombre = input("Ingrese Su Nombre: ")
                    tipoEntrada = input("Ingrese tipo de entrada (G/V): ")
                    if tipoEntrada in ["G","V"]:  
                        while True:
                            contra =  input("Ingrese código de confirmación: ")
                            if verificarCodigo(contra) == True:
                                entradas["Nombre":nombre,
                                        "tipoEntrada":tipoEntrada,
                                        "Codigo": contra]
                                break
                            else:
                                continue
                    else:
                        print("ingrese una entrada valida")
                except ValueError:
                    print("Vuelva A intentar")

            case "2":
                person = input("Ingrese nombre de comprador")
                buscarComprador(person)
                    
            case "3":
                persona = print("Ingrese nombre de comprador a cancelar")
                cancelarCompra(persona)
            case "4":
                print("Programa terminado...")
                break
            case _:
                print("INgrese Opcion Valida")
    except Exception:
        print("Ingrese Opcion correcta")     

