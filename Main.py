from tkinter import *
from tkinter import ttk
import shelve
root=Tk()
#root.title="Folder Management System"
#root.update

root.title('Folder Management System')
Content=ttk.Frame(root)
Folderlbl=ttk.Label(Content, text="Folder: ")

db=shelve.open('FolderDB')
keys=[]
Folder=[]
FolderCombo=[]
for item in db:
    keys.append(item)
    Folder.append(db[item])
    FolderCombo.append(db[item][0].upper() + ' in ' + db[item][1])



Folder = ttk.Combobox(Content)
Folder['values']=FolderCombo
Folder['width']=50

NewButton=ttk.Button(Content,text='New')
ProjectFrame=ttk.Frame(Content)
Projects=StringVar()
ProjectLabel=ttk.Label(ProjectFrame,textvariable=Projects)
Projects.set('Selecte a Folder')







Content.grid(column=0,row=0)
Folderlbl.grid(column=0,row=0, sticky=(N,E),padx=5,pady=5)
Folder.grid(column=1,row=0,rowspan=2,sticky=(N,W),padx=5,pady=5)
NewButton.grid(column=3,row=0,sticky=(N,W),padx=5,pady=3)
ProjectFrame.grid(column=0,row=1,columnspan=4,sticky=N)
ProjectLabel.grid(column=0,row=0,columnspan=4,sticky=N)
Folder.bind('<<ComboboxSelected>>',lambda e: Projects.set(Folder.get()))

