#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: bcValoracionPrestamos.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''

from bcValoracion import Clase, Atributo, Regla

class Solicitud(Clase):
	"""
	Clase para la representacion de la solicitud de un prestamo
	@param: Motivo: Compra casa, cambio coche, estudios
	@param: Cantidad: cantidad solcitada
	@param: TiempoDevolucion: tiempo de devolucion del prestamo
	@param: Valor Limite: valor maximo del prestamo.
	"""
		
    
	def __init__(self,nombre=None):
		Clase.__init__(self,nombre=nombre)
        
		self.atMotivo=Atributo('Motivo','multiple',None, None,['Compra de Casa','Cambio Coche','Estudios'])
		self.atCantidad=Atributo('Cantidad','int',None)
		self.atTiempoDevolucion=Atributo('Tiempo Devolucion','int',None)
		self.valorLimite=Atributo('ValorLimite','float',None)        
		self.atributos=[self.atMotivo,self.atCantidad,self.atTiempoDevolucion]
		self.criterio=Criterio("criterio")
		r=AbstraerLimite('r')
		self.reglas=[r]

        


class Persona(Clase):
	"""
	Describe los atributos por los que se caracterizará a una persona solicitante de un prestamo

	@param: Nombre
	@param: Apellidos
	@param: Sueldo Mensual
	@param: Sueldo Anual
	@param: Situacion laboral: parado, trabajo temporal, trabajo fijo.
	@param: Riesgo: alto, medio, bajo
	@param: Solvencia: mucha, poca, media.
	"""
  
	def __init__(self,nombre=None):

		Clase.__init__(self,nombre=nombre)

		self.atNombre=Atributo('Nombre','str',None)
		self.atApellidos=Atributo('Apellidos','str',None)
		self.atSueldoMensual=Atributo('Sueldo Mensual','float', None)
		self.atSueldoAnual=Atributo('Sueldo Anual','float',None)
		self.atSituacionLaboral=Atributo('Situacion Laboral','multiple',None,None,['Parado','Trabajo Temporal','Trabajo Fijo'])
		self.atRiesgo=Atributo('Riesgo','multiple',None,None,['Alto','Medio','Bajo'])
		self.atSolvencia=Atributo('Solvencia','multiple',None,None,['Mucha','Poca','Media'])
		#Se establece la lista de atributos que posee esta clase
		self.atributos=[self.atNombre,self.atApellidos,self.atSueldoAnual,self.atSituacionLaboral]
		r2= AbstraerSolvencia('r2')
		r1= AbstraerSueldoMensual('r1')        
		self.reglas=[r1,r2]


class Criterio(Regla):
	"""
	Requisitos aplicados para valorar la concesion de un prestamo
	@return: valor calculado para ver si es solvente o no.
	"""
  
	def __init__(self,idRegla):
        
		Regla.__init__(self,idRegla)
             
	def execute(self,persona,solicitud):
        
		valor=0.0
            
		if persona.atSolvencia.valor == 'Mucha':
			solicitud.descripcion+='El atributo '+persona.atSolvencia.nombre+' con valor '+persona.atSolvencia.valor+' proporciona 0.7 puntos de valoracion\n'
			valor=valor+0.7
        
		if persona.atSituacionLaboral.valor == 'Trabajo Fijo':
			solicitud.descripcion+='El atributo '+persona.atSituacionLaboral.nombre+' con valor '+persona.atSituacionLaboral.valor+' proporciona 0.4 puntos de valoracion\n'
			valor=valor+0.4
        
		if persona.atSituacionLaboral.valor == 'Trabajo Temporal':
			solicitud.descripcion+='El atributo '+persona.atSituacionLaboral.nombre+' con valor '+persona.atSituacionLaboral.valor+' proporciona 0.2 puntos de valoracion\n'
			valor=valor+0.2
            
		return valor, solicitud

  
    
class AbstraerSueldoMensual(Regla):
	"""
	Regla basica para abstraer el sueldo mensual del solicitante del prestamo
	@param: sueldoAnual
	@return: sueldo de la persona
	"""  

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
  

	def execute(self,persona,solicitud):
		return persona
        
    
class AbstraerCapacidadEconomica(Regla):
	"""
	Obtine el poder económico del solicitante en base a datos proporcionados
    como su patrimonio, sueldo y capacidad de los avalistas
	"""    

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
  

	def execute(self, persona, solicitud):                       
		return persona
   
class AbstraerPosibilidadPago(Regla):
	"""
	Obtiene la cantidad total que el solicitante sería capaz de pagar en función de su capacidad económica,
    perfil de riesgo y edad. 
	"""   	

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
        
	def execute(self,persona,solicitud):
		return solicitud
        
        
