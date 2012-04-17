import sys
import os.path
import logging
from PyQt4 import QtGui, QtCore

from FileField import FileField

from rf.Project import Project
from rf.Document import Document
from DocumentsEdit import DocumentsEdit

class KileHelper(QtGui.QWidget):
    def __init__(self, config):
        super(KileHelper, self).__init__()
        self.config = config
        self.initUI()
    
    def initUI(self):
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(QtGui.QLabel("Project options"))
        
        projectWidget = QtGui.QWidget()
        grid = QtGui.QGridLayout()
        
        self.__projectTitleField = QtGui.QLineEdit()
        grid.addWidget(QtGui.QLabel("Project title"), 0, 0)
        grid.addWidget(self.__projectTitleField, 0, 1)
        
        grid.addWidget(QtGui.QLabel("Project folder"), 1, 0)
        self.__projectFolderField = FileField("Project folder", self.config.get('base', 'projectFolder') ,True)
        grid.addWidget(self.__projectFolderField, 1, 1)
        
        grid.addWidget(QtGui.QLabel("Master template"), 2, 0)
        self.__masterTemplateField = FileField("Master template", self.config.get('base', 'masterTemplate'))
        grid.addWidget(self.__masterTemplateField, 2, 1)
        
        projectWidget.setLayout(grid)
        
        vbox.addWidget(projectWidget)
        
        # Add documents
        vbox.addWidget(QtGui.QLabel("Documents"))
        
        self.__documentsEdit = DocumentsEdit(self.config)
        vbox.addWidget(self.__documentsEdit)
        
        vbox.addWidget(self.initOptions())
        
        self.setLayout(vbox)
        self.setWindowTitle("Kile project creator")
        self.show()
    
    def initOptions(self):
        widget = QtGui.QWidget()
        optionsLayout = QtGui.QHBoxLayout()
        
        saveOptionsButton = QtGui.QPushButton('Save settings')
        saveOptionsButton.clicked.connect(self.__saveOptionsClick)
        optionsLayout.addWidget(saveOptionsButton)
        
        generateProjectButton = QtGui.QPushButton('Create project')
        generateProjectButton.clicked.connect(self.__createProject)
        optionsLayout.addWidget(generateProjectButton)
        
        widget.setLayout(optionsLayout)
        return widget
    
    def __saveOptionsClick(self, e):
        self.config.set('base', 'projectFolder', self.__projectFolderField.getPath())
        if self.__masterTemplateField.getPath():
            logging.info("Master template set")
            self.config.set('base', 'masterTemplate', self.__masterTemplateField.getPath())
        
        for doc in self.__documentsEdit.documents:
            if not doc.name:
                continue
            docSection = doc.name.lower()
            if not self.config.has_section(docSection):
                self.config.add_section(docSection)
            
            self.config.set('documents', doc.name)
            self.config.set(docSection, 'name', doc.name)
            self.config.set(docSection, 'title', doc.title)
            self.config.set(docSection, 'template', doc.template)
    
    def __createProject(self, e):
        project = Project()
        project.name = self.__projectTitleField.text()
        
        masterDoc = Document()
        masterDoc.name = 'Master'
        masterDoc.template = str(self.__masterTemplateField.getPath())
        project.setMaster(masterDoc)
        
        for doc in self.__documentsEdit.documents:
            project.addDocument(doc)
        
        project.createProject(str(self.__projectFolderField.getPath()))