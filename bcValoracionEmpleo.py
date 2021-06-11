#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: bcValoracionEmpleo.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''

from bcValoracion import Clase, Atributo, Regla

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
        self.puestosOcupados = Atributo('Puestos ocupados', 'str', None)
        self.anyosExperiencia = Atributo('Años de experiencia', 'int', None)
        self.disponibilidadVehiculoPropio = Atributo('Disponibilidad de vehículo propio', 'boolean', None )
        self.disponibilidadViajar = Atributo('Disponibilidad para viajar', 'boolean', None )
        self.atributos = [self.titulacion, self.notaMedia, self.puestosOcupados, self.anyosExperiencia, self.disponibilidadVehiculoPropio, self.disponibilidadViajar]
        

class Solicitud(Clase):
    def __init__(self, nombre='Solicitud'):
        Clase.__init__(self, nombre=nombre)
        
        self.atTipoEmpleo = Atributo('Tipo de empleo', 'multiple', None, None, ['Nacional', 'Internacional'] )
        self.perfilEmpleado = Atributo('Perfil del empleado', 'multiple', None, None, ['Junior', 'Mid-Level', 'Senior'])
        self.atributos = [self.atTipoEmpleo, self.perfilEmpleado]
        
class Criterio(Regla):
    def __init__(self, idRegla):
        
        Regla.__init__(self, idRegla)
    
    def execute(self, persona, solicitud):
        valor= 0.0
        for             


class AbstraerPerfilEmpleado(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
        
    def execute(self, persona, solicitud):
        
    
class AbstraerPorcentajeExito(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    
    def execute(self, persona, solicitud):
        

        
    
