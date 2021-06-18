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
        
        self.titulacion = Atributo('Titulacion', 'multiple', None, None, None)
        self.notaMedia = Atributo('Nota media', 'float', None)
        self.puestosOcupados = Atributo('Puestos ocupados', 'multiple', None, None, None)
        self.anyosExperiencia = Atributo('Anyos de experiencia', 'int', None)
        self.disponibilidadVehiculoPropio = Atributo('Disponibilidad de vehículo propio', 'boolean', None )
        self.disponibilidadViajar = Atributo('Disponibilidad para viajar', 'boolean', None )
        self.pocentajeExito = Atributo('Porcentaje de exito', 'int', None)
        self.perfilEmpleado = Atributo('Perfil empleado', 'str', None)
        self.atributos = [self.titulacion, self.notaMedia, self.puestosOcupados, self.anyosExperiencia, self.disponibilidadVehiculoPropio, self.disponibilidadViajar]
        r1 = AbstraerPerfilEmpleado('r1')
		r2 = AbstraerPorcentajeExito('r2')
		self.reglas=[r1,r2]

class Solicitud(Clase):
    def __init__(self, nombre='Solicitud'):
        Clase.__init__(self, nombre=nombre)
        
        self.atTipoEmpleo = Atributo('Tipo de empleo', 'multiple', None, None, ['Nacional', 'Internacional'] )
        self.perfilEmpleado = Atributo('Perfil del empleado', 'multiple', None, None, ['Junior', 'Mid-Level', 'Senior'])
        self.atributos = [self.atTipoEmpleo, self.perfilEmpleado]



class Criterios:
    def __init__(self):
        self.criterios = {
            'NacionalJunior': NacionalJunior(),
            'NacionalMidLevel': NacionalMidLevel(),
            'NacionalSenior': NacionalSenior(),
            'InternacionalJunior': NacionalJunior(),
            'InternacionalMidLevel': NacionalMidLevel(),
            'InternacionalSenior': NacionalSenior(),  
        }
    
    def obtenerCriterio(persona):
        for atributo in persona.atributos:
            if atributo.nombre == 'Tipo de empleo': tipoEmpleo = atributo.value
            if atributo.nombre == 'Perfil del empleado': perfilEmpleado = atributo.value
    
        return self.criterios[tipoEmpleo+perfilEmpleado]


class NacionalJunior(Regla):
    def __init__():
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        valor = 0.0
        return valor

class NacionalMidLevel(Regla):
    def __init__():
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        valor = 0.0
        return valor

class NacionalSenior(Regla):
    def __init__():
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        valor = 0.0
        return valor

class InternacionalJunior(Regla):
    def __init__():
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        valor = 0.0
        return valor

class InternacionalMidLevel(Regla):
    def __init__():
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        valor = 0.0
        return valor

class InternacionalSenior(Regla):
    def __init__():
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        valor = 0.0
        return valor
    

class AbstraerPerfilEmpleado(Regla):
        def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    
    def execute(self, persona, solicitud):
        perfilEmpleado = None
        anyosExperiencia = persona.getAtributoValor('Anyos de experiencia')
        
        if anyosExperiencia >= 5: pefilEmpleado = 'Senior'
        if anyosExperiencia >=3 && <5: pefilEmpleado = 'Mid-level'
        if anyosExperiencia <3: pefilEmpleado = 'Senior'
        

        resultado = persona.setAtributoSiExiste('Perfil empleado', perfilEmpleado)
        
        if resultado != None: 
            persona.perfilEmpelado.valor = perfilEmpleado
            persona.atributos.append(persona.perfilEmpleado)
        
        return solicitud
    
                

class AbstraerPorcentajeExito(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    
    def execute(self, persona, solicitud):
        porcentajeExito = 0
        puestosOcupados = persona.getAtributoValor('Puestos ocupados')
        anyosExperiencia = persona.getAtributoValor('Anyos de experiencia')
        
        if puestosOcupados >= 5: porcentajeExito = 70
        if puestosOcupados <= 3: porcentajeExito = 40
        if anyosExperiencia >= 3: porcentajeExito+= 20
        if anyosExperiencia < 3: porcentajeExito+= 10
        
        
        resultado = persona.setAtributoSiExiste('Porcentaje de exito', porcentajeExito)
        
        if resultado != None: 
            persona.porcentajeExito.valor = porcentajeExito
            persona.atributos.append(persona.porcentajeExito)
        
        return solicitud

    
    
