#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: bcValoracionEmpleo.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''

from bcValoracion import Clase, Atributo

class Persona(Clase):
    """
	Clase para la representacion de la persona que solicita el empleo
	@param: Motivo: Compra casa, cambio coche, estudios
	@param: Cantidad: cantidad solcitada
	@param: TiempoDevolucion: tiempo de devolucion del prestamo
	@param: Valor Limite: valor maximo del prestamo.
	"""
    
    def __init__(self, nombre='Persona'):
        Clase.__init__(self, nombre=nombre)
        
        self.titulacion = Atributo('Titulacion', 'str', None)
        self.notaMedia = Atributo('Nota media', 'float', None)
        self.puestosOcupados = Atributo('Puesto ocupado', 'str', None)
        self.anyosExperiencia = Atributo('Años de experiencia', 'int', None)
        self.disponibilidadVehiculoPropio = Atributo('Disponibilidad de vehículo propio', 'boolean', None )
        self.disponibilidadViajar = Atributo('Disponibilidad para viajar', 'boolean', None )
        
        

class Solicitud(Clase):
    def __init__(self, nombre=None):
        self.atTipoEmpleo
