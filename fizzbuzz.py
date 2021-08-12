#1. Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.
def fizzbuzz(maxnum):
    x = range(1,maxnum+1)
    for i in x:
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz", end = " ")
        elif(i % 3 == 0):
            print("Fizz", end = " ")
        elif(i % 5 == 0):
            print("Buzz", end = " ")
        else: print(i, end = " ")
        if(i%10 ==0):
            print(" ")


fizzbuzz(100)