#sum  and avg of n numbers
n=input("enter any numbers")
m=n.split()
c=0
for j in m:
    c=c+1
print(c)
for i in range(0,c):
    m[i]=int(m[i])
s=0
for k in m:
    s=s+k
print(f"sum={s}")
avg=s/c
print(f"avg={avg}")
max=m[0]
for h in m:
  if h>max:
      max=h
print(max)

      
