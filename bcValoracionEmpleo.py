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
        
        self.titulacion = Atributo('Titulacion', 'array', None, None, None)
        self.puestosOcupados = Atributo('Puestos ocupados', 'array', None, None, None)
        self.anyosExperiencia = Atributo('Anyos de experiencia', 'int', None)
        self.disponibilidadVehiculoPropio = Atributo('Disponibilidad vehiculo propio', 'boolean', None )
        self.disponibilidadViajar = Atributo('Disponibilidad para viajar', 'boolean', None )
        self.perfilEmpleado = Atributo('Perfil empleado', 'str', None)
        self.puntuacionExito = Atributo('Puntuacion exito', 'int', None)
        self.atributos = [self.titulacion, self.puestosOcupados, self.anyosExperiencia, self.disponibilidadVehiculoPropio, self.disponibilidadViajar]
        r1 = AbstraerPerfilEmpleado('r1')
        r2 = AbstraerPuntuacionExito('r2')
        self.reglas=[r1,r2]
        

class Solicitud(Clase):
    def __init__(self, nombre='Solicitud'):
        Clase.__init__(self, nombre=nombre)
        
        self.atTipoEmpleo = Atributo('Tipo de empleo', 'multiple', None, None, ['Nacional', 'Internacional'] )
        self.perfilEmpleado = Atributo('Perfil del empleado', 'multiple', None, None, ['Junior', 'MidLevel', 'Senior'])
        self.valorLimite = Atributo('Valor limite', 'int', None)
        self.criterio=Criterios()
        r1 = AbstraerValorLimite('r1')
        self.reglas=[r1]

        self.atributos = [self.atTipoEmpleo, self.perfilEmpleado]



class Criterios:
    def __init__(self):
        self.criterios = {
            'NacionalJunior': NacionalJunior(1),
            'NacionalMidLevel': NacionalMidLevel(2),
            'NacionalSenior': NacionalSenior(3),
            'InternacionalJunior': NacionalJunior(4),
            'InternacionalMidLevel': NacionalMidLevel(5),
            'InternacionalSenior': NacionalSenior(6),  
        }
    
    def obtenerCriterio(self, criterio):
        #perfilEmpleado = persona.getAtributoValor('Perfil empleado')
        #disponibilidadViajar = persona.getAtributoValor('Disponibilidad para viajar')
    
        return self.criterios[criterio]


class NacionalJunior(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        perfilPersona = persona.getAtributoValor('Perfil empleado')
        disponibilidadVehiculo = persona.getAtributoValor('Disponibilidad vehiculo propio')
        
        if perfilPersona == 'Junior': valor = 30
        elif perfilPersona == 'MidLevel': valor = 20
        elif perfilPersona == 'Senior': valor = 10
        
        if disponibilidadVehiculo == True: valor+= 5
        valor+= persona.getAtributoValor('Puntuacion exito')
        
        return valor, solicitud

class NacionalMidLevel(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        perfilPersona = persona.getAtributoValor('Perfil empleado')
        disponibilidadVehiculo = persona.getAtributoValor('Disponibilidad vehiculo propio')


        if perfilPersona == 'Junior': valor = 20
        elif perfilPersona == 'MidLevel': valor = 30
        elif perfilPersona == 'Senior': valor = 10
        
        if disponibilidadVehiculo == True: valor+= 5
        valor+= persona.getAtributoValor('Puntuacion exito')


        return valor, solicitud

class NacionalSenior(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        perfilPersona = persona.getAtributoValor('Perfil empleado')
        disponibilidadVehiculo = persona.getAtributoValor('Disponibilidad vehiculo propio')


        if perfilPersona == 'Junior': valor = 10
        elif perfilPersona == 'MidLevel': valor = 20
        elif perfilPersona == 'Senior': valor = 30
        
        if disponibilidadVehiculo == True: valor+= 5
        valor+= persona.getAtributoValor('Puntuacion exito')
        
        
        return valor, solicitud

class InternacionalJunior(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        perfilPersona = persona.getAtributoValor('Perfil empleado')
        disponibilidadViajar = persona.getAtributoValor('Disponibilidad para viajar')

        if perfilPersona == 'Junior': valor = 30
        elif perfilPersona == 'MidLevel': valor = 20
        elif perfilPersona == 'Senior': valor = 10
        
        if disponibilidadViajar == True: valor+= 5
        
        valor+= persona.getAtributoValor('Puntuacion exito')

        
        return valor, solicitud

class InternacionalMidLevel(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        perfilPersona = persona.getAtributoValor('Perfil empleado')
        disponibilidadViajar = persona.getAtributoValor('Disponibilidad para viajar')
        if perfilPersona == 'Junior': valor = 20
        elif perfilPersona == 'MidLevel': valor = 30
        elif perfilPersona == 'Senior': valor = 10
        
        if disponibilidadViajar == True: valor+= 5
        
        valor+= persona.getAtributoValor('Puntuacion exito')
        
        return valor, solicitud

class InternacionalSenior(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    def execute(self, persona, solicitud):
        perfilPersona = persona.getAtributoValor('Perfil empleado')
        disponibilidadViajar = persona.getAtributoValor('Disponibilidad para viajar')

        if perfilPersona == 'Junior': valor = 10
        elif perfilPersona == 'MidLevel': valor = 20
        elif perfilPersona == 'Senior': valor = 30
        
        if disponibilidadViajar == True: valor+= 5
        valor+= persona.getAtributoValor('Puntuacion exito')


        return valor, solicitud
    

class AbstraerPerfilEmpleado(Regla):

    def execute(self, persona, solicitud):
        def __init__(self, idRegla):
            Regla.__init__(self, idRegla)
        
        perfilEmpleado = None
        anyosExperiencia = persona.getAtributoValor('Anyos de experiencia')
        
        if anyosExperiencia >= 5: perfilEmpleado = 'Senior'
        if anyosExperiencia >=3 and anyosExperiencia <5: perfilEmpleado = 'MidLevel'
        if anyosExperiencia <3: perfilEmpleado = 'Junior'
        

        resultado = persona.setAtributoSiExiste('Perfil empleado', perfilEmpleado)
        
        if resultado is None: 
            persona.perfilEmpleado.valor = perfilEmpleado
            persona.atributos.append(persona.perfilEmpleado)
        
        return persona
    
                

class AbstraerPuntuacionExito(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    
    def execute(self, persona, solicitud):
        puntuacionExito = 0
        puestosOcupados = persona.getAtributoValor('Puestos ocupados')
        anyosExperiencia = persona.getAtributoValor('Anyos de experiencia')
        titulaciones = persona.getAtributoValor('Titulacion')

        
        if len(puestosOcupados) >= 5: puntuacionExito = 4
        elif len(puestosOcupados) <= 3: puntuacionExito = 2
        if anyosExperiencia >= 3: puntuacionExito+= 4
        elif anyosExperiencia < 3: puntuacionExito+= 2
        if len(titulaciones) > 2: puntuacionExito+= 2

        
        resultado = persona.setAtributoSiExiste('Puntuacion exito', puntuacionExito)
        
        if resultado is None: 
            persona.puntuacionExito.valor = puntuacionExito
            persona.atributos.append(persona.puntuacionExito)
        
        return persona
    
    
class AbstraerValorLimite(Regla):
    def __init__(self, idRegla):
        Regla.__init__(self, idRegla)
    
    def execute(self, persona, solicitud):
        valorLimite = 0
        tipoEmpleo = solicitud.getAtributoValor('Tipo de empleo')
        perfilEmpleo = solicitud.getAtributoValor('Perfil del empleado')
    
        if  tipoEmpleo == 'Nacional' and perfilEmpleo == 'Junior': valorLimite = 30
        elif  tipoEmpleo == 'Nacional' and perfilEmpleo == 'MidLevel': valorLimite = 35
        elif  tipoEmpleo == 'Nacional' and perfilEmpleo == 'Senior': valorLimite = 40
        
        elif  tipoEmpleo == 'Internacinal' and perfilEmpleo == 'Junior': valorLimite = 30
        elif  tipoEmpleo == 'Internacional' and perfilEmpleo == 'MidLevel': valorLimite = 35
        elif  tipoEmpleo == 'Internacional' and perfilEmpleo == 'Senior': valorLimite = 40
        
                
        resultado = solicitud.setAtributoSiExiste('Valor limite', valorLimite)
        
        if resultado is None: 
            solicitud.valorLimite.valor = valorLimite
            solicitud.atributos.append(solicitud.valorLimite)
        
        return solicitud
    
    


    
    
