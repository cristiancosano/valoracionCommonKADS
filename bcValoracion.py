#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: bcValoracion.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''

import types

class Clase():
    def __init__(self, nombre):
        self.nombre=nombre
        self.reglas=[]
        self.descripcion=u'' 
		self.atributos=[]

	def getAtributo(nombre):
		response = None
		for atributo in self.atributos:
			if(atributo.nombre == nombre):
				response = atributo
		return response

	def getAtributoValor(nombre):
		response = self.getAtributo(nombre)
		if(request != None):
			response = response.valor
		return response
	def setAtributoSiExiste(nombre, valor):
		response = None
		for atributo in self.atributos:
			if(atributo.nombre == nombre):
				atributo.valor = valor
				response = atributo
		return response


class Regla():
	def __init__(self,idRegla):
		self.idRegla=idRegla
		pass

class Atributo():
	"""
	Clase Atributo. permite especificar las propiedades
	de los atributos que van a usarse en la base de conocimiento para 
	describir un objeto.
	"""	
	def __init__(self,nombre,tipo,unidad,valor=None,posiblesValores=None):
		self.nombre=nombre
		self.tipo=tipo
		self.unidad=unidad

		# Obtenemos los posibles valores del atributo en caso de que sea de tipo multiple
		if (tipo=='multiple') and (posiblesValores is not None) and (type(posiblesValores) is types.ListType):
			self.posiblesValores = posiblesValores 
			
		# Comprobamos si el tipo de atributo es boleano para añadir los posibles valores de dicho tipo
		if tipo=='boleano':
			self.posiblesValores= [True, False]
