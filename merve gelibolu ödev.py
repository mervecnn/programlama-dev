#1.soru
satisMiktari=500
birimMiktari=20
ciro=5000
i=1
while True:
    satisMiktari=(satisMiktari+200)*12
    birimMiktari=(birimMiktari+10)*12
    ciro=satisMiktari+birimMiktari
    i=i+1
    if(ciro>500000):
        print(i,"yıl sonra cironuz 500000 tl yi geçer.")
        break

#2.soru
stok=10000
i=0
while True:
    stok=stok-500
    stok=stok+100
    i=i+1
    if(stok==0):
        print(i,".ayda stoklar sıfırlanır.")
        break


#3.soru
i=0
while True:
    a=int(input("bir sayı giriniz.çıkmak için 0'a basınız."))

    if(a==0):
        print("çıkış yaptınız!")
        break
    else:
        i=i+a%3
        print("sayının 3'e bölümünden kalanlar toplamı:",i)


#4.soru
gunlukyevmiye=90
calisansayisi=50
mesaisaati=""
calismasaati=40
while True:
    mesaisaati=int(input("mesai saatinizi giriniz:"))
    if (mesaisaati<22):
        print("aylık mesai ile birlikte ödenecek miktar:",(40*4*90)+(mesaisaati*gunlukyevmiye*0.10)*50)
    else:
        print("22 saatten fazla mesai yapılmaz.")
        break




#5.soru
gunlukurun=200
defolumal=""
toplamdefo=0
i=0
while True:
    defolumal=int(input("Günlük defolu ürün sayısınız giriniz:"))
    toplamdefo=toplamdefo+defolumal
    i=i+1
    print(i,"günlük toplam defolu ürün sayınız:",toplamdefo)
    if(defolumal>(gunlukurun*0.20)):
        print("Defolu ürün sayınız günlük mal üretiminizin %20'nin üzerindedir")
