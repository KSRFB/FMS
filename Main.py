from tkinter import *
from tkinter import ttk
root=Tk()
#root.title="Folder Management System"
root.update
Content=ttk.Frame(root)
Folderlbl=ttk.Label(Content, text="Folder: ")
foldervar=StringVar()
Folder = ttk.Combobox(Content, textvariable=foldervar)
Folder['values']=('Folder1','Folder2','Folder3')
NewButton=ttk.Button(Content,text='New')
ProjectFrame=ttk.Frame(Content)
ProjectLabel=ttk.Label(ProjectFrame,text='Projects')






Content.grid(column=0,row=0)
Folderlbl.grid(column=0,row=0, sticky=(N,E),padx=5,pady=5)
Folder.grid(column=1,row=0,rowspan=2,sticky=(N,W),padx=5,pady=5)
NewButton.grid(column=3,row=0,sticky=(N,W),padx=5,pady=3)
ProjectFrame.grid(column=0,row=1,columnspan=4,sticky=N)
ProjectLabel.grid(column=0,row=0,columnspan=4,sticky=N)


