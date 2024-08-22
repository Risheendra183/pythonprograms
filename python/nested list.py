r1=[0,0,0]
r2=[0,0,0]
r3=[0,0,0]
print(f"{r1}\n{r2}\n{r3}")
newlist=[r1,r2,r3]
pos=input("enter pos to hide")
a=int(pos[0])
b=int(pos[1])
row_selected=newlist[a-1]
row_selected[b-1]=1
print(f"{r1}\n{r2}\n{r3}")

