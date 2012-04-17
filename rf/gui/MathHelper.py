import sys
from PyQt4 import QtGui, QtCore

import ConfigParser
import os.path
import logging

from MaximaHelper import MaximaHelper
from KileHelper import KileHelper

class MathHelper(QtGui.QMainWindow):
    def __init__(self):
        super(MathHelper, self).__init__()
        self.initConfig()
        self.initUI()
    
    def initConfig(self):
        self.__path = os.path.expanduser('~/.config/RfMathHelper.cfg')
        self.config = ConfigParser.RawConfigParser()
        
        try:
            self.config.read(self.__path)
        except IOError:
            logging.error("IO error caught")
            pass
        
        logging.info(self.config.get('base', 'projectFolder'))
        
        if not self.config.has_section('base'):
            self.config.add_section('base')
            
            self.config.set('base', 'projectFolder', os.path.expanduser('~'))
            self.config.set('base', 'masterTemplate', '~')
        
        if not self.config.has_section('documents'):
            self.config.add_section('documents')
    
    def initUI(self):
        self.setGeometry(100, 100, 450, 350)
        self.setWindowTitle("Kile project creator")
        
        self.initTabBar()
        
        self.show()
        
    def initTabBar(self):
        tabBar = QtGui.QTabWidget()
        
        tabBar.addTab(KileHelper(self.config), "Kile helper")
        tabBar.addTab(MaximaHelper(self.config), "Maxima helper")
        
        self.setCentralWidget(tabBar)
    
    def closeEvent(self, e):
        with open(self.__path, 'w') as configFile:
            self.config.write(configFile)

def main():
    app = QtGui.QApplication(sys.argv)
    mh = MathHelper()
    
    sys.exit(app.exec_())