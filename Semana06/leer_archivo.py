# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:21:18 2024

@author: Dell
"""
#"rt" significa read text (solo lectura de texto)
#para que se muestren las tildes y ñ, se agrega encoding='utf8'
noticia = open("noticia.txt","rt", encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)