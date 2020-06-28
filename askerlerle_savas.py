import random
import time

class Asker :

    def __init__(self):
        self.ad = "İsimsiz Asker"
        self.can = random.randint(40,70)
        self.saldiri = random.randint(20,40)

    def deg_goster(self):
        print("Askerin ad : {} -- Asker canı : {} -- Asker saldırısı : {}".format(self.ad,self.can,self.saldiri))

    def hasar_al(self,hasar):
        if hasar >= self.can:
            self.ol = True
            self.can = 0
        else:
            self.can = self.can - hasar
            self.ol = False

    def saldir(self):
        return self.saldiri

class Oyuncu :

    def __init__(self,ad):
        self.ad = ad
        self.can = random.randint(320,420)
        self.saldiri = random.randint(40,60)

    def deger_goster(self):
        print("Oyuncunun adı : {} -- Oyuncunun canı : {} -- Oyuncunun saldırısı : {}".format(self.ad, self.can, self.saldiri))

    def hasar_al(self,hasar):
        if hasar >= self.can :
            self.ol = True
            self.can = 0
        else :
            self.can = self.can - hasar
            self.ol = False

    def saldir(self):
        return self.saldiri

asker_liste = []

for i in range(5):
    asker_liste.append(Asker())

isim = input("Oyuncu adı : ")
oyuncu = Oyuncu(isim)

while True :
    if oyuncu.can == 0 :
        print("-------------------------", end="")
        print("Kaybettiniz Oyun Bitti", end="")
        print("-------------------------")
        time.sleep(5)
        exit()

    print("-------------------------------",end="")
    print("Oyuncu Bilgileri",end="")
    print("-------------------------------")
    oyuncu.deger_goster()
    print("-------------------------------", end="")
    print("Askerlerin Bilgileri", end="")
    print("-------------------------------")
    sayac = 1
    for i in asker_liste:
        print("[{}]".format(sayac),end=" ")
        i.deg_goster()
        sayac += 1

    secim = int(input("Saldırmak istediğiniz askerin numarasını girin : "))

    asker_liste[secim - 1].hasar_al(oyuncu.saldir())
    print("-------------------------", end="")
    print("Saldırılan Askerin Bilgileri", end="")
    print("-------------------------")
    asker_liste[secim - 1].deg_goster()
    if asker_liste[secim - 1].ol:
        asker_liste.remove(asker_liste[secim - 1])

    time.sleep(0.1)

    if oyuncu.can == 0 and len(asker_liste) != 0 :
        print("-------------------------", end="")
        print("Kaybettiniz Oyun Bitti", end="")
        print("-------------------------")
        time.sleep(5)
        exit()
    elif oyuncu.can != 0 and len(asker_liste) == 0 :
        print("-------------------------", end="")
        print("Tebrikler Kazandınız", end="")
        print("-------------------------")
        time.sleep(5)
        exit()
    else:
        rast_sayi = random.randint(0, len(asker_liste) )
        oyuncu.hasar_al(asker_liste[rast_sayi-1].saldir())
        rast_sayi = random.randint(0, len(asker_liste) )
        oyuncu.hasar_al(asker_liste[rast_sayi-1].saldir())
        print("-----------------------------------------------")
        print("Paaattt Küüüttt !")
        print("Saldırıya uğradın !")
