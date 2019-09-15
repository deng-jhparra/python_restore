servidores = ['localhost','A','B']
def menu(servidores,etiqueta):
    while True:
        for host in servidores:
            print(servidores.index(host) + 1,host)
        seleccion = int(input("Seleccione un "))
        if seleccion > 0 and seleccion <= len(servidores):
            break
    return seleccion
        
while True:
    servidor=menu(servidores,'Servidor')
    print("Ud selecciono ", servidor)
    seguir = input ('Continuar S/N : ')
    if seguir.upper() == 'N':
        break
print("Fin del Proceso")    
