from tkinter import *
from tkinter import ttk
import shelve


#Create and Edit Window
root=Tk()
root.title('Folder Management System')


#Create first Frame 'Content1'
Content1=ttk.Frame(root)

#Edit 'Content1' Label
Folderlbl=ttk.Label(Content1, text="Folder: ")



#Fetch 'Content 1' Combobox Content
db=shelve.open('FolderDB')
keys=[]
Folder=[]
FolderCombo=[]
ComboList=StringVar()
for item in db:
    keys.append(item)
    Folder.append(db[item])
    FolderCombo.append(db[item][0].upper() + ' in ' + db[item][1])

ComboList.set(FolderCombo)

#Edit 'Content1' Combobox
Folder = ttk.Combobox(Content1)
Folder['width']=50
Folder['values']= FolderCombo



#Create button to create new Folder
NewButton=ttk.Button(Content1,text='New')

#Create Description Label

#Create second frame 'Content2'

Content2=ttk.Frame(root)

#create Projects Variable 
Projects=StringVar()
ProjectLabel=ttk.Label(Content2,textvariable=Projects)
Projects.set('Selecte a Folder')







Content1.grid(column=0,row=0)
Folderlbl.grid(column=0,row=0, sticky=(N,E),padx=5,pady=5)
Folder.grid(column=1,row=0,rowspan=2,sticky=(N,W),padx=5,pady=5)
NewButton.grid(column=3,row=0,sticky=(N,W),padx=5,pady=3)
Content2.grid(column=0,row=1,columnspan=4,sticky=N)
ProjectLabel.grid(column=0,row=0,columnspan=4,sticky=N)
Folder.bind('<<ComboboxSelected>>',lambda e: Projects.set(Folder.get()))

