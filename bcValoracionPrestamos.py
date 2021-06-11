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
		#r=AbstraerLimite('r')
		#self.reglas=[r]

        


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
		#self.atSueldoMensual=Atributo('Sueldo Mensual','float', None)
		self.atSueldoAnual=Atributo('Sueldo Anual','float',None)
		self.atPatrimonio=Atributo('Patrimonio','float',None)
		self.atPatrimonioAvalistas=Atributo('Patrimonio Avalistas','float',None)
		self.atSituacionLaboral=Atributo('Situacion Laboral','multiple',None,None,['Parado','Trabajo Temporal','Trabajo Fijo'])
		self.atRiesgo=Atributo('Riesgo','multiple',None,None,['Alto','Medio','Bajo'])
		self.atEdad=Atributo('Edad', 'int', None)
		self.atSolvencia=Atributo('Solvencia','multiple',None,None,['Mucha','Poca','Media'])
		self.atCapacidadEconomica('Capacidad Economica', 'float', None)
		#Se establece la lista de atributos que posee esta clase
		self.atributos=[self.atNombre,self.atApellidos,self.atSueldoAnual,self.atSituacionLaboral]
		#r2= AbstraerSolvencia('r2')
		#r1= AbstraerSueldoMensual('r1')        
		#self.reglas=[r1,r2]
	

class RiesgoBajoJoven(Regla):
	def __init__():
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		valor = 0.0
		return valor

class RiesgoMedioJoven(Regla):
	def __init__():
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		valor = 0.0
		return valor

class RiesgoAltoJoven(Regla):
	def __init__():
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		valor = 0.0
		return valor

class RiesgoBajoAdulto(Regla):
	def __init__():
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		valor = 0.0
		return valor
class RiesgoMedioAdulto(Regla):
	def __init__():
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		valor = 0.0
		return valor
class RiesgoAltoAdulto(Regla):
	def __init__():
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		valor = 0.0
		return valor

class Criterios:
	def __init__():
		self.criterios = {
			'RiesgoBajoJoven'	: RiesgoBajoJoven(),
			'RiesgoMedioJoven'	: RiesgoMedioJoven(),
			'RiesgoAltoJoven'	: RiesgoAltoJoven(),
			'RiesgoBajoAdulto'	: RiesgoBajoAdulto(),
			'RiesgoMedioAdulto'	: RiesgoMedioAdulto(),
			'RiesgoAltoAdulto'	: RiesgoAltoAdulto()
		}
	
	def obtenerCriterio(persona):
		for atributo in persona.atributos
			if(atributo.nombre == 'Edad') 	edad 	= atributo.value
			if(atributo.nombre == 'Riesgo') riesgo 	= atributo.value
		
		return self.criteros['Riesgo'+riesgo.capitalize()+('Joven', 'Adulto')[edad<50]]

class Criterio(Regla):
	"""
	Requisitos aplicados para valorar la concesion de un prestamo
	@return: valor calculado para ver si es solvente o no.
	"""
  
	def __init__(self,idRegla):
        
		Regla.__init__(self,idRegla)
             
	def execute(self,persona,solicitud):
        
		valor=0.0
		return valor, solicitud

  
    
class AbstraerSueldoMensual(Regla):
	"""
	Regla basica para abstraer el sueldo mensual del solicitante del prestamo
	@param: sueldoMensual
	@return: sueldo medio de la persona al mes
	"""  

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
  

	def execute(self,persona,solicitud):
		return persona.atPatrimonio
        
    
class AbstraerCapacidadEconomica(Regla):
	"""
	Obtine el poder económico del solicitante en base a datos proporcionados
    como su patrimonio, sueldo y capacidad de los avalistas
	"""    

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
  

	def execute(self, persona, solicitud): 
		sueldoAnual = persona.getAtributoValor('Sueldo Anual')
		patrimonio = persona.getAtributoValor('Patrimonio')
		patrimonioAvalistas = persona.getAtributoValor('Patrimonio Avalistas')
		cantidadPrestamo = solicitud.getAtributoValor('Cantidad')

		capacidadMensual = (sueldoAnual / 12) + ((patrimonio + patrimonioAvalistas) / 240)
		porcentajeCapacidad = (capacidad / cantidadPrestamo) * 100

		resultado = persona.setAtributoSiExiste('Capacidad Economica', porcentajeCapacidad)
		if(resultado = None): 
			persona.atCapacidadEconomica.valor = porcentajeCapacidad
			persona.atributos.append(atCapacidadEconomica)

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