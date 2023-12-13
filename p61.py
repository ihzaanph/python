inf=False
outf=False
try:
    inf=open('inf.txt')
    print("Input File")
    print(inf.read())
    inf.seek(0,0)
    line=inf.readlines()

    outf=open('out.txt','w+')
    outf.writelines(line[0::2])
    outf.seek(0,0)
    print("\nOutput File")
    print(outf.read())
except IOError as e:
    print(e)
finally:
    if inf:inf.close()
    if outf:outf.close()