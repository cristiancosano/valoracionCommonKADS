#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: ckModValoracion.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''

from bcValoracionEmpleo import Persona, Solicitud



class Dominio:
	def __init__(self, persona, solicitud, criterio): 
		self.persona            = persona
		self.solicitud          = solicitud
		self.nombreCriterio 	= criterio
		self.criterio           = None
		self.decision           = None
		self.valor              = None
		self.personaAbstraida   = None
		self.solicitudAbstraida = None
		self.valorLimite        = None
		
		
	def execute(self):
		self.personaAbstraida, self.solicitudAbstraida = Abstraer(self.persona, self.solicitud).execute()
		self.criterio, self.valorLimite                = Seleccionar(self.solicitudAbstraida, self.personaAbstraida, self.nombreCriterio).execute()
		self.valor, self.solicitudAbstraida            = Evaluar(self.criterio, self.personaAbstraida, self.solicitudAbstraida).execute()
		self.decision, self.descripcion                = Equiparar(self.valorLimite, self.valor, self.solicitudAbstraida).execute()
		
		
		return self.decision, self.descripcion

class Inferencia:
	def __init__(self):
		pass
	def execute(self):
		pass

class Abstraer(Inferencia):
	def __init__(self, persona, solicitud):
		Inferencia.__init__(self)
		self.persona = persona
		self.solicitud = solicitud

	def execute(self):
		personaAbstraida    =   self.persona
		solicitudAbstraida  =   self.solicitud
		

		for regla in personaAbstraida.reglas:
			personaAbstraida = regla.execute(personaAbstraida, solicitudAbstraida)

		for regla in solicitudAbstraida.reglas:
			solicitudAbstraida = regla.execute(personaAbstraida, solicitudAbstraida)
		
		return personaAbstraida, solicitudAbstraida

class Seleccionar(Inferencia):
	"""
	Inferencia encargada de seleccionar el criterio y determinar valor limite para la solicitud
	"""
	def __init__(self, solicitud, persona, criterio):
		Inferencia.__init__(self)
		self.solicitud=solicitud
		self.persona=persona
		self.criterio=criterio
	
	def execute(self):
		
		criterio    =   self.solicitud.criterio.obtenerCriterio(self.criterio)
		atributos   =   self.solicitud.atributos

		for atributo in atributos:
			if atributo.nombre == 'Valor limite': valorLimite = atributo.valor
		

		return criterio, valorLimite

class Evaluar(Inferencia):
	"""
	Inferencia encargada de seleccionar obtener el valor asignado a la persona en funcion del criterio anteriormente seleccionado
	"""	
	def __init__(self, criterio,persona,solicitud):
		Inferencia.__init__(self)
		self.criterio   =   criterio
		self.persona    =   persona
		self.solicitud  =   solicitud
	
	def execute(self):
		valor, solicitudAbstraida = self.criterio.execute(self.persona, self.solicitud)
		return valor, solicitudAbstraida

class Equiparar(Inferencia):
	"""
	Inferencia encargada de equiparar el valor limite con el valor obtenido por la persona en la inferencia evaluar
	""" 
	def __init__(self, valorLimite, valor,solicitud):
		Inferencia.__init__(self)
		self.valorLimite    =   valorLimite
		self.valor          =   valor 
		self.solicitud      =   solicitud

	def execute(self):
		decision = self.valorLimite <= self.valor
		descripcion = 'El valor ('+str(self.valor)+') es '+ ('menor', 'mayor')[decision]+' que '+ str(self.valorLimite) + ' por tanto se '+('deniega', 'acepta')[decision]+'\n'
		return decision, descripcion
	pass


if __name__ == "__main__":
	
	persona1 = Persona()
	persona1.setAtributoSiExiste('Titulacion', 'Grado superior informatica')
	persona1.setAtributoSiExiste('Nota media', 9)
	persona1.setAtributoSiExiste('Puestos ocupados', 'Desarrollador Web')
	persona1.setAtributoSiExiste('Anyos de experiencia', 4)
	persona1.setAtributoSiExiste('Disponibilidad vehiculo propio', True)
	persona1.setAtributoSiExiste('Disponibilidad para viajar', True)
		
	
	solicitud1 = Solicitud()
	solicitud1.setAtributoSiExiste('Tipo de empleo', 'Nacional')
	solicitud1.setAtributoSiExiste('Perfil del empleado', 'Junior')
	
	dominio = Dominio(persona1, solicitud1, 'NacionalJunior')
	decision, descripcion = dominio.execute()
	print (descripcion)
		
	
	
	
	
	
	
