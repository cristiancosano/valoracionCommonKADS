#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: ckCtrlValoracion.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''
from ckModValoracion import Dominio
import bcValoracionEmpleo
import bcValoracionPrestamos

def obtenerDominio(dominio):
    dominios = {
			'Empleo':  bcValoracionEmpleo,
			'Prestamos': bcValoracionPrestamos
	}
    return dominios[dominio]
def valorar(dominio, criterio, datos):
	resultado = None
	if(dominio == 'Empleo'):
		resultado = valorarEmpleo(criterio, datos)
	elif(dominio == 'Prestamos'):
		resultado = valorarPrestamo(criterio, datos)
	
	return resultado

def valorarEmpleo(criterio, datos):
	persona = bcValoracionEmpleo.Persona()
	solicitud = bcValoracionEmpleo.Solicitud()

	for dato in datos:
		patributo = persona.getAtributo(dato['atributo'])
		if patributo is not None:
			dato['valor'] = parseaAtributo(patributo, dato['valor'])
			persona.setAtributoSiExiste(dato['atributo'], dato['valor'])


		satributo = solicitud.getAtributo(dato['atributo'])
		if satributo is not None:
			dato['valor'] = parseaAtributo(satributo, dato['valor'])
			solicitud.setAtributoSiExiste(dato['atributo'], dato['valor'])
	dominio = Dominio(persona, solicitud)
	return dominio.execute()

def valorarPrestamo(criterio, datos):
	persona = bcValoracionPrestamos.Persona()
	solicitud = bcValoracionPrestamos.Solicitud()

	print(datos)
	for dato in datos:
		patributo = persona.getAtributo(dato['atributo'])
		if patributo is not None:
			dato['valor'] = parseaAtributo(patributo, dato['valor'])
			persona.setAtributoSiExiste(dato['atributo'], dato['valor'])


		satributo = solicitud.getAtributo(dato['atributo'])
		if satributo is not None:
			dato['valor'] = parseaAtributo(satributo, dato['valor'])
			solicitud.setAtributoSiExiste(dato['atributo'], dato['valor'])

	print('atributos de persona')
	for atributo in persona.atributos:
		print(atributo.nombre, atributo.tipo, atributo.valor)

	print('atributos de solicitud')
	for atributo in solicitud.atributos:
		print(atributo.nombre, atributo.tipo, atributo.valor)
		
	dominio = Dominio(persona, solicitud)
	return dominio.execute()

def parseaAtributo(atributo, dato):
	if atributo is not None:
		if atributo.tipo == 'float':
			dato = float(dato)
		elif atributo.tipo == 'int':
			dato = int(dato)
		elif atributo.tipo == 'array':
			dato = dato.split(',')
		elif atributo.tipo == 'boolean':
			dato = dato == True
	return dato