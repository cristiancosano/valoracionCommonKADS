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

# Objetos de la base del conocimiento


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
		
		self.atMotivo=Atributo('Motivo', 'multiple', None, None, ['Compra de Casa','Cambio Coche','Estudios'])
		self.atCantidad=Atributo('Cantidad', 'int', None)
		self.atTiempoDevolucion=Atributo('Tiempo Devolucion', 'int', None)
		self.valorLimite=Atributo('ValorLimite', 'float', None)       
		#self.atCapacidadMaximaDePago('Capacidad Maxima de Pago', 'float', None) 
		self.atributos=[self.atMotivo,self.atCantidad,self.atTiempoDevolucion]
<<<<<<< HEAD
		self.criterio=Criterios()
		r1 = AbstraerPosibilidadPago('r1')
=======
		self.criterio=Criterios("criterio")
		r1 = AbstraerValorLimite('r1')
>>>>>>> 9d7eadc0c64401903baaa0dedeb0b4f91b42bb0f
		self.reglas=[r1]

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
		self.atPatrimonio=Atributo('Patrimonio','float',None)
		self.atPatrimonioAvalistas=Atributo('Patrimonio Avalistas','float',None)
		self.atSituacionLaboral=Atributo('Situacion Laboral','multiple',None,None,['Parado','Trabajo Temporal','Trabajo Fijo'])
		self.atRiesgo=Atributo('Riesgo','multiple',None,None,['Alto','Medio','Bajo'])
		self.atEdad=Atributo('Edad', 'int', None)
		self.atSolvencia=Atributo('Solvencia','multiple',None,None,['Mucha','Poca','Media'])
		self.atCapacidadEconomica('Capacidad Economica', 'float', None)
		#Se establece la lista de atributos que posee esta clase
		self.atributos=[self.atNombre,self.atApellidos,self.atSueldoAnual,self.atSituacionLaboral]
		r1 = AbstraerSueldoMensual('r1')
		r2 = AbstraerCapacidadEconomica('r2')
		self.reglas=[r1,r2]

# Criterios

class Criterios:
	def __init__(self):
		self.criterios = {
			'RiesgoBajoJoven'	: RiesgoBajoJoven(),
			'RiesgoMedioJoven'	: RiesgoMedioJoven(),
			'RiesgoAltoJoven'	: RiesgoAltoJoven(),
			'RiesgoBajoAdulto'	: RiesgoBajoAdulto(),
			'RiesgoMedioAdulto'	: RiesgoMedioAdulto(),
			'RiesgoAltoAdulto'	: RiesgoAltoAdulto()
		}
	
	def obtenerCriterio(self, persona):
		edad = persona.getAtributoValor('Edad')
		riesgo = persona.getAtributoValor('Riesgo')
		
		return self.criterios['Riesgo'+riesgo.capitalize()+('Joven', 'Adulto')[edad<50]]

class RiesgoBajoJoven(Regla):
	def __init__(self, idRegla):
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		capacidadEconomica = persona.getAtributo('Capacidad Economica')
		valor = 0.0
		valor += capacidadEconomica * 12 * 25  # Persona joven
		valor -= capacidadEconomica * 12 * 0   # Riesgo bajo
		return valor
class RiesgoMedioJoven(Regla):
	def __init__(self, idRegla):
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		capacidadEconomica = persona.getAtributo('Capacidad Economica')
		valor = 0.0
		valor += capacidadEconomica * 12 * 25  # Persona joven
		valor -= capacidadEconomica * 12 * 2.5 # Riesgo medio
		return valor
class RiesgoAltoJoven(Regla):
	def __init__(self, idRegla):
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		capacidadEconomica = persona.getAtributo('Capacidad Economica')
		valor = 0.0
		valor += capacidadEconomica * 12 * 25  # Persona joven
		valor -= capacidadEconomica * 12 * 5   # Riesgo alto
		return valor
class RiesgoBajoAdulto(Regla):
	def __init__(self, idRegla):
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		capacidadEconomica = persona.getAtributo('Capacidad Economica')
		valor = 0.0
		valor += capacidadEconomica * 12 * 10 # Persona adulta
		valor -= capacidadEconomica * 12 * 0  # Riesgo bajo
		return valor	
class RiesgoMedioAdulto(Regla):
	def __init__(self, idRegla):
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		capacidadEconomica = persona.getAtributo('Capacidad Economica')
		valor = 0.0
		valor += capacidadEconomica * 12 * 10   # Persona adulta
		valor -= capacidadEconomica * 12 * 2.5  # Riesgo medio
		return valor
class RiesgoAltoAdulto(Regla):
	def __init__(self, idRegla):
		Regla.__init__(self,idRegla)
	def execute(self, persona, solicitud):
		capacidadEconomica = persona.getAtributo('Capacidad Economica')
		
		valor = 0.0
		valor += capacidadEconomica * 12 * 10 # Persona adulta
		valor -= capacidadEconomica * 12 * 5  # Riesgo alto
		
		return valor

  


# Abstracciones


class AbstraerSueldoMensual(Regla):
	"""
	Regla basica para abstraer el sueldo mensual del solicitante del prestamo
	@param: sueldoMensual
	@return: sueldo medio de la persona al mes
	"""  

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
  

	def execute(self,persona,solicitud):
		sueldoMensual = (persona.getAtributoValor('Sueldo Anual') / 12)
		resultado = persona.setAtributoSiExiste('Sueldo Mensual', sueldoMensual)
		if(resultado is None): 
			persona.atSueldoMensual.valor = sueldoMensual
			persona.atributos.append(persona.atSueldoMensual)

		return persona        
	
class AbstraerCapacidadEconomica(Regla):
	"""
	Obtine el poder económico del solicitante en base a datos proporcionados
	como su patrimonio, sueldo y capacidad de los avalistas
	"""    

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
  

	def execute(self, persona, solicitud): 
		sueldoMensual = persona.getAtributoValor('Sueldo Mensual')
		patrimonio = persona.getAtributoValor('Patrimonio')
		patrimonioAvalistas = persona.getAtributoValor('Patrimonio Avalistas')

		capacidadEconomica = sueldoMensual + ((patrimonio + patrimonioAvalistas) / 240)

		resultado = persona.setAtributoSiExiste('Capacidad Economica', capacidadEconomica)
		if(resultado is None): 
			persona.atCapacidadEconomica.valor = capacidadEconomica
			persona.atributos.append(persona.atCapacidadEconomica)

		return persona
   
class AbstraerValorLimite(Regla):
	"""
	Obtiene el valor mínimo que el solicitante debería tener para poder hacer frente al prestamo.
	"""   	

	def __init__(self,idRegla):
		Regla.__init__(self,idRegla)
		
	def execute(self, persona, solicitud):
		valorLimite = ((solicitud.getAtributoValor('Cantidad') / solicitud.getAtributoValor('Tiempo Devolucion')) / 12)
		penalizaciones = {
			'Compra de Casa': -150,
			'Cambio de Coche': +150,
			'Estudios': -400,
			None: +500,
		}
		valorLimite += penalizaciones.get(solicitud.getAtributorValor('Motivo'))
		# sueldoAnual = persona.getAtributoValor('Sueldo Anual')
		# patrimonio = persona.getAtributoValor('Patrimonio')
		# patrimonioAvalistas = persona.getAtributoValor('Patrimonio Avalistas')
		# edad = persona.getAtributoValor('Edad')
		# perfilRiesgo = persona.getAtributoValor('Riesgo')
		# cantidadPrestamo = solicitud.getAtributoValor('Cantidad')

		# capacidadMensual = (sueldoAnual / 12) + ((patrimonio + patrimonioAvalistas) / 240)

		# capacidadMaximaDePago = 0.0
		# capacidadMaximaDePago += [(capacidadMensual * 12 * 25), (capacidadMensual * 12 * 10)](edad < 50)
		# capacidadMaximaDePago -= [(capacidadMensual * 12 * 10), 0](perfilRiesgo == 'Alto')
		# capacidadMaximaDePago -= [(capacidadMensual * 12 * 5), 0](perfilRiesgo == 'Medio')

		resultado = solicitud.setAtributoSiExiste('Valor Limite', valorLimite)
		if(resultado is None): 
			solicitud.atValorLimite.valor = valorLimite
			solicitud.atributos.append(solicitud.atValorLimite)
		
		return solicitud



