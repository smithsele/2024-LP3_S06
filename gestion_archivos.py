#nombre = input("Ingrese nombre: ")
def crear_archivo(nombre):
        archivo = open (nombre,"wt")
        contenido = input("Contenido: ")
        archivo.write(contenido)
        archivo.close()

def eliminar_archivo(nombre):
        import os
        os.remove(nombre)

def agregar_contenido_archivo(nombre):
        archivo = open(nombre,"at")
        contenido = input("Contenido que desea agregar: ")
        archivo.write(contenido)
        archivo.close() 

def leer_archivo(nombre):
        leer = open(nombre,"rt", encoding='utf8')
        datos_lectura = leer.read()
        print(datos_lectura)
        