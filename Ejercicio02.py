#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:26:35 2024

@author: ricardocruzgonzaga
"""
meses1 = [0, 0.01, 0.02, 0.03]
meses2 = [0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11 ]
print("Programa para calcular las horas de sueño segun tu edad")
try:
    edad = float(input('Ingresa tu edad en años: '))
    if edad < 0:
        print('No hay edades negativas')
    elif edad in meses1:
        print('Deberias de dormir entre 14 y 17 horas al día')
    elif edad in meses2:
        print('Deberias de dormir entre 12 a 15 horas al día')
    elif edad >= 1 and edad < 3:
        print('Deberias de dormir entre 11 a 14 horas')
    elif edad >= 3 and  edad < 6:
        print("Deberias de dormir entre 10 a 13 horas")
    elif edad >= 6 and edad < 14:
        print("Deberias de dormir entre 9 y 11 horas")
    elif edad >=14 and edad < 18:
        print("Deberias de dormir  10,08 horas")
    elif edad >= 18 and edad <= 64:
        print("Deberias dormir entre 7 a 9 horas al dìa") 
    elif edad > 64:
        print('deberias dormir entre 7 a 8 horas')
    else:
        print('Edad no valida')

except ValueError:
    print('Ingrese un nùmero, por favor')

