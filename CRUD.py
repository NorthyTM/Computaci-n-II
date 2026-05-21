import mysql.connector #Importe de librería para gestionar Database
conn = mysql.connector.connect(
     host = "localhost", #host el nombre de la conexión generada
     user = "root", #nombre del usuario admin de la dtb
     password = "", #contraseña del usuario admin de la dtb
     database = "" #nombre de la dtb / eschema a utilizar
)

cursor = conn.cursor() #definición de cursor para posicionar búsquedas dentro de la dtb

#Menu principal de opciones
print("===================================")
print("\n1.Ingreso de datos en tabla libros.")
print("\n2.Muestreo de datos de tabla libros.")
print("\n3.Busqueda de libros.")
print("\n5.Actualizar registros de libros.")
print("\n6.Eliminar registros de libros.")
print("===================================")
opcion = int(input("\nIngresar opcion: "))

# Ciclo if para validarlos casos (referencia a case)
if opcion == 1:
    #funcion de ingreso de datos
    ID = int(input("\nIngresar ID: "))
    Title = input("\nIngresar Titulo: ")
    Author = input("\nIngresar Autor: ")
    Genre = input("\nIngresar Genero: ")
    ISBN = input("\nIngresar ISBN del libro: ")

    # SQL INJECTION CON LOS DATOS RECIBIDOS
    if ID > 0:
        print("El id es valido para su registro")
        print("\n")
        sql = """INSERT INTO libros(titulo, autor, genero, ISBN) VALUES (%s, %s, %s, %s)"""
        values_insert = (ID, Title, Author, Genre, ISBN)
        cursor.execute(sql, values_insert) #execute indica la ejecución de comandos sql
        conn.commit() #commit actualizar la database con el query hecho y cierra la conexión
        print("\nRegistro insertado")
    else:
        print("Id invalido para registro")
prestado = True

#Seccion busqueda de * elementos
if opcion == 2:
    #SQL Injection para tomar todos los registros de la dtb
    #sqlSearch = ("""SELECT * FROM DTBNAME""")

#Seccion busqueda por nombres
if opcion == 3:

    #SQL Injection para buscar por nombre
    #TitleSearch = input("\nIngresar Titulo: ")

    #sqlSearch = ("""SELECT * FROM DTBNAME WHERE NOMBRE = ?""")
    #sqlSearch([TitleSearch])