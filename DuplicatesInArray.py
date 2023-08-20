def DuplicatesInArray():
    my_Arr=[30,20,30,40,1000,20,70,80,80,1000]
    print('Duplicates element in the given array are :')
    arr_len=len(my_Arr)
    
    for i in range(0,arr_len):
        for j in range(i+1,arr_len):
            if(my_Arr[i]==my_Arr[j]):
                print(my_Arr[j])

DuplicatesInArray()    