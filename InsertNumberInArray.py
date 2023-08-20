# given array (list)

my_arr=[1,2,3,4,5,6]
num = int(input('Enter your number that you want to insert :'))
index = int(input('Enter your index number :'))
len_arr=len(my_arr)

if index >= len(my_arr):
    print('index out of range :')
else:
    my_arr.insert(index,num)

print('array after insertng :',my_arr)        