'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''

def elemzo(szo1, szo2, szo3):
    lista = [szo1, szo2, szo3] 

    szoveg1 = len(lista[0])
    szoveg2 = len(lista[1])
    szoveg3 = len(lista[2])
    
    if szoveg1 < szoveg2 and szoveg1 < szoveg3:
        return print(f"A kisebb szó: {szo1}")
    elif szoveg2 < szoveg3 and szoveg2 < szoveg1:
        return print(f"A kisebb szó: {szo2}")
    elif szoveg3 < szoveg1 and szoveg3 < szoveg2:
        return print(f"A kisebb szó: {szo3}")
    else:
        return print(f"Az összes szöveg egyenlő hosszú: {szo3}")

bekeres = elemzo(input(" Kérnék egy szót: "),input(" Kérnék még egy szót: "), input(" Kérnék egy utolsó szót: "))