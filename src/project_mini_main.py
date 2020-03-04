##________Python3 implemation of of my pmini application________
##
##  core implemation of the mkdir 
##  later split the implemetation into seperate py files for modularity 
## todo;PyQt5 implementation 
import os as os
import sys as sys
import glob as glob
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QDialog, QVBoxLayout

## colors for terminal
class Colors:
    STND = '\033[1;37;40m'
    OUTP = '\033[1;33;40m'
    WARN = '\033[1;31;40m'

##project class
class Project:
    def __init__(self, _path_, _name_):
        self.path = _path_
        self.name = _name_

    def Generate_Working_Dir(self):
        self.c = Colors()
        project_path = ''
        sub_dir = ['_src_','_lib_','_data_','_shots_', '_fin_', '_doc_']
        if(len(self.path) < 1):
            self.path = 'C:/'
        if(len(self.name) > 0):

            project_path = os.path.join(self.path, self.name)
            try:
                os.mkdir(project_path)
                print(self.c.OUTP+"Successfully created project"+self.c.STND)
            except FileExistsError:
                print(self.c.WARN+'Project already exists'+self.c.STND)
            except FileNotFoundError:
                print(self.c.WARN+'Invalid file path'+self.c.STND)
                
    

        if(os.path.exists(project_path)):

            for d in sub_dir:
                try:
                    os.makedirs( os.path.join(project_path, d) )
                    print(self.c.OUTP+"Successfully created folders: "+d+self.c.STND)
                except FileExistsError:
                    print(self.c.WARN+d+' exists'+self.c.STND)
      
## main form dialog
class Form(QDialog):
    
    def __init__(self):
        super(Form, self).__init__(parent=None)

        ##widgets
        self.setWindowTitle('PMINI')
        self._button = QPushButton('Create New Project')
    
        self._edit_project_path = QLineEdit()
        self._edit_project_name = QLineEdit()
        self._edit_project_path.setPlaceholderText('Project path')
        self._edit_project_name.setPlaceholderText('Project name')
        
        ##UI layout 
        layout = QVBoxLayout()    
        layout.addWidget(self._edit_project_path)
        layout.addWidget(self._edit_project_name)
        layout.addWidget(self._button)
        self.setLayout(layout)

        self._button.clicked.connect(self.Generate_Project)

    def Generate_Project(self):
        self._prj_ = Project( self._edit_project_path.text(),  self._edit_project_name.text() )
        self._prj_.Generate_Working_Dir()



_app_ = QApplication([])
form = Form()
form.show()
sys.exit(_app_.exec_())
