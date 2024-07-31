#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:18:04 2024

@author: ricardocruzgonzaga
"""


print("Programa que calcula el Indice de Masa Corporal")
try:
    e = float(input("Ingresa tu estatura en m: "))
    p = float(input("Ingresa tu peso en kg: "))

#Calculamos el IMC

    IMC = p/(e**2)
    print(f"Tu IMC es de: {IMC}")
    if IMC < 18.5:
        print('Estás bajo de peso')
    elif IMC <=24.9:
        print('Tu peso es normla')
    elif IMC <=29.9:
        print('Tienes sobrepeso')
    elif IMC >= 30:
        print('Tienes obesidad')
except ValueError:
    print('Ingrese nùmeros, por favor')    
except ZeroDivisionError:
    print('No hay división entre cero')