l1=[[1,2,3],
    [4,5,5],
    [7,6,8]]
l2=[[55,66,34],
    [47,55,52],
    [75,67,85]]
result=[ [0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(l1)):
    for j in range(len(l1[0])):
        result[i][j]=l1[i][j]+l2[i][j]
for r in result:
    print(result)

