def estNbresPremier(num):
    if((num==2)or(num==3)or(num==5)or(num==7)):
        return str(num)+" est un nombre premier"
    elif((num%2==0)or(num%3==0)or(num%5==0)or(num%7==0)):
        return str(num)+" n'est pas un nombre premier"
    else:
        return str(num)+" est un nombre premier"

continuer=True
while continuer:
    max = int(input("entrer le nombre de valaue à vérifier: "))
    print(estNbresPremier(max))
    continuer=bool(input("continuer ? "))
