
# 3. Write a program that produce the following output giving an integer input n.
while True:
    x = int(input("Please input integer number: "))
    if(x>0 and x%1==0):
        break;

# 3.1
def slope(n):
    ran = range(1,n+1)
    sym = ""
    for i in ran:
        sym += "*"
        print(sym)

# 3.2
def slope_re(n):
    sym = [" "]*n
    for i in range(n):
        sym[-i-1] = "*"
        print("".join(sym))

# 3.3
def halfclub(n):
    for i in range(n):
        sym = [" "]*(n+(n-1))
        if(i==0):
            sym[n-(i+1)] = "*"
            print("".join(sym))
        else:
            sym[n-(i+1)] = "*"
            sym[n+(i-1)] = "*"
            print("".join(sym))

# 3.4
def star(n):
    for i in range(n):
        sym = [" "]*n
        sym[i] = "*"
        sym[n-(i+1)] = "*"
        print("".join(sym))

# 3.5
def diamond(n):
    sym = [" "]*n
    cnt = 1
    for i in range(n):
        sym[int(n/2)] = "*"
        if(n%2 != 0): 
            if(i>=0 and i<n/2):
                sym[int(n/2)-i] = "*"
                sym[int(n/2)+i] = "*"
            else:
                sym[i-(int(n/2)+1)] = " "
                sym[n-cnt] = " "
                cnt += 1
        else:
            if(i>= 0 and i<n/2):
                sym[int(n/2)-i] = "*"
                sym[int(n/2)+i] = "*"
            elif(i>n/2):
                sym[i-(int(n/2))] = " "
                sym[n-cnt] = " "
                cnt += 1
        print("".join(sym))

# 3.6
def zoneabcde(n):
    cnt = (n+(n-1))-1
    sym = [" "]+[" "]*((n-1)*2)
    for i in range(n+(n-1)):
        
        if(i==0):
            sym[int(len(sym)/2)] = "+"
            for j in range(int(len(sym)/2)):
                sym[j] = "A"
            for k in range(int(len(sym)/2),len(sym)):
                sym[k] = "B"
        if(i<=int(len(sym)/2)):
            sym[int(len(sym)/2)-i] = "+"
            sym[int(len(sym)/2)+i] = "+"
            for j in range(int(len(sym)/2)-i):
                sym[j] = "A"
            for k in range(int(len(sym)/2)+i+1,len(sym)):
                sym[k] = "B"
        else:
            for j in range(i-n+1):
                sym[j] = "C"
            for k in range(cnt,len(sym)):
                sym[k] = "D"
            cnt -= 1   
            sym[i-int(len(sym)/2)] = "+"
            sym[n-(i+2)] = "+"
        if(i>0 and i<int(len(sym)/2)+1):
            sym[int(len(sym)/2)+i-1] = "E"
            sym[int(len(sym)/2)-i+1] = "E"
        print("".join(sym))

while(True):
    patt = input("Please select pattern you want to show 3.1, 3.2, 3.3, 3.4, 3.5, 3.6 :")
    if patt in ("3.1","3.2","3.3","3.4","3.5","3.6"):
        break

if(patt == "3.1"):
    print("3.1")
    slope(x)
elif(patt == "3.2"):
    print("3.2")
    slope_re(x)
elif(patt == "3.3"):
    print("3.3")
    halfclub(x)
elif(patt == "3.4"):
    print("3.4")
    star(x)
elif(patt == "3.5"):
    print("3.5")
    diamond(x)
elif(patt == "3.6"):
    print("3.6")
    zoneabcde(x)

