inf=False
try:
    inf=open('pqr.txt','r')
    for line in inf.readlines():
        if not(line.startswith('#')):
               print(line)
except IOERROR as e:
    print(e)
finally:
    if inf:inf.close()
