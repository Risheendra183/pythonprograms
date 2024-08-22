f=open('rishi.txt','r')
c=f.read()
print(c)
f.close()

f=open('rishi.txt','w')
c=f.write("hru\n")
print(c)
f.close()


f=open('rishi.txt','a')
c=f.write("wts u r age")
print(c)
f.close()

f=open('rishi.txt','r')
c=f.read()
print(c)
f.close()
