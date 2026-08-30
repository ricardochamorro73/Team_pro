#Funciones de validacion
def validacion_string(dato:str,str_validos:tuple[str]|str = None,nombre:str=None)->None:
    """Valida si el dato es un string y si es string valida si tiene un caracter ademas del espacio, puede validar tambien si el dato pertenece a un string o conjunto de strings.
    Ademas, para un uso mas flexible se le implemento el parametro 'nombre' para usarlo para representar diferentes tipos de datos
    que contienen strings,por ejemplo, un nombre.
    """
    if nombre is None:
        nombre="dato"
    if not isinstance(dato,str):
        raise ValueError(f"{nombre} debe ser un string")
    if dato == "" or len(dato.split()) == 0:
        raise ValueError(f"{nombre} no debe ser una cadena vacia")
    #Si es que especifican valores especificos de strings.
    if str_validos != None:
        str_validos = map(lambda x: x.lower(),str_validos)
        if dato.lower() not in str_validos:
            raise ValueError(f"{nombre} no es un string valido")
        
def bucle_validacion(mensaje:str,str_validos:tuple[str]|str = None,nombre:str=None)-> None:
    """Entra en bucle y validara el tipo de dato ingresado.
    Ademas, para un uso mas flexible se le implemento el parametro 'nombre' para usarlo para representar diferentes tipos de datos
    que contienen strings.
    De esta forma el mensaje de error sera mas especifico, lo que ayudara a depurar facilmente el codigo ante posibles fallos.
    """
    while True: 
        try:    
            variable = input(mensaje)
            validacion_string(variable,str_validos,nombre)
            return variable
        except ValueError as e:
            print(e)


#Funciones auxiliares
def continuar(mensaje:str) -> bool:
    while True:
        seguir = input(mensaje)
        if seguir in ('s','n'):
            return seguir == 's'
        else:
            print(f'Entrada Invalida: La entrada "{seguir}" debe ser "n" o "s".')

def crear_columnas()->list:
    columnas:list = []
    while True:
        columna:str = input('Ingrese el nombre de la columna de su tabla: ').strip().title()
        columnas.append(columna)
        if not continuar(mensaje='Quieres agregar otra columna a tu tabla?(s/n): '):
            break
    return columnas

def crear_informacion_tabla(columnas_tabla)->dict:
    fila:int = 1
    informacion_tabla:dict = {}
    while True:    
        for columna in columnas_tabla:
            contenido:str = input(f'\nQue informacion desea agregar a la fila {fila} de la columna "{columna}"?:\n')
            informacion_tabla[columna] = [contenido] if informacion_tabla.get(columna,None) == None else informacion_tabla[columna].append(contenido)

        if not continuar(mensaje='Quieres agregar otra fila a tu tabla?(s/n): '):
            break
        fila += 1
    return informacion_tabla


#OPCIONES DEL PROGRAMA
def crear_nueva_tabla() -> None:
    columnas:list = crear_columnas()

    informacion_de_la_tabla:dict = crear_informacion_tabla(columnas)
    
    nueva_tabla = pd.DataFrame(data= informacion_de_la_tabla)

    #Guardar la tabla como archivo csv(Comma-Separated-Values)
    nombre = input('Como quieres llamar a tu tabla?(El nombre no debe tener espacios):\n').replace(" ","") + '.csv'
    nueva_tabla.to_csv(nombre,mode='w',index=False)

def agregar_informacion_a_la_tabla_csv()->None:
    nombre_tabla:str = input('Ingrese el nombre exacto de la tabla(revise como esta guardada en el equipo): ')
    columnas = pd.read_csv(nombre_tabla).columns.to_list()

    nueva_informacion_tabla:list = crear_informacion_tabla(columnas)

    tabla = pd.DataFrame(data=nueva_informacion_tabla)

    tabla.to_csv(nombre_tabla,mode='a',index=False,header=False)


def modificar_tabla_existente():
    print('Proximamente estara disponible')

def convertir_la_tabla_a_markdown():
    nombre_tabla:str = input('Ingrese el nombre exacto de la tabla(revise como esta guardada en el equipo): ')

    tabla = pd.read_csv(nombre_tabla)

    tabla_en_markdown = tabla.to_markdown(index=False)

    print(tabla_en_markdown)
