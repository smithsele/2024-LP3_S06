# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:08:13 2024

@author: Dell
"""
# Importamos la libreria
import camelcase

nombre = "smith seleni ramos sanchez"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'smith' y 'ramos' 
cam2 = camelcase.CamelCase('smith','ramos')
print(cam2.hump(nombre))