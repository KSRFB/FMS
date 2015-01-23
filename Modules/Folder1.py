#! Folder.py

"""
This module includes the Folder and sub-folder classes
"""
import os

class Folder:   
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.dir = os.path.join(path,name)
        self.logfile = os.path.join(self.dir,name + '.log')
        
    def create(self): #Create new project Folder + SubFolders
        try:
            os.stat(self.dir)
        except:
            os.mkdir(self.dir)

    def subfolder(self,file):
         f = open(file,'r')
         lst = f.readlines()
         f.close()

         for folder in lst:
             fold = os.path.join(x.dir,folder.rstrip())
             try:
                 os.mkdir(fold)
             except:
                 continue
                  
    def updateLog(self,text): #Create/update log file
        try:
            f=open(self.logfile,'r')
            logtxt=f.read()
            f.close
        except:
            logtxt=''

        logtxt += (text + '\n')
        g = open(self.logfile,'w')
        g.write(logtxt)
        g.close

        
        


if __name__ == '__main__':
    import os
    x = Folder('ENG0001', r'C:\Users\fviallevieille\PythonTest')
    print('-' * 10)
    print(x.name)
    print(x.path)
    print(x.dir)
    print(x.logfile)
    print('-' * 10)

    x.create()
    x.updateLog('New Log')
    x.updateLog('Second Log')
    file = r'C:\Users\fviallevieille\PythonTest\build.txt'
    x.subfolder(file)
        
    
