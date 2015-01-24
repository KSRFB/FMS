#!OtherFunc

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
    db = shelve.open('MasterFolderdb')
    try:
        db[dir]
    except:
        db[dir]=dir
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
    name='Human Resource'
    path=r'C:\Users\fviallevieille\PythonTest'
    d=datetime.now()
    date = TimeDisplay(d)
    createMF(name,path)
    
