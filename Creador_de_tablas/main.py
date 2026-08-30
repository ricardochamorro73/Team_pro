from funciones_programa import (
    bucle_validacion,
    continuar,
    crear_nueva_tabla,
    agregar_informacion_a_la_tabla_csv,
    modificar_tabla_existente,
    convertir_la_tabla_a_markdown
    
)

def mostrar_opciones()->None:
    print('Este programa tiene 5 opciones:')
    print('A: Crear una tabla')
    print('B: Agregar informacion a una tabla existente')
    print('C: Modificar la informacion de una tabla existente')
    print('D: Convertir tabla a formato markdown')

#PROGRAMA
opciones:dict = {
    'A': crear_nueva_tabla,
    'B': agregar_informacion_a_la_tabla_csv,
    'C': modificar_tabla_existente,
    'D': convertir_la_tabla_a_markdown,
}

mostrar_opciones()

while True:
    #Asegurarse que la persona no escoja otras opciones a parte de esas
    opcion:str = bucle_validacion(mensaje='Escoja una opcion(A,B,C,D): ',nombre='opcion',str_validos=('A','B','C','D')).upper()
    funcion_del_programa = opciones[opcion]
    funcion_del_programa()

    if not continuar(mensaje='Quiere seguir en el programa?(s/n): '):
        break
