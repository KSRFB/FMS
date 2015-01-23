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


if __name__ == '__main__':
    import datetime
    d=datetime.datetime.now()
    date = timedisplay(d)
