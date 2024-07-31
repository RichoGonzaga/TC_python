#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 20:09:46 2024

@author: ricardocruzgonzaga
"""

print("Programa para hacer conversión de divisas")
print('El usuario debera proporcionar la tasa de cambio')

tc = float(input('ingresa la tasa de cambio: '))
a = float(input('Ingresa la cantidad de dinero que desees hacer la cionversión: '))

if tc >= 0 and a >=0:
    b = a*tc 
    print(f'El dinero en la otra moneda es de: {b}')
else: 
    print('No hay tasas de cambios negativas ni dinero negativo')    