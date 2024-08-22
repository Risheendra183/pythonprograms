
#dic={'name':'rishi','age':20}
#print(dic['name'])
#print(dic.pop('name'))
#dic.update({'name':'usha'})
#print(dic)
#dic.clear()
#print(dic)

def rishi(a,b):
     return a+b
w=rishi(3,1)
print(w)

def fname(a):
    for i in a:
        print(i)
fname([1,2,4,7,8])
        
def ram(*a):
    print(a)
ram(1,3,6,7,8)

def ram(**a):
    print(a)
ram(name='rishi',age=21)
