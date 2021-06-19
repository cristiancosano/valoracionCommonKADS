#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: ckVstValoracion.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QDialog, QComboBox, QTableWidget, QApplication, QGridLayout,
							 QPushButton, QLabel, QLineEdit, QListWidget,
							 QTextEdit, QHBoxLayout, QVBoxLayout, QFileDialog)

import ckCtrlValoracion as ctrl

class ValoracionDlg(QWidget):
	def __init__(self):
		super(ValoracionDlg, self).__init__()
		self.initUI()
		self.nombreDominio = ''
		self.dominio = None
		
	def initUI(self):
		
		
		#Labels
		self.lblDominio = QLabel('Dominio')
		self.lblCaso = QLabel('Caso')
		#self.labelTipoSolicitud.setAlignment(QtCore.Qt.AlignCenter)

		
		#Buttons
		self.btnValorar = QPushButton("Valorar")
		self.btnSalir = QPushButton("Salir")
		self.btnsLayout = QHBoxLayout()
		self.btnsLayout.addStretch()
		self.btnsLayout.addWidget(self.btnValorar)
		self.btnsLayout.addWidget(self.btnSalir)
		self.btnsLayout.addStretch()

		#Table
		self.header = ['ATRIBUTO', 'VALOR']
		self.tableWidgetCaso = QTableWidget(0,2) #Crea la tabla de elementos observables de dos columnas
		self.tableWidgetCaso.setColumnWidth(0, 225) #Asignan ancho a las columnas izq
		self.tableWidgetCaso.setColumnWidth(1, 225) #Asignan ancho a las columnas derecha
		self.tableWidgetCaso.setHorizontalHeaderLabels(self.header) #Asigna el header a las columnas

		#Form Inputs
		self.dominioInput = QComboBox()
		self.dominioInput.addItem('Empleo')
		self.dominioInput.addItem('Prestamos')
		self.setDominio(self)

		self.txtDecision = QTextEdit()
		
	
		


		#self.folderInput = QLineEdit()
		#self.folderInput.setReadOnly(True)
		#self.filesInput = QListWidget()
		
		
		#Grid
		grid = QGridLayout()
		grid.setSpacing(3)


		grid.addWidget(self.lblDominio, 0, 0)
		grid.addWidget(self.dominioInput, 1, 0)

		grid.addWidget(self.txtDecision, 0, 1)

		grid.addWidget(self.lblCaso, 2, 0)
		grid.addWidget(self.tableWidgetCaso, 0, 2)

		
		
		#Set grid layouts
		mainLayout = QVBoxLayout()
		mainLayout.addLayout(grid)
		mainLayout.addLayout(self.btnsLayout)
		self.setLayout(mainLayout)


		self.setGeometry(300, 300, 1000, 600)
		
		#Set Connections
		self.setConnections()
		
		#Display app
		self.resize(800, 400)
		self.setWindowTitle("Tarea de Valoración")
		self.show()
		
	def setConnections(self):
		self.dominioInput.currentIndexChanged.connect(self.setDominio)
	
	

	def setDominio(self, i):
		self.nombreDominio = self.dominioInput.currentText()
		self.dominio = ctrl.obtenerDominio(self.nombreDominio)
		for atributo in self.dominio.Solicitud().atributos:
			print(atributo.nombre)
		for atributo in self.dominio.Persona().atributos:
			print(atributo.nombre)

		self.setTable()

	def setTable(self):
		numrows = self.tableWidgetCaso.rowCount()
		needrows = len(self.dominio.Solicitud().atributos)+len(self.dominio.Persona().atributos)
		while(numrows != needrows):
			if(numrows > needrows):
				self.tableWidgetCaso.removeRow(numrows-1)
			elif(numrows < needrows):
				self.tableWidgetCaso.insertRow(numrows)
			numrows = self.tableWidgetCaso.rowCount()
		for i in numrows:
			
				

		

	



		
		

if __name__=='__main__':
	app = QtWidgets.QApplication(sys.argv) #Create an applitacion
	form = ValoracionDlg()   #Create a form instance
	sys.exit(app.exec_())   #Starts application and wait for events