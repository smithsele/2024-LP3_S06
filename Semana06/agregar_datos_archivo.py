# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:41:39 2024

@author: Dell
"""
#"at" significa add text (para añadir texto)
archivo = open("noticia.txt","at")
# \n es para agregar el contenido en una línea al final
contenido="\nFuente: RPP"

archivo.write(contenido)

archivo.close()