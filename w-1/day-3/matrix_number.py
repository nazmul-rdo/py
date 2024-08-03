li = [ [1,2,3,5,6],
       [5,6,7,8,8],
       [9,6,0,0,2],
       [3,2,4,5,0] ]
for x in li:
    print(x)
print("---------")

li = [ [1,2,3,5,6],
       [5,6,7,8,8],
       [9,6,0,0,2],
       [3,2,4,5,0] ]
for x in li:        #ak e kaj. ata shudhu bracket chhara
    for y in x:
        print(y,end=',')
    print()
