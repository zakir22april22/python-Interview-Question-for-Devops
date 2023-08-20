# formula n(n+1)/2

def sum_of_N_Natural_Numbers(params):
    result=params*(params+1)
    result= result/2
    return result

num= int(input('enter you number :'))

if num>0:
    print('sum of n natural numbers is :',sum_of_N_Natural_Numbers(num))
else:
    print('numbers should be positive or greater then 0 :')    