# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:30:32 2024

@author: Dell
"""
#"wt" significa write text (para escribir texto)
archivo = open ("archivo_de_prueba.txt","wt")
contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a la UNTELS."
archivo.write(contenido)
archivo.close()