str="risheendra"
j=0;
while j< len(str) :
    
       if str[j]=='d':
             j=j+1;  
             continue;
      
       print(str[j])
       j=j+1;
n=10;
i=0;
s=0;
while i<n:
    s=s+i;
    i=i+1;
print(s);

l=[1,2,3,4]
c=1;
for i in l:
    if i==3:
        print("item matched")
   
        break
    c=c+1;

print("item found ",c,"location")

m=2;

while 1:
    i=1;
    while i<=10:
        print("%d x %d = %d\n"%(m,i,m*i))
        i=i+1;
    cho=input("do you want continue [y/n]")
    if cho=='n' or cho=='N':
          break;
    m=m+1;
    
  
    
    

    
