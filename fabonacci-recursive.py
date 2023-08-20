# series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fabonacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fabonacci(i-2)+fabonacci(i-1)
    
series = int(input('enter your series till you want :'))
if series<=0:
    print('enter positive number :')
else:
    for i in range(0,series):
        print(fabonacci(i))
                
    
    