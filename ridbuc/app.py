import sqlite3
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

conn = sqlite3.connect('books.db')

sql = conn.cursor()


        
def Registrar():
    try:
        name = input('Registar nuevo libro--> ')
        name = str(name)
        stars  = input('Calificaion (1-5)--> ')
        stars = int(stars)
        notes = input('Reseña--> ')
        notes = str(notes)

        query = f"INSERT INTO books(Name, Stars, Notes) VALUES ('{name}', {stars}, '{notes}');"
        sql.execute(query)
        conn.commit()
        print('\n Libro registrado correctamente')
    except:
        print('Error al registrar el libro')
    

def Consultar_libros():
    try:
        query = "SELECT Name FROM books;"    
        sql.execute(query)
        libros = sql.fetchall()
        print("Libros registrados: \n")
        for libro in libros:
            print(f'\t {libro[0]}')
        print('\n')
    except:
        print('Error al consultar los libros')
        print('\n')

def Consultar_libro_detalle():
    try:
        name = input(Fore.BLUE + 'Nombre del libro a consultar--> ' + Style.RESET_ALL)
        name = str(name)
        query = f"SELECT Name, Stars, Notes FROM books WHERE Name = '{name}';"
        sql.execute(query)
        libro = sql.fetchall()
        print('\n')
        print(Fore.GREEN + Style.BRIGHT + '\t Titulo--> ' + Style.RESET_ALL, libro[0][0])
        print(Fore.YELLOW + Style.BRIGHT + '\t Estrellas--> ' + Style.RESET_ALL, libro[0][1])
        print(Fore.RED + Style.BRIGHT + '\t Notas--> ' + Style.RESET_ALL, libro[0][2])
        print('\n')
    except:
        print('Error al consultar el libro')
        
        
def Eliminar_libro():
    try:
        name = input('Nombre del libro a eliminar--> ')
        name = str(name)
        query = f"DELETE FROM books WHERE Name = '{name}';"
        sql.execute(query)
        conn.commit()
        print('Libro eliminado correctamente')
    except:
        print('Error al eliminar el libro')

def Salir():
    print('Saliendo...')
    sys.exit(0)


def main():
    while True:
        print('1) Registrar libro')
        print('2) Consultar libros registrados')
        print('3) Consultar libro en detalle')
        print('4) Eliminar libro')
        print('5) Salir')
        
        print('\n')
        opcion = input('Que deseas hacer?--> ')
        if opcion == '1':
            Registrar()
        elif opcion == '2':
            Consultar_libros()
        elif opcion == '3':
            Consultar_libro_detalle()
        elif opcion == '4':
            Eliminar_libro()
        elif opcion == '5':
            Salir()
        else:
            print('Opcion no valida')



    
if __name__ == '__main__':
    main()
    conn.close()