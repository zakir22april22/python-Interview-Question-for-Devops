def string_Length(mystring):
    len_count=0
    for i in mystring:
        len_count = len_count+1
    return len_count

mystring = input('enter you strinh :')

# deriver code
str_len=string_Length(mystring)
print('the length of the given string is :',str_len)