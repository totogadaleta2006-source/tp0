import random
from validaciones import *

# BUSQUEDA Y ORDENAMIENTO

def buscarVueloPorCodigo(vuelos, codigo):
    '''Busqueda secuencial de un vuelo por codigo. Retorna la posicion o -1 si no existe'''
    # Autor/es principal/es: Santiago Molina
    
    for i in range(len(vuelos)):
        if vuelos[i][0] == codigo:
            return i
    return -1


def codigoDisponible(vuelos, codigo):
    '''Verifica que el codigo no exista ya en el sistema usando la busqueda secuencial'''
    # Autor/es principal/es: Santiago Molina
    
    return buscarVueloPorCodigo(vuelos, codigo) == -1


def ordenarVuelos(vuelos):
    '''Ordena los vuelos de mayor a menor pasajeros. Si empatan, destino alfabetico'''
    # Autor/es principal/es: Santiago Molina
    
    for i in range(len(vuelos)):
        for j in range(i + 1, len(vuelos)):
            pasajerosI = vuelos[i][3]
            pasajerosJ = vuelos[j][3]
            destinoI = vuelos[i][1]
            destinoJ = vuelos[j][1]

            intercambiar = False
            if pasajerosJ > pasajerosI:
                intercambiar = True
            elif pasajerosJ == pasajerosI and destinoJ < destinoI:
                intercambiar = True

            if intercambiar:
                auxiliar = vuelos[i]
                vuelos[i] = vuelos[j]
                vuelos[j] = auxiliar

# INGRESO DE DATOS

def ingresarEntero(mensaje, mensajeError):
    '''Ingresa un entero validando el formato antes de convertir'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFormatoEntero(texto):
            return int(texto)
        print(mensajeError)


def ingresarEnteroEnRango(mensaje, mensajeError, minimo, maximo):
    '''Ingresa un entero validando formato y rango permitido'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFormatoEntero(texto):
            numero = int(texto)
            if numero >= minimo and numero <= maximo:
                return numero
        print(mensajeError)


def ingresarDecimalPositivo(mensaje, mensajeError):
    '''Ingresa un decimal positivo validando formato y valor (directo valida el peso)'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFormatoDecimal(texto):
            numero = float(texto)
            if validarPesoEquipaje(numero):
                return round(numero, 2)
        print(mensajeError)


def ingresarTexto(mensaje, mensajeError, validarFuncion):
    '''Ingresa un texto y lo valida con la funcion recibida por parametro'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFuncion(texto):
            return texto
        print(mensajeError)


def ingresarOpcion(desde, hasta):
    '''Valida que se ingrese una opcion entre dos parametros (desde y hasta)'''
    # Autor/es principal/es: Matias Cross
    
    while True:
        texto = input("Elija alguna opcion: ")
        if validarFormatoEntero(texto):
            opcion = int(texto)
            if validarOpcionMenu(opcion, desde, hasta):
                return opcion
        print("Por favor, elija alguna opcion valida.")


def ingresarCodigoManual(vuelos, aerolineas):
    '''Ingresa manualmente el codigo de vuelo y valida formato y si esta disponible'''
    # Autor/es principal/es: Tomas Gadaleta
    
    while True:
        aerolinea = input("Ingrese la aerolinea (AA, LAT, FLY, EU, QAT, JET): ").upper()
        while not validarAerolinea(aerolinea, aerolineas):
            aerolinea = input("Error. Ingrese una aerolinea valida: ").upper()

        numero = ingresarEnteroEnRango(
            "Ingrese el numero de vuelo (1-999): ",
            "Error. Ingrese un numero entre 1 y 999.",
            1,
            999
        )

        # El .zfill agrega a la izquierda ceros si no hay nada. La cantidad de ceros se pasa por parametro
        codigo = aerolinea + str(numero).zfill(3)

        if validarFormatoCodigo(codigo) and codigoDisponible(vuelos, codigo):
            return codigo

        print()
        print("El codigo ingresado es invalido o ya existe. Por favor, intente de nuevo.")
        print()


def ingresarDestinoManual():
    '''Ingresa el destino manualmente y controla que no este vacio'''
    # Autor/es principal/es: Santino Nasuti
    
    destino = ingresarTexto(
        "Ingrese el lugar de destino: ",
        "Error. El destino no puede estar vacio.",
        validarDestino
    )
    return destino.title()


def ingresarHorarioManual():
    '''Ingresa el horario manualmente y valida que cumpla con el formato HH:MM'''
    # Autor/es principal/es: Santino Nasuti
    
    hora = ingresarEnteroEnRango(
        "Ingrese la hora del horario de salida del vuelo (0-23): ",
        "Error. Ingrese una hora valida entre 0 y 23.",
        0,
        23
    )
    minutos = ingresarEnteroEnRango(
        "Ingrese los minutos del horario de salida del vuelo (0-59): ",
        "Error. Ingrese minutos validos entre 0 y 59.",
        0,
        59
    )
    return str(hora).zfill(2) + ":" + str(minutos).zfill(2)


def ingresarPasajerosManual():
    '''Ingresa la cantidad de pasajeros manualmente y valida que no sea negativa'''
    # Autor/es principal/es: Santino Nasuti
    
    while True:
        cantPasajeros = ingresarEntero(
            "Ingrese la cantidad de pasajeros: ",
            "Error. Debe ingresar un numero entero valido."
        )
        if validarCantidadPasajeros(cantPasajeros):
            return cantPasajeros
        print("No se pueden ingresar numeros negativos.")


def ingresarPesoManual():
    '''Ingresa el peso del equipaje manualmente y controla que no sea negativo'''
    # Autor/es principal/es: Santino Nasuti
    
    return ingresarDecimalPositivo(
        "Ingrese el peso del equipaje: ",
        "Error. Debe ingresar un peso valido y no negativo."
    )


def ingresarEstadoManual(estados):
    '''Ingresa el estado operativo manualmente'''
    # Autor/es principal/es: Santino Nasuti
    
    mostrarEstadosOperativos()
    opcion = ingresarOpcion(1, 4)
    # Opcion - 1 ya que los indices empiezan desde 0
    return estados[opcion - 1]


def ingresarTipoManual():
    '''Ingresa el tipo del vuelo y controla que sea Nacional o Internacional'''
    # Autor/es principal/es: Santino Nasuti
    
    while True:
        tipo = input("Indique el tipo del vuelo (Nacional o Internacional): ").capitalize()
        if validarTipoVuelo(tipo):
            return tipo
        print("Error. Debe ingresar Nacional o Internacional.")


# GENERACION ALEATORIA


def crearCodigoVuelo(vuelos, aerolineas):
    '''Genera aleatoriamente un codigo de vuelo unico'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    while True:
        aerolinea = random.choice(aerolineas)
        numero = str(random.randint(1, 999)).zfill(3)
        codigo = aerolinea + numero

        if validarFormatoCodigo(codigo) and codigoDisponible(vuelos, codigo):
            return codigo


def crearHorario():
    '''Genera aleatoriamente un horario de vuelo respetando el modelo HH:MM'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    hora = random.randint(0, 23)
    minutos = random.randint(0, 59)
    return str(hora).zfill(2) + ":" + str(minutos).zfill(2)


def crearDatosVueloAleatorio(vuelos, aerolineas, destinos, estados, tiposVuelo):
    '''Genera todos los datos de un vuelo de forma aleatoria'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    codigo = crearCodigoVuelo(vuelos, aerolineas)
    destino = random.choice(destinos)
    horario = crearHorario()
    cantPasajeros = random.randint(1, 300)
    peso = round(random.uniform(1000, 30000), 2)
    estado = random.choice(estados)
    tipo = random.choice(tiposVuelo)
    return [codigo, destino, horario, cantPasajeros, peso, estado, tipo]


# MENUS


def inicio():
    '''Muestra las opciones de inicio cuando no hay vuelos cargados'''
    # Autor/es principal/es: Tomas Gadaleta
    
    print("========================================")
    print("SISTEMA DE GESTION: SKYBRIDGE AIRLINES")
    print("Ingrese:")
    print()
    print("1: Registrar vuelo (Alta)")
    print("2: Salir")
    print()
    print("========================================")


def mostrarOpciones():
    '''Muestra las opciones del menu principal'''
    # Autor/es principal/es: Tomas Gadaleta
    
    print("========================================")
    print("SISTEMA DE GESTION: SKYBRIDGE AIRLINES")
    print()
    print("1: Registrar vuelo (Alta)")
    print("2: Eliminar vuelo (Baja)")
    print("3: Modificar vuelo (Modificacion)")
    print("4: Informe General (Visualizacion de Datos)")
    print("5: Salir")
    print()
    print("========================================")


def tipoIngreso():
    '''Muestra las opciones de tipo de ingreso (Alta)'''
    # Autor/es principal/es: Tomas Gadaleta
    
    print("========================================")
    print("Tipo de ingreso:")
    print("Ingrese:")
    print()
    print("1: Aleatorio")
    print("2: Por consola")
    print()
    print("========================================")


def mostrarEstadosOperativos():
    '''Muestra las opciones para ingresar un estado operativo'''
    # Autor/es principal/es: Santino Nasuti
    
    print()
    print("Estados Operativos:")
    print("1: Programado")
    print("2: Embarcando")
    print("3: En vuelo")
    print("4: Cancelado")
    print()


def mostrarOpcionesEliminacion():
    '''Muestra las opciones de eliminacion de vuelos'''
    # Autor/es principal/es: Matias Cross
    
    print()
    print("========================================")
    print("Eliminacion de vuelos:")
    print("Ingrese:")
    print()
    print("1: Si desea ingresar algun codigo para eliminar un vuelo")
    print("2: Si desea volver al menu principal")
    print("========================================")
    print()


def mostrarOpcionesModificacion():
    '''Muestra las opciones de modificacion de vuelos'''
    # Autor/es principal/es: Moro Bussolini
    
    print()
    print("========================================")
    print("Opciones de Modificacion de Vuelos:")
    print("Ingrese:")
    print()
    print("1: Modificar Destino de vuelo.")
    print("2: Modificar Horario de Salida de vuelo.")
    print("3: Modificar Cantidad de Pasajeros de vuelo.")
    print("4: Modificar Peso Total de Equipaje Despachado de vuelo.")
    print("5: Modificar Estado Operativo de vuelo.")
    print("6: Modificar Tipo de vuelo.")
    print("7: Terminar modificacion.")
    print()
    print("========================================")
    print()


def mostrarVuelo(vuelo):
    '''Muestra los datos de un vuelo en pantalla'''
    # Autor/es principal/es: Santiago Molina
    
    print("Codigo de vuelo:", vuelo[0])
    print("Destino:", vuelo[1])
    print("Horario de salida:", vuelo[2])
    print("Cantidad de pasajeros:", vuelo[3])
    print("Peso de equipaje despachado:", vuelo[4], "KG")
    print("Estado de vuelo:", vuelo[5])
    print("Tipo de vuelo:", vuelo[6])
    print()


# OPERACIONES PRINCIPALES


def ingresoManual(vuelos, aerolineas, estados):
    '''Permite ingresar N vuelos manualmente. N se pregunta por consola'''
    # Autor/es principal/es: Santino Nasuti
    
    cantidad = ingresarEnteroEnRango(
        "Ingrese cuantos vuelos desea dar de alta (1-50): ",
        "Por favor, ingrese una cantidad de vuelos a agregar valida.",
        1,
        50
    )

    for i in range(cantidad):
        vuelo = [
            ingresarCodigoManual(vuelos, aerolineas),
            ingresarDestinoManual(),
            ingresarHorarioManual(),
            ingresarPasajerosManual(),
            ingresarPesoManual(),
            ingresarEstadoManual(estados),
            ingresarTipoManual()
        ]
        vuelos.append(vuelo)

    print()
    if cantidad == 1:
        print("El vuelo se ha agregado correctamente.")
    else:
        print("Los vuelos se han agregado correctamente.")


def generarVuelosAleatorios(vuelos, aerolineas, destinos, estados, tiposVuelo):
    '''Genera aleatoriamente N vuelos. N se pide por consola'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    print()
    cantidad = ingresarEnteroEnRango(
        "Ingrese la cantidad de vuelos a generar (1-50): ",
        "Por favor, ingrese una cantidad valida.",
        1,
        50
    )

    print()
    print("Vuelos generados aleatoriamente:")
    print()

    for i in range(cantidad):
        vuelo = crearDatosVueloAleatorio(vuelos, aerolineas, destinos, estados, tiposVuelo)
        vuelos.append(vuelo)
        mostrarVuelo(vuelo)


def registrarVueloMenu(vuelos, aerolineas, destinos, estados, tiposVuelo):
    '''Coordina el alta de vuelos (manual o aleatoria)'''
    # Autor/es principal/es: Tomas Gadaleta
    
    tipoIngreso()
    opcionAlta = ingresarOpcion(1, 2)

    if opcionAlta == 1:
        generarVuelosAleatorios(vuelos, aerolineas, destinos, estados, tiposVuelo)
    else:
        ingresoManual(vuelos, aerolineas, estados)


def eliminarVuelo(vuelos):
    '''Permite eliminar un vuelo cancelado ingresando su codigo. Pide una segunda confirmacion'''
    # Autor/es principal/es: Matias Cross
    
    mostrarOpcionesEliminacion()
    opcion = ingresarOpcion(1, 2)

    while opcion == 1:
        print()
        codigo = input("Ingrese el codigo del vuelo a eliminar: ").upper()
        posicion = buscarVueloPorCodigo(vuelos, codigo)

        if posicion == -1:
            print("No se encontro un vuelo con ese codigo.")
        elif vuelos[posicion][5] != "Cancelado":
            print()
            print("Solo se pueden eliminar vuelos cancelados.")
        else:
            confirmar = input("Seguro que desea eliminar el vuelo? (SI/NO): ").upper()
            while confirmar != "SI" and confirmar != "NO":
                print("Por favor, ingrese una opcion valida.")
                confirmar = input("Seguro que desea eliminar el vuelo? (SI/NO): ").upper()

            print()
            if confirmar == "SI":
                vuelos.pop(posicion)
                print("Vuelo eliminado correctamente.")
            else:
                print("Eliminacion cancelada.")
            print()

        mostrarOpcionesEliminacion()
        opcion = ingresarOpcion(1, 2)

    print()
    print("Se ha finalizado la eliminacion de vuelos.")


def modificarVuelo(vuelos, estados):
    '''Permite buscar un vuelo por codigo y modificar uno o mas atributos'''
    # Autor/es principal/es: Moro Bussolini
    
    codigo = input("Ingrese el Codigo del Vuelo del cual quiere realizar una modificacion: ")
    posicion = buscarVueloPorCodigo(vuelos, codigo)

    while posicion == -1:
        print("El codigo ingresado no existe. Intente de nuevo.")
        codigo = input("Ingrese el Codigo del Vuelo del cual quiere realizar una modificacion: ")
        posicion = buscarVueloPorCodigo(vuelos, codigo)

    mostrarOpcionesModificacion()
    opcion = ingresarOpcion(1, 7)

    while opcion != 7:
        if opcion == 1:
            vuelos[posicion][1] = ingresarDestinoManual()
            print("El destino del vuelo fue modificado.")
        elif opcion == 2:
            vuelos[posicion][2] = ingresarHorarioManual()
            print("El horario del vuelo fue modificado.")
        elif opcion == 3:
            vuelos[posicion][3] = ingresarPasajerosManual()
            print("La cantidad de pasajeros del vuelo fue modificada.")
        elif opcion == 4:
            vuelos[posicion][4] = ingresarPesoManual()
            print("El peso de equipaje despachado del vuelo fue modificado.")
        elif opcion == 5:
            vuelos[posicion][5] = ingresarEstadoManual(estados)
            print("El estado operativo del vuelo fue modificado.")
        else:
            vuelos[posicion][6] = ingresarTipoManual()
            print("El tipo del vuelo fue modificado.")

        mostrarOpcionesModificacion()
        opcion = ingresarOpcion(1, 7)

    print()
    print("Se han realizado las modificaciones del vuelo.")


def mostrarInformeGeneral(vuelos):
    '''Muestra un informe general de los vuelos ordenados'''
    # Autor/es principal/es: Santiago Molina
    
    print()
    print("INFORME GENERAL - VUELOS REGISTRADOS")
    print()

    ordenarVuelos(vuelos)

    for i in range(len(vuelos)):
        mostrarVuelo(vuelos[i])


# PROGRAMA PRINCIPAL (main)

def main():
    '''Ejecucion principal del programa. Coordina llamadas a funciones'''
    # Autor/es principal/es: Tomas Gadaleta
    
    aerolineas = ["AA", "LAT", "FLY", "EU", "QAT", "JET"]
    destinos = ["Madrid", "Barcelona", "Buenos Aires", "Nueva York", "Miami"]
    estados = ["Programado", "Embarcando", "En vuelo", "Cancelado"]
    tiposVuelo = ["Nacional", "Internacional"]

    vuelos = []
    opcion = 0

    while opcion != 5:
        if len(vuelos) == 0:
            inicio()
            opcionAlta = ingresarOpcion(1, 2)

            if opcionAlta == 1:
                registrarVueloMenu(vuelos, aerolineas, destinos, estados, tiposVuelo)
            else:
                opcion = 5
        else:
            mostrarOpciones()
            opcion = ingresarOpcion(1, 5)

            if opcion == 1:
                registrarVueloMenu(vuelos, aerolineas, destinos, estados, tiposVuelo)
            elif opcion == 2:
                eliminarVuelo(vuelos)
            elif opcion == 3:
                modificarVuelo(vuelos, estados)
            elif opcion == 4:
                mostrarInformeGeneral(vuelos)

    print()
    print("Se ha finalizado la ejecucion del sistema.")
    print()


main()