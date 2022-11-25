def nameJump(names,marks,updates,n):
    x = [[0 for j in range(3)]for i in range(n)]
    for i in range(n):
        x[i][0]= names[i]
        x[i][1]= marks[i]+updates[i]
        x[i][2]= i+1
    highest = x[0]
    for j in range(1,n):
        if (x[j][1]>= highest[1]):
            highest = x[j]
    print("Name: ",highest[0],", jump: ",
           abs(highest[2]-1),sep="")

names = ["smita","suhel","soni","shruti","kavya"]
marks = [83,78,77,82,85]
updates = [0,5,-9,5,-1]
n = len(marks)
nameJump(names,marks,updates,n)

