def leap(year):
    if(year % 400 == 0):
        print(str(year) + " -> true")
    elif(year % 4 == 0 and year % 100 != 0):
        print(str(year) + " -> true")
    else:
        print(str(year) + " -> false")


while(1):
    x = int(input("Check leap year : "))
    if(x>=0):
         leap(x)
    elif(x==-1):
         break;
    else:
         x = int(input("Leap year cannot be negative, please enter new leap year : "))


