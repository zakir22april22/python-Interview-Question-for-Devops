# program to add two matrices:-

m1 = [[10,100,230],[40,50,60],[70,80,90]]
m2 = [[90,100,70],[60,50,40],[30,20,10]]

m3 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m1)):
    for j in range(len(m2)):
        m3[i][j] = m1[i][j] + m2[i][j]
        print('i is',i,'j is',j)
        print(m3)
print('final matrix is :') 
for k in m3:
    print(k)   