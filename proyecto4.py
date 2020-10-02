#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:02:05 2019

@author: juan
"""
class Personajes():

    def __init__(self,nombre,ataque,defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa


    def Crear(self):
        nombreArchivo = "Personajes.txt"
        self.archivo = open(nombreArchivo, 'a')
        self.nombre = input('Nombre:')
        self.ataque = input('Ataque:')
        self.defensa=input('Defensa:')
        informacion = '\n'+self.nombre + '' +self.ataque+ ''+self.defensa
        self.archivo.write(informacion)
        self.archivo.close()

    def Actualizar(self):
        nombreArchivo = "Personajes.txt"
        archivo = open(nombreArchivo, 'r')
        lectura=archivo.readlines()
        archivo.close()
        self.nombre = input('Nombre personaje a editar:')

        for i in range(len(lectura)):
            lectura[i] = lectura[i].split(' ')

        for i in range(len(lectura)):
            if lectura [i][0] == self.nombre:
                lectura [i][1] = input('Ataque Nuevo: ')
                lectura [i][2] = input('Defensa Nueva: ')+'\n'

        datosActualizados = ''
        archivo = open(nombreArchivo , 'w')
        for i in range(len(lectura)):
            for j in range(len(lectura[i])):
                if j == 2:
                    datosActualizados += lectura[i][j]
                else:
                    datosActualizados += lectura[i][j] +' '
        archivo.write(datosActualizados)

        archivo.close()


    def Borrar(self):
        nombreArchivo = "Personajes.txt"
        archivo= open(nombreArchivo, 'r')
        lectura = archivo.readlines()
        archivo.close()
        for i in range(len(lectura)):
            lectura[i]= lectura[i].split(' ',)
        nombre = input('Personaje a borrar:')
        for i in range(len(lectura)):
            if lectura[i][0] == nombre:
                indice=i
        lectura.remove(lectura[indice])
        datosActualizados = ''
        archivo = open(nombreArchivo , 'w')
        for i in range(len(lectura)):
            for j in range(len(lectura[i])):
                if j == 2:
                    datosActualizados += lectura[i][j]
                else:
                    datosActualizados += lectura[i][j] +' '
        archivo.write(datosActualizados)

        archivo.close()

while True:
    print("Este es un menu para poder crear o actualizar los datos de un personaje.")
    print("1)Crear Personaje")
    print("2)Actualizar Datos")
    print("3)Borrar personaje")
    print("4) Salir")

    seleccion = []

    seleccion.append(float(input("¿Qué quieres hacer?")))

    if seleccion[0]==4:
        break


    for i in range(len(seleccion)):
        if seleccion[i] == 1:
            accion = Personajes(self.nombre,self.ataque,self.defensa)
            accion.Crear()
        elif seleccion[i] == 2:
            accion = Personajes(self.nombre,self.ataque,self.defensa)
            accion.Actualizar()
        elif seleccion[i] == 3:
            accion = Personajes(self.nombre,self.ataque,self.defensa)
            accion[i].Borrar()
