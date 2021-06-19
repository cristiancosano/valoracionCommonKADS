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
							 QPushButton, QLabel, QLineEdit, QListWidget, QTableWidgetItem,
							 QTextEdit, QHBoxLayout, QVBoxLayout, QFileDialog)

import ckCtrlValoracion as ctrl

class ValoracionDlg(QWidget):
	def __init__(self):
		super(ValoracionDlg, self).__init__()
		self.initUI()
		self.nombreDominio = ''
		self.dominio = None
		self.criterios = None
		
	def initUI(self):
		
		
		#Labels
		self.lblDominio = QLabel('Dominio')
		self.lblCaso = QLabel('Caso')
		self.lblDecision = QLabel('Decision')
		self.lblCriterio = QLabel('Criterio')


		
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
		self.tableWidgetCaso.setColumnWidth(0, 175) #Asignan ancho a las columnas izq
		self.tableWidgetCaso.setColumnWidth(1, 175) #Asignan ancho a las columnas derecha
		self.tableWidgetCaso.setHorizontalHeaderLabels(self.header) #Asigna el header a las columnas

		#Form Inputs
		self.criterioInput = QComboBox()
		self.dominioInput = QComboBox()
		self.dominioInput.addItem('Empleo')
		self.dominioInput.addItem('Prestamos')
		self.setDominio(self)
		self.txtDecision = QTextEdit()
		self.txtDecision.setReadOnly(True)
		
	
		
		
		
		#Grid
		grid = QGridLayout()
		grid.setSpacing(3)


		grid.addWidget(self.lblDominio, 0, 0)
		grid.addWidget(self.dominioInput, 1, 0)

		grid.addWidget(self.lblCriterio, 0, 1)
		grid.addWidget(self.criterioInput, 1, 1)

		grid.addWidget(self.lblDecision, 2, 1)
		grid.addWidget(self.txtDecision, 3, 1)

		grid.addWidget(self.lblCaso, 2, 0)
		grid.addWidget(self.tableWidgetCaso, 3, 0)

		
		
		#Set grid layouts
		mainLayout = QVBoxLayout()
		mainLayout.addLayout(grid)
		mainLayout.addLayout(self.btnsLayout)
		self.setLayout(mainLayout)


		self.setGeometry(300, 300, 1000, 600)
		
		#Set Connections
		self.setConnections()
		
		#Display app
		self.resize(800, 440)
		self.setWindowTitle("Tarea de Valoración")
		self.show()
		
	def setConnections(self):
		self.dominioInput.currentIndexChanged.connect(self.setDominio)
		self.btnSalir.clicked.connect(self.salir)
		self.btnValorar.clicked.connect(self.valorar)
	
	def salir(self):
		sys.exit()

	def setDominio(self, i):
		self.nombreDominio = self.dominioInput.currentText()
		self.dominio = ctrl.obtenerDominio(self.nombreDominio)
		self.setTable()
		self.setCriterios()

	def setCriterios(self):
		self.criterios = self.dominio.Criterios().criterios
		self.criterioInput.clear()
		for criterio in self.criterios.keys():
			self.criterioInput.addItem(criterio)
			
	def setTable(self):
		numrows = self.tableWidgetCaso.rowCount()
		data = self.dominio.Solicitud().atributos + self.dominio.Persona().atributos

		needrows = len(data)
		while numrows != needrows:
			if numrows > needrows:
				self.tableWidgetCaso.removeRow(numrows-1)
			elif(numrows < needrows):
				self.tableWidgetCaso.insertRow(numrows)
			numrows = self.tableWidgetCaso.rowCount()
		for i in range(len(data)):
			self.tableWidgetCaso.setItem(i, 0, QTableWidgetItem(data[i].nombre))
			if (data[i].tipo == 'boolean' or data[i].tipo == 'multiple'):
				cb = QComboBox()
				cb.addItems(data[i].posiblesValores)
				self.tableWidgetCaso.setCellWidget(i, 1, cb)	

			else: self.tableWidgetCaso.setItem(i, 1, QTableWidgetItem(data[i].valor))	
	
	def valorar(self):
		decision = ctrl.valorar()
		self.txtDecision.setText(decision)

if __name__=='__main__':
	app = QtWidgets.QApplication(sys.argv) #Create an applitacion
	form = ValoracionDlg()   #Create a form instance
	sys.exit(app.exec_())    #Starts application and wait for events