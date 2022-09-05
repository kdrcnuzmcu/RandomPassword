import random

hL="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lL="abcdefghijklmnopqrstuvwxyz"
n="1234567890"
s="+-*/!?-_()%&.,"

def ParolaOlustur(uzunluk):
    parola=""
    for i in range(int(uzunluk)):
        x=random.randint(1,4)
        if x==1:
            parola+=random.choice(hL)
        elif x==2:
            parola+=random.choice(lL)
        elif x==3:
            parola+=random.choice(n)
        elif x==4:
            parola+=random.choice(s)
    return parola

print("Parolanız:",ParolaOlustur(12))