#FolderGUI.py

from tkinter import *
from tkinter import ttk
import os
from OtherFunc import *
sys.path.append(r'C:\Users\fviallevieille\FMS')
from Modules.OtherFunc import mesa, mesc, mesb
import sys

class FolderGUI:
    
    def __init__(self,**kargs):
        FolderGUI=Tk()
        frame=ttk.Frame(FolderGUI)
        frame.grid(column=0,row=0)
        if ('name' in kargs.keys() and 'path' in kargs.keys()):
            FolderGUI.title('Folder Edit')
            name=kargs['name']
            path=kargs['path']
            dbpath=os.path.join(path,name,name + 'db')
            try:
                dic=GetData(dbpath)
            except:
                dic={'LET':mesa, 'description':mesb,'structure':mesc}
            print(dic)

            #display Name and path
            Folderlbl=ttk.Label(frame, text=name)
            Folderlbl.grid(column=1,row=0, columnspan=2,sticky=(N,W),padx=10,pady=10)
            Pathlbl=ttk.Label(frame, text=path)
            Pathlbl.grid(column=1,row=1, columnspan=3,sticky=(N,W),padx=10,pady=10)
  
        else:
            FolderGUI.title('New Folder Creation')
            nametxt=StringVar()
            nametxt=ttk.Entry(frame, width=20)
            nametxt.grid(column=1,row=0,columnspan=2, sticky=(N,W),padx=10,pady=10)
            repbutton=ttk.Button(frame, text='...',width=3)
            repbutton.grid(column=1,row=1, sticky=(N,W),padx=10,pady=5)
            repbutton.bind('<Button>',lambda e: self.repfunc(varpath,repbutton,Pathlbl))
            varpath=StringVar()
            varpath.set('')
            Pathlbl=ttk.Label(frame, textvariable=varpath)
            Pathlbl.grid(column=2,row=1, columnspan=3,sticky=(N,W),padx=10,pady=10)
        
        #Create Labels
        Folderlbl=ttk.Label(frame, text="Folder Name:")
        Locationlbl=ttk.Label(frame, text="Folder Location:")
        Descriptionlbl=ttk.Label(frame, text="Folder Description:")
        LETlbl=ttk.Label(frame, text="Project folders start with:")
        Structlbl=ttk.Label(frame, text="Project folders structure:")

        Folderlbl.grid(column=0,row=0, sticky=(N,E),padx=10,pady=10)
        Locationlbl.grid(column=0,row=1, sticky=(N,E),padx=10,pady=10)
        Descriptionlbl.grid(column=0,row=2, sticky=(N,E),padx=10,pady=10)
        LETlbl.grid(column=0,row=3, sticky=(N,E),padx=5,pady=10)
        Structlbl.grid(column=0,row=4, sticky=(N,E),padx=10,pady=10)

        #text boxes for Description, Starting Letters and Structure
        Struct=StringVar()
        Structtxt=Text(frame,wrap=WORD, width=23, height=10)
        Structtxt.grid(column=1,row=4,columnspan=2, sticky=(N,W),padx=10,pady=10)
        
        LET=StringVar()
        LETtxt=ttk.Entry(frame, width=10)
        LETtxt.grid(column=1,row=3, sticky=(N,W),padx=10,pady=10)

        Desc=StringVar()
        Desctxt=Text(frame,wrap=WORD, width=34, height=5)
        Desctxt.grid(column=1,row=2, sticky=(N,W),columnspan=3,padx=10,pady=10)

        #e.g. Labels
        LETexlbl=ttk.Label(frame, text='e.g. ENG, BP, DES, etc.')
        LETexlbl.grid(column=2,row=3, sticky=(N,W),pady=10)        

        Structexlbl=ttk.Label(frame, text='e.g.\nA-FolderA\nB-FolderB\nC-FolderC\nD-FolderD\nF-FolderF\nG-FolderG\netc.')
        Structexlbl.grid(column=3,row=4, sticky=(N,W),pady=10,padx=10)    
            
    def repfunc(self,var1,widgwt1,widgwt2):
        rep = filedialog.askdirectory(title='Choisissez un répertoire')
        var1.set(rep)
        widgwt1.grid(column=3,stick=(N,E))
        widgwt2.grid(column=1)        

if __name__=='__main__':
    sys.path.append(r'C:\Users\fviallevieille\FMS')
    #=FolderGUI(name='Design',path=r'C:\Users\fviallevieille\PythonTest')
    x=FolderGUI()
