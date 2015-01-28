#!OtherFunc
import os
import shelve

mesa='No Description, please edit'
mesb='No starting characters, please edit'
mesc='No Strucuture, please edit'

def Getdbpath(cblist,value,dblist,folderlist):
    for i in [i for i,x in enumerate(cblist) if x==value]:
        x=i
        dbpath=os.path.join(dblist[x],folderlist[x][0] + 'db')
    return dbpath

def GetData(dbpath):
    db=shelve.open(dbpath)
    d=dict()
    try:
        d['description']=db['description']
    except:
        d['description']=mesa
        
    try:
        d['LET']=db['LET']
    except:
        d['LET']=mesb
        
    try:
        d['structure']=db['structure']
    except:
        d['structure']=mesc
        
    db.close()
    return d


def GetDesc(cblist,value,dblist,folderlist):
    return GetData(Getdbpath(cblist,value,dblist,folderlist))['description']

def GetChar(cblist,value,dblist,folderlist):
    return GetData(Getdbpath(cblist,value,dblist,folderlist))['LET']

def GetStructure(cblist,value,dblist,folderlist):
    lsStruct=GetData(Getdbpath(cblist,value,dblist,folderlist))['structure']
    if lsStruct==mesc:
        txtStruct=mesc
    else:
        txtStruct=''
        for item in lsStruct: txtStruct=txtStruct+item+';'
        txtStruct=txtStruct[:-1]
    return txtStruct

def TimeDisplay(datetime):
    y=str(datetime.year)
    m='0' + str(datetime.month)
    m=m[-2:]
    d=str(datetime.day)
    h='0' + str(datetime.hour)
    h=h[-2:]
    mi='0' + str(datetime.minute)
    mi=mi[-2:]
    s='0' + str(datetime.second)
    s=s[-2:]
    dstring = '%s/%s/%s - %s:%s:%s' %(d,m,y,h,mi,s)
    return dstring


def createMF(name,path):
    name=name.strip()
    dir=os.path.join(path,name)
    db = shelve.open('FolderDB')
    try:
        db[dir]
    except:
        db[dir]=[name,path]
    db.close()

    try:
        os.stat(dir)
    except:
        os.mkdir(dir)
    dir2=os.path.join(dir,name + 'db')
    db2 = shelve.open(dir2)
    try:
        db2['title']
    except:
        title = name.strip()
        db2['title']=title

    try:
        db2['description']
    except:
        desc = input('Description?')
        db2['description']=desc

    try:
        db2['LET']
    except:
        LET=input('Enter the starting characters for your folder (e.g. ENG)').strip().upper()
        a=True
        while a:
            try:
                folder=os.path.join(dir,LET+'0000000000000')
                os.mkdir(folder)
                os.rmdir(folder)
                a = False
            except:
                LET=input(folder + 'A folder cannot be created using these character. Enter other starting characters for your folder (e.g. ENG)').strip().upper()
        db2['LET']= LET
        db2.close()
        
            
    

    
    

if __name__ == '__main__':
    import os
    import shelve
    from datetime import *
    name='Design'
    path=r'C:\Users\fviallevieille\PythonTest'
    d=datetime.now()
    date = TimeDisplay(d)
    createMF(name,path)
    print(GetPath(['a','b'],'b',['path1','path2']))
