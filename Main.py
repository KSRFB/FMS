from tkinter import *
from tkinter import ttk
from Modules.OtherFunc import GetDesc,GetStructure
import shelve

"""
Main Window root
"""

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
FolderList=[]
FolderCombo=[]
ComboList=StringVar()
for item in db:
    keys.append(item)
    FolderList.append(db[item])
    FolderCombo.append(db[item][0].upper() + ' in ' + db[item][1])

#Edit 'Content1' Combobox
Folder = ttk.Combobox(Content1,values=FolderCombo,width=50)

#Create button to create new Folder
NewButton=ttk.Button(Content1,text='New')

#Create button to edit details
EditButton=ttk.Button(Content1,text='Edit')


#create description Label
Description=StringVar()
Desclbl = ttk.Label(Content1,textvariable=Description,wraplength=300)
Description.set('')

#Create Structure label
Structure=StringVar()
structlbl = ttk.Label(Content1,textvariable=Structure,wraplength=400)
Structure.set('')


#Create second frame 'Content2'
#Content2=ttk.Frame(root)

#create Projects Variable 
#Projects=StringVar()
#ProjectLabel=ttk.Label(Content2,textvariable=Projects)
#Projects.set('')

def Comboboxselected(a,b,c,d):
    Description.set(GetDesc(a,b,c,d))
    Structure.set(GetStructure(a,b,c,d))


#Display
Content1.grid(column=0,row=0)
Folderlbl.grid(column=0,row=0, sticky=(N,E),padx=5,pady=5)
Folder.grid(column=1,row=0,columnspan=2,sticky=(N,W),padx=5,pady=5)
NewButton.grid(column=3,row=0,sticky=(N,W),padx=5,pady=3)
EditButton.grid(column=3,row=1,padx=5,pady=5,columnspan=2,sticky=(N))
Desclbl.grid(column=1,row=1,columnspan=3,sticky=(N,W),padx=5, pady=5)
structlbl.grid(column=1,row=2,columnspan=4,sticky=(N,W),padx=5, pady=5)
#Content2.grid(column=0,row=1,columnspan=4,sticky=N)
#ProjectLabel.grid(column=0,row=0,columnspan=4,sticky=N)
Folder.bind('<<ComboboxSelected>>',lambda e: Comboboxselected(FolderCombo,Folder.get(),keys,FolderList))

root.mainloop()



"""
Secondary Window root2
"""

