import os
def fibo(a, b, n):
    i=1
    while i<=n:
        t=a
        a=b
        b+=t
        i+=1
    return t

a=int(input("entrer le premier terme: "))
b=int(input("entrer le deuxième terme: "))
n=int(input("entrer le nombre max de calcul: "))
j=1
while j<=n:
    print(j,' ',fibo(a, b, j))
    j+=1
os.system("pause")
