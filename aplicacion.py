import gestion_archivos
try:
    print("MENU\n"+
          "1. Crear archivo\n"+
          "2. Eliminar archivo\n"+
          "3. Agregar contenido\n"+
          "4. Mostrar contenido de archivo\n"+
          "5. Salir"
          )
except KeyboardInterrupt:
    print("\nSe ha interrumpido la ejecución del programa.")
opcion = int(input("Digite opción: "))

def crear_archivo():
    print("Crear un archivo")
    nombre = input("Archivo: ")
    print(gestion_archivos.crear_archivo(nombre))
def eliminar_archivo():
    print("Eliminar un archivo")
    nombre = input("Archivo: ")
    print(gestion_archivos.eliminar_archivo(nombre))
def agregar_contenido_archivo():
    print("Agregar contenido a un archivo")
    nombre = input("Archivo: ")
    print(gestion_archivos.agregar_contenido_archivo(nombre))
def leer_archivo():
    print("Mostrar contenido de un archivo")
    nombre = input("Archivo: ")
    print(gestion_archivos.leer_archivo(nombre))
def error():
    print("Error")

if (opcion ==1):
    crear_archivo() 
elif (opcion ==2):
    eliminar_archivo()
elif (opcion ==3):
    agregar_contenido_archivo()
elif (opcion ==4):
    leer_archivo()
else:
    error()
    