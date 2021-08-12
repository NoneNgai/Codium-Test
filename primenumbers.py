
while True:
    x = int(input("Enter range of number you want to find prime numbers: "))
    if(x>=0):
        break;
    
def prime(n):
    div = 0
    for i in range(1,n+1):
        if(n%i==0):
            div += 1

    if(div==2):
        print(str(n), end=" ")

for i in range(1,x+1):
    prime(i)
