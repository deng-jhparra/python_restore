tipo_ambiente = ['localhost','Desarrollo','Calidad']

def menu (tipo,etiqueta):
    while True:
        for elemento in tipo:
            print(tipo.index(elemento) + 1, elemento)
        seleccion = int(input("Seleccione un " + etiqueta + " : "))
        if seleccion > 0 and seleccion <= len(tipo):
            break
    return seleccion - 1

        
while True:
    ambiente = menu(tipo_ambiente,'ambiente')
    print("Ud selecciono ", tipo_ambiente[ambiente])
    seguir = input ('Continuar S/N : ')
    if seguir.upper() == 'N':
        break
print("Fin del Proceso")    
