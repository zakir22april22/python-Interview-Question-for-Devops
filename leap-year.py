def Leap_year(year):

    if ((year % 400 == 0)| (year % 100 !=0) & (year % 4 ==0)):
        return True
    else:
        return False

year= int(input('enter your year :'))
print(Leap_year(year))        