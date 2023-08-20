# collects number make list

def collectsNumber(totalNumbers):
    print('enter your',totalNumbers, 'number :')
    for i in range(0,totalNumbers):
        ele=float(input())
        mylist.append(ele)

# Calcolate average 

def CalculateAverage():
    total=0
    for i in range(0,len(mylist)):
        total=total + mylist[i]
    return (total/totalNumber)
    
mylist=[]    

totalNumber= int(input('Average of how many numbers :?'))
collectsNumber(totalNumber) #calling a function to create a list
Average=CalculateAverage()
print('Average is :',Average)

