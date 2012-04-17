from Document import Document
import os

class Project:
    name = "Project"
    lastDocument = None
    __masterDocument = None
    __documents = [None]
    
    def __init__(self):
        self.__initMaster()
    
    def __initMaster(self):
        doc = Document()
        doc.name = "master"
        self.setMaster(doc)
    
    def setMaster(self, masterDoc):
        self.__masterDocument = masterDoc
        lastDocument = self.__masterDocument
        self.__documents[0] = masterDoc
    
    def addDocument(self, document):
        self.__documents.append(document)
    
    def generateProjectFile(self):
        masterDoc = self.__masterDocument.name + ".tex"
        projectFile = general.format(self.name, self.lastDocument, masterDoc)
        projectFile += tools
        
        for doc in self.__documents:
            projectFile += doc.generateDocumentSettings()
        
        projectFile += projItem.format(self.name)
        for i in range(0, len(self.__documents)):
            projectFile += self.__documents[i].generateItem(i)
        
        for doc in self.__documents:
            projectFile += doc.generateViewSettings()
        
        return projectFile
    
    def getDocuments(self):
        return self.__documents[1:]
    
    def createMasterDoc(self):
        masterDoc = self.__masterDocument.generateContent()
        
        if len(masterDoc) == 0:
            masterDoc += "\\documentclass[a4paper,10pt]{article}\n"
            masterDoc += "\\usepackage[utf8x]{inputenc}\n\n"
        
        masterDoc += "\\begin{document}\n"
        for doc in self.__documents[1:]:
            masterDoc += "\\include{{{0}}}\n".format(doc.name)
        
        masterDoc += "\\end{document}"
        
        return masterDoc
    
    def createProject(self, parentFolder):
        absParent = os.path.abspath(parentFolder)
        projectDir = str(absParent+"/"+self.name)
        
        os.makedirs(projectDir)
        
        projectFile = open(projectDir+"/"+self.name+".kilepr", 'w')
        projectFile.write(self.generateProjectFile())
        projectFile.close()
        
        masterDoc = self.__masterDocument
        docFile = open(projectDir+"/"+masterDoc.name+".tex", 'w')
        docFile.write(self.createMasterDoc())
        docFile.close()
        
        for doc in self.__documents[1:]:
            docFile = open(projectDir+"/"+doc.name+".tex", 'w')
            docFile.write(doc.generateContent())
            docFile.close()


general = """[General]
def_graphic_ext=eps
img_extIsRegExp=false
img_extensions=.eps .jpg .jpeg .png .pdf .ps .fig .gif
kileprversion=2
kileversion=2.1.0
lastDocument={1}
masterDocument={2}
name={0}
pkg_extIsRegExp=false
pkg_extensions=.cls .sty .bbx .cbx .lbx
src_extIsRegExp=false
src_extensions=.tex .ltx .latex .dtx .ins

"""

tools = """[Tools]
MakeIndex=
QuickBuild=

"""

projItem = """[item:{0}.kilepr]
archive=true
column=6684777
encoding=
highlight=
line=0
mode=
open=false
order=-1

"""