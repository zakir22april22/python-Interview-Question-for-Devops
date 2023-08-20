def Reverse_string(my_string):
    reverseString=""
    for i in my_string:
        reverseString=i+reverseString
    return reverseString

my_string= input('enter your string :')

reverse=Reverse_string(my_string)

print('you reverse string is :',reverse)

