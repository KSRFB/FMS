#FolderGUI.py

from tkinter import *
from tkinter import ttk
import os
from OtherFunc import *

class FolderGUI:
    

    def __init__(self,**kargs):
        FolderGUI=Tk()
        if ('name' in kargs.keys() and 'path' in kargs.keys()):
            FolderGUI.title('Folder Edit')
            name=kargs['name']
            path=kargs['path']
            dbpath=os.path.join(path,name,name + 'db')
            try:
                dic=GetData(dbpath)
            except:
                dic={'LET':'', 'description':'','structure':''}
            
            print(dic)
            
        else:
            FolderGUI.title('New Folder Creation')


    #def Edit(self,name,path):
            



if __name__=='__main__':
    x=FolderGUI(name='Design',path=r'C:\Users\fviallevieille\PythonTest')
