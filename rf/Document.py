import os

class Document:
    name = None
    title = None
    template = None
    
    def __init__(self):
        pass
    
    def generateDocumentSettings(self):
        return documentSettings.format(self.name)
    
    def generateItem(self, order):
        return item.format(self.name, order)
    
    def generateViewSettings(self):
        return viewSettings.format(self.name)
    
    def generateContent(self):
        content = ""
        
        if self.template:
            template = open(os.path.abspath(self.template), 'r')
            content += template.read()
            template.close()
        if self.title:
            content += "\\section*{{{0}}}".format(self.title)
        
        return content

documentSettings = """[document-settings,item:{0}.tex]
Bookmarks=
Encoding=UTF-8
FoldedColumns=
FoldedLines=
Highlighting=LaTeX
Indentation Mode=
Mode=LaTeX
ReadWrite=true

"""

item = """[item:{0}.tex]
archive=true
column=0
encoding=UTF-8
highlight=LaTeX
line=0
mode=LaTeX
open=true
order={1}

"""


viewSettings = """[view-settings,view=0,item:{0}.tex]
CursorColumn=0
CursorLine=0
JumpList=
ViMarks=

"""