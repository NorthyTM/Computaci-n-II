#Menu principal de opciones
print("===================================")
print("\n1.Ingreso de datos en tabla libros.")
print("\n2.Muestreo de datos de tabla libros.")
print("\n3.Busqueda de libros.")
print("\n5.Actualizar registros de libros.")
print("\n6.Eliminar registros de libros.")
print("===================================")

opcion = int(input("\nIngresar opcion: "))

#Ciclo if para validar los casos (referencia a case)

if opcion == 1:

    #funcion de ingreso de datos
    ID = int(input("\nIngresar ID: "))
    Title = input("\nIngresar Titulo: ")
    Author = input("\nIngresar Autor: ")
    Genre = input("\nIngresar Genero: ")
    ISBN = input("\nIngresar ISBN del libro: ")

    if ID > 0:
        print("El id es valido para su registro")

        #SQL INJECTION CON LOS DATOS RECIBIDOS

    else:
        print("Id invalido para registro")

prestado = True

#Seccion busqueda de * elementos
if opcion == 2:

    #SQL INJECTION PARA TOMAR TODOS LOS REGISTRO DE LA DTB
    #sqlSearch = ("""SELECT * FROM DTBNAME""")

#Seccion busqueda por nombres
if opcion == 3:

    #SQL INJECTION PARA BUSCAR POR NOMBRE
    #TitleSearch = input("\nIngresar Titulo: ")

    #sqlSearch = ("""SELECT * FROM DTBNAME WHERE NOMBRE = ?""")
    #sqlSearch([TitleSearch])