#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: ckModValoracion.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''

class Dominio:
    def __init__(self, persona, solicitud): 
        self.persona            = persona
        self.solicitud          = solicitud
        self.criterio           = None
        self.decision           = None
        self.valor              = None
        self.personaAbstraida   = None
        self.solicitudAbstraida = None
        self.valorLimite        = None

	
	def execute(self):
         self.personaAbstraida, self.solicitudAbstraida = Abstraer(self.persona,self.solicitud).execute()
         self.criterio, self.valorLimite                = Seleccionar(self.solicitudAbstraida).execute()
         self.valor, self.solicitudAbstraida            = Evaluar(self.criterio,self.personaAbstraida,self.solicitudAbstraida).execute()
         self.decision, self.solicitudAbstraida         = Equiparar(self.valorLimite,self.valor,self.solicitudAbstraida).execute()
         
         return self.decision, self.solicitudAbstraida.descripcion

class Inferencia:
    def __init__(self):
        pass
    def execute(self):
        pass

class Abstraer(Inferencia):
    def __init__(self, persona, solicitud):
        super().__init__(self)
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
    def __init__(self, solicitud):
	    super().__init__(self)
	    self.solicitud=solicitud
	
    def execute(self):
        
        criterio    =   self.solicitud.criterio
        atributos   =   self.solicitud.atributos
        
        for atributo in atributos:
            if atributo.nombre == 'ValorLimite':
                valorLimite = atributo.valor
                       
        return criterio, valorLimite

class Evaluar(Inferencia):
    """
	Inferencia encargada de seleccionar obtener el valor asignado a la persona en funcion del criterio anteriormente seleccionado
	"""	
    def __init__(self, criterio,persona,solicitud):
	    super().__init__(self)
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
        self.solicitud.descripcion += 'El valor es '+ ('mayor', 'menor')[decision]+' que '+ str(self.valorLimite) + ' por tanto se'+('acepta', 'deniega')[decision]+'\n'
        return decision, self.solicitud
    pass
