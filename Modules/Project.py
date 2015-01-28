#! Project.py

"""
This module includes the Folder and sub-folder classes
"""
import os
import subprocess
import datetime
from OtherFunc import TimeDisplay

class Project:   
    def __init__(self,name,path,user,build):
        self.name = name
        self.path = path
        self.dir = os.path.join(path,name)
        self.logfile = os.path.join(self.dir,name + '.log')
        self.user=user
        self.build=build
        
    def open(self): #Create new project Folder (if doesn't exist)
        try:
            os.stat(self.dir)
        except:
            os.mkdir(self.dir)
            self.updateLog('Folder Creation')
            self.subfolder(os.path.join(self.path,self.build))

        self.openProject()

    def subfolder(self,file): #create subfolders
         f = open(file,'r')
         lst = f.readlines()
         f.close()

         for folder in lst:
             fold = os.path.join(x.dir,folder.rstrip())
             try:
                 os.mkdir(fold)
                 os.mkdir(os.path.join(fold,'Archive'))
            
             except:
                 continue
                  
    def updateLog(self,text): #Create/update log file
        try:
            f=open(self.logfile,'r')
            logtxt=f.read()
            f.close
        except:
            logtxt=''
            
        d=datetime.datetime.today()
        logtxt += ('[' + TimeDisplay(d) + '] ' + self.user + ' -> ' + text + '\n')
        g = open(self.logfile,'w')
        g.write(logtxt)
        g.close

    def openProject(self):
        subprocess.call(['explorer',self.dir])

    

        
        


if __name__ == '__main__':
    import os
    x = Project('ENG0001', r'C:\Users\fviallevieille\PythonTest','Fabien Viallevieille','build.txt')
    print('-' * 10)
    print(x.build)
    print(x.name)
    print(x.path)
    print(x.dir)
    print(x.logfile)
    print('-' * 10)

    x.open()
    #x.openFolder()
        
    
