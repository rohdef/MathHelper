import sys
import logging
from PyQt4 import QtGui, QtCore
from FileField import FileField

from rf.Document import Document

class DocumentsEdit(QtGui.QWidget):
    __documentTitleField = None
    __documentFileNameField = None
    documents = []
    
    def __init__(self, config):
        super(DocumentsEdit, self).__init__()
        self.__config = config
        
        grid = QtGui.QGridLayout()
        
        grid.addWidget(QtGui.QLabel("Document title"), 0, 0)
        self.__documentTitleField = QtGui.QLineEdit()
        grid.addWidget(self.__documentTitleField, 0, 1)
        
        grid.addWidget(QtGui.QLabel("File name"), 1, 0)
        self.__documentFileNameField = QtGui.QLineEdit()
        grid.addWidget(self.__documentFileNameField, 1, 1)
        
        self.__documentTitleField.textChanged.connect(self.__documentFileNameField.setText)
        
        grid.addWidget(QtGui.QLabel("Template"), 2, 0)
        self.__templateField = FileField("Template")
        grid.addWidget(self.__templateField, 2, 1)
        
        addIcon = QtGui.QIcon.fromTheme("document-new")
        addButton = QtGui.QPushButton(addIcon, 'Add', self)
        addButton.clicked.connect(self.__addDocument)
        grid.addWidget(addButton, 3, 1)
        
        self.__documentList = QtGui.QListWidget(self)
        grid.addWidget(self.__documentList, 4, 0, 1, 2)
        
        self.setLayout(grid)
        self.__loadDocuments()
    
    def __loadDocuments(self):
        options = self.__config.options('documents')
        
        for option in options:
            doc = Document()
            doc.name = self.__config.get(option, 'name')
            doc.title = self.__config.get(option, 'title')
            doc.template = self.__config.get(option, 'template')
            
            self.documents.append(doc)
            self.__documentList.addItem(doc.name)
            
            logging.debug("Loaded document:")
            logging.debug("name: %s", doc.name)
            logging.debug("title: %s", doc.title)
            logging.debug("template: %s", doc.template)
    
    def __addDocument(self, e):
        doc = Document()
        doc.name = str(self.__documentFileNameField.text())
        doc.title = str(self.__documentTitleField.text())
        doc.template = self.__templateField.getPath()
        
        self.documents.append(doc)
        
        self.__documentList.addItem(self.__documentFileNameField.text())