#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: app.py
Descripcion: Aplicacion
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''

import sys
from PyQt5 import QtWidgets
import ckVstValoracion as view

app = QtWidgets.QApplication(sys.argv) #Create an applitacion
form = view.ValoracionDlg()   #Create a form instance
sys.exit(app.exec_())   #Starts application and wait for events
