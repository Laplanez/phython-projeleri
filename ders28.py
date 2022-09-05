#sayı tahmin oyunu
from random import randint
Oyun = True
while Oyun:
    hak = 6
    random = randint(1,100)
    while True:
        tahmin = int(input("Tahmininiz(1-100): "))
        if tahmin == random:
            print("Tebrikler Kazandınız!")
            break
        else:
            if hak == 0:
                print("Kaybettiniz")
                print("Doğru Cevap {} idi.".format(random))
                break
            if random > tahmin:
                print("Sayı Yukarıda")
            else: print("Sayı Aşağıda")
            hak -= 1
            print("Kalan Hakkınız: {}".format(hak))

    bir_daha = input("Bir daha Oynamak İster Misiniz? (E/H): ")
    if bir_daha == "E" or bir_daha == "e":
        Oyun = True
    if bir_daha == "H" or bir_daha == "h":
        Oyun = False
