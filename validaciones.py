# VALIDACIONES

def validarFormatoEntero(texto):
    '''Verifica que el numero ingresado sea un numero entero'''
    # Autor/es principal/es: Santino Nasuti

    return texto.isnumeric()


def validarFormatoDecimal(texto):
    '''Verifica que el texto ingresado represente un número decimal (positivo o negativo)'''
    # Autor/es principal/es: Moro Bussolini
    
    # Primero se verifica casos vacios
    if texto == "" or texto == "-." or texto == ".":
        return False

    cantPuntos = 0
    
    inicio = 0
    if texto[0] == "-":
        if len(texto) == 1: # Si solo ingresó el signo menos
            return False
        inicio = 1

    for i in range(inicio, len(texto)):
        # Recorre el numero y verifica que maximo haya un punto, y que todo el resto de caracteres sean numeros
        if texto[i] == ".":
            cantPuntos = cantPuntos + 1
            if cantPuntos > 1:
                return False
        elif texto[i] < "0" or texto[i] > "9":
            return False

    return True


def validarOpcionMenu(opcion, desde, hasta):
    '''Verifica que la opcion del menu este dentro del rango permitido'''
    # Autor/es principal/es: Matias Cross
    
    return opcion >= desde and opcion <= hasta


def validarFormatoCodigo(codigo):
    '''Verifica que el codigo cumpla con el formato (4 a 10 caracteres alfanumericos)'''
    # Autor/es principal/es: Santino Nasuti
    
    if len(codigo) < 4 or len(codigo) > 10:
        return False

    if not codigo.isalnum():
        return False

    return True


def validarAerolinea(aerolinea, aerolineas):
    '''Verifica que la aerolinea exista sistema'''
    # Autor/es principal/es: Santino Nasuti
    
    for i in range(len(aerolineas)):
        if aerolineas[i] == aerolinea:
            return True
    return False


def validarDestino(destino):
    '''Verifica que el destino no este vacio'''
    # Autor/es principal/es: Santino Nasuti
    
    return len(destino.strip()) > 0


def validarCantidadPasajeros(cantidad):
    '''Verifica que la cantidad de pasajeros no sea negativa'''
    # Autor/es principal/es: Santino Nasuti
    
    return cantidad >= 0


def validarPesoEquipaje(peso):
    '''Verifica que el peso del equipaje no sea negativo'''
    # Autor/es principal/es: Santino Nasuti
    
    return peso >= 0


def validarEstadoOperativo(opcion):
    '''Verifica que la opcion de estado operativo sea valida'''
    # Autor/es principal/es: Santino Nasuti
    
    return opcion >= 1 and opcion <= 4


def validarTipoVuelo(tipo):
    '''Verifica que el tipo de vuelo sea Nacional o Internacional'''
    # Autor/es principal/es: Santino Nasuti
    
    return tipo == "Nacional" or tipo == "Internacional"