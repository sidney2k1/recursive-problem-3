def Hanoi(n,a,b,c):
    if n==1:
        print("Move disc 1 from rod",a,"to",b)
        return
    Hanoi(n-1,a,c,b)
    print("Move disc",n,"from",a,"to",b)
    Hanoi(n-1,c,b,a)
n=5
Hanoi(n,"A","B","C")