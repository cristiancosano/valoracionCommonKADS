#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Nombre: ckVstValoracion.py
Descripcion: Base del Conocimiento De Valoración
Asignatura: Ingeniería de Sistemas Software Basados en Conocimiento
Autor: Cristian Cosano Cejas y Antonio Luis Rodriguez Jiménez 
Fecha: 20/06/2021
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout,
                             QPushButton, QLabel, QLineEdit, QListWidget,
                             QTextEdit, QVBoxLayout, QFileDialog)
class ValoracionDlg(QWidget):
    def __init__(self):
        super(ValoracionDlg, self).__init__()
        self.initUI()
        
    def initUI(self):
        
        
        #Labels
        self.labelFolder = QLabel("Folder: ",self)
        self.labelFiles = QLabel("Files: ", self)
        
        #Buttons
        self.buttonBrowse = QPushButton("Browse")
        self.buttonSave = QPushButton("Save")
        self.buttonSaveAs = QPushButton("Save As")
        
        #Form Inputs
        self.folderInput = QLineEdit()
        self.folderInput.setReadOnly(True)
        self.filesInput = QListWidget()
        self.textInput = QTextEdit()
        
        #Grid
        grid = QGridLayout()
        
        #Row 1
        grid.addWidget(self.labelFolder, 0, 0, 1, 1)
        grid.addWidget(self.folderInput, 0, 1, 1, 44)
        grid.addWidget(self.buttonBrowse, 0, 45, 1, 1)
        
        #Row 2
        grid.addWidget(self.labelFiles, 1, 0)
        
        #Row 3
        grid.addWidget(self.filesInput, 2, 0, 1, 1)
        grid.addWidget(self.textInput, 2, 1, 1, 45)
        
        #Row 4
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.addWidget(self.buttonSave)
        self.buttonsLayout.addWidget(self.buttonSaveAs)
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addStretch()
        
        #Set grid layouts
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttonsLayout)
        
        self.setLayout(mainLayout)
        
        #Set Connections
        self.setConnections()
        
        #Display app
        self.resize(800, 450)
        self.setWindowTitle("File Manager")
        self.show()
        
    def setConnections(self):
        self.buttonBrowse.clicked.connect(self.setFolder)
        self.filesInput.itemPressed.connect(self.setText)
        self.buttonSave.clicked.connect(self.saveFile)
        self.buttonSaveAs.clicked.connect(self.saveFileAs)
    
    def setFolder(self):
        folder = QFileDialog.getExistingDirectory()
        if(folder!=''):
            self.folderInput.setText(folder)
            #files = controller.eventSelectFolder(folder)
            self.filesInput.clear()
            #self.filesInput.addItems(files)
    
    def setText(self):
        file = self.folderInput.text()+"/"+self.filesInput.currentItem().text()
        #text = controller.eventSelectFile(file)
        #self.textInput.setText(text)
        
    def saveFile(self):
        if(self.filesInput.currentItem() is None):
            self.saveFileAs()
        else:
            file = self.folderInput.text()+"/"+self.filesInput.currentItem().text()
            text = self.textInput.toPlainText()
            #controller.eventSave(file, text)
        
    def saveFileAs(self):
        file = QFileDialog.getSaveFileName()[0]
        if(file!=''):
            text = self.textInput.toPlainText()
            #controller.eventSave(file, text)
            
            #Get dirname and update folder and files inputs
            #path = os.path.dirname(file)

            
            #self.folderInput.setText(path)
            #files = controller.eventSelectFolder(path)
            self.filesInput.clear()
            #self.filesInput.addItems(files)
            