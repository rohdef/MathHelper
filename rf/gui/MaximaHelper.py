import sys
from PyQt4 import QtGui, QtCore
import rf.MaximaDataHelper as mh

class MaximaHelper(QtGui.QWidget):
    def __init__(self, config):
        super(MaximaHelper, self).__init__()
        self.initUI()
    
    def initUI(self):
        vbox = QtGui.QVBoxLayout()
        
        vbox.addWidget(QtGui.QLabel("Input data"))
        vbox.addWidget(QtGui.QLabel(" use new line for each list, space between entries"))
        
        self.inputText = QtGui.QTextEdit()
        vbox.addWidget(self.inputText)
        
        buttons = self.initButtons()
        vbox.addWidget(buttons)
        
        self.resultText = QtGui.QTextEdit()
        vbox.addWidget(self.resultText)
        
        self.setLayout(vbox)
    
    def initButtons(self):
        buttons = QtGui.QWidget()
        buttonLayout = QtGui.QHBoxLayout()
        
        listButton = QtGui.QPushButton("Create list")
        listButton.clicked.connect(self.__listButtonSelect)
        buttonLayout.addWidget(listButton)
        
        matrixButton = QtGui.QPushButton("Create matrix")
        matrixButton.clicked.connect(self.__matrixButtonSelect)
        buttonLayout.addWidget(matrixButton)
        
        buttons.setLayout(buttonLayout)
        return buttons
    
    def __matrixButtonSelect(self, e):
        inputStr = str(self.inputText.toPlainText())
        listOfList = mh.parseMatrix(inputStr)
        self.resultText.setPlainText(listOfList)
    
    def __listButtonSelect(self, e):
        inputStr = str(self.inputText.toPlainText())
        listOfList = mh.parseListOfList(inputStr)
        self.resultText.setPlainText(listOfList)