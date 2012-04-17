import sys
import os.path
from PyQt4 import QtGui, QtCore

class FileField(QtGui.QWidget):
    __directory = False
    __fileTextField = None
    __name = None
    
    def __init__(self, name, path = '~', directory = False):
        super(FileField, self).__init__()
        
        if not path:
            path = '~'
        
        self.__directory = directory
        self.__name = name
        self.__path = path
        
        self.initUI()
    
    def initUI(self):
        hbox = QtGui.QHBoxLayout()
        
        self.__fileTextField = QtGui.QLineEdit()
        if self.__path != '~':
            self.__fileTextField.setText(self.__path)
        hbox.addWidget(self.__fileTextField)
        
        openIcon = QtGui.QIcon().fromTheme("document-open")
        fileSelectButton = QtGui.QPushButton(openIcon, '', self)
        fileSelectButton.clicked.connect(self.showFileDialog)
        hbox.addWidget(fileSelectButton)
        
        self.setLayout(hbox)
    
    def showFileDialog(self, e):
        if self.__directory:
            self.__fileTextField.setText(QtGui.QFileDialog().getExistingDirectory(self, self.__name, self.__path))
        else:
            self.__fileTextField.setText(QtGui.QFileDialog().getOpenFileName(self, self.__name, self.__path, 'LaTeX files (*.tex)'))
    
    def getPath(self):
        if self.__fileTextField.text() and self.__fileTextField.text() != '~':
            return str(self.__fileTextField.text())
        elif self.__directory:
            return os.path.expanduser('~')
        else:
            return None