111111111111111111111111111111

satisMiktari=500
birimSatisMiktari=20
i=0
while True:
    satisMiktari=satisMiktari+200
    birimSatisMiktari=birimSatisMiktari+10
    ciro=satisMiktari*birimSatisMiktari
    i=i+1
    if(ciro>500000):
        print(i/12,"yıl sonra şirketinizin cirosu 500.000 TL'den fazla olacaktır.",ciro+5000)
        break

222222222222222222222222222222222222


stokMiktari=10000
satisMiktari=500
alisMiktari=100
i=0
while True:
    stokMiktari=stokMiktari-satisMiktari+alisMiktari
    i=i+1
    if (stokMiktari==0):
        print(i,".ay sonunda stoktaki ürün miktarı tükenmiştir.")
        break
		
		
33333333333333333333333333333333333333


a=''
kalan=0
while(a!=0):
    a=int(input("Bir sayı giriniz.Çıkmak için 0'a basınız:"))
    if(a==0):
        print("Çıkış yapıldı.")
    else:
        x=(a%3)
        print("Girdiğiniz sayının 3 ile bölümünden kalan:",x)
        kalan=kalan+x
        print("Girdiğiniz sayının 3 ile bölümünden kalanların toplamı:",kalan)
        
44444444444444444444444444444444444444444


y=2520 #Haftanın 7 günü çalışacaklar.1 ay=4 hafta 4*7*90
x=''
while True:
    x=int(input("1. haftadaki mesai saatiniz:"))
    k=int(input("2. haftadaki mesai saatiniz:"))
    z=int(input("3. haftadaki mesai saatiniz:"))
    t=int(input("4. haftadaki mesai saatiniz:"))
    if (0<(x+k+z+t)<22):
        y=(y+(x+k+z+t)*9*4)*50
        print("Aylık maaşınız",y,"TL'dir.")
    elif((x+k+z+t)==0):
        print("Aylık maaşınız 126.000 TL'dir.")
    else:
        print("Aylık maaşınız hesaplanamaz.")

 
        
55555555555555555555555555555555555555555



pantolon=200
i=0
x=''
while True:
    x=int(input("Günlük defolu ürün sayısını giriniz:"))
    i=i+1
    if(x<200/5):
        print(i,"günlük",x,"defolu ürün bulunuyor.")
    else:
        print("Dikkat!Çok fazla defolu ürün bulunuyor.")
        break  
#üretilen pantolonun %20si 200/5'tir.
