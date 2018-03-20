##1111111111111111111111111111111111111

def katmaDegerCiroHesapla(a,b,c,d,e):
    f=a-(b+c+d+e)
    if(f>1000):
        print("işletme katma değer cirosu yüksek")
    elif(500<f<999):
        print("işletme katma değer cirosu normal")
    else:
        print("işletme katma değer cirosu düşük")
a=int(input("Toplam Satış Miktarınız:"))
b=int(input("Hammadde Maliyeti:"))
c=int(input("Bakım Onarım Gideriniz:"))
d=int(input("Sevkiyat Gideriniz:"))
e=int(input("Satın Alınan Hizmet Giderleriniz:"))
katmaDegerCiroHesapla(a,b,c,d,e)

##22222222222222222222222222222222

print("Fark:")
def m2016(x,y):
    global z
    z=x/y
    return z
def m2017(a,b):
    global t
    t=a/b
    return t
def musteriFark(t,z):
    w=t-z
    print("2016-2017 Yılları Arası Müşteri Farkı:",w)
    return w
z=int(input("Müşterilerle Çalışma Süresini Hesaplayacanız Yıl:"))
x=int(input("2016/Çalışılan Süre:"))
y=int(input("2016/Toplam Müşteri Sayısı:"))
t=int(input("Müşterilerle Çalışma Süresini Karşılaştıracağınız Yıl:"))
a=int(input("2017/Çalışılan Süre:"))
b=int(input("2017/Toplam Müşteri Sayısı:"))

mCSa=m2016(x,y)
mCSy=m2017(a,b)
mFark=musteriFark(t,z)

	
##333333333333333333333333333333333333333333

def isletmeKari():
    x=int(input("İlk 6 Aylık Yazılım Gelirleriniz Giriniz:"))
    y=int(input("İlk 6 Aylık Finansaman Gelirlerini Giriniz:"))
    z=int(input("İlk 6 Aylık Ürün Satış Gelirlerini Giriniz:"))
    t=x+y+z
    print("İlk 6 Aylık Geliriniz:",t)
    a=int(input("İlk 6 Aylık Çalışan Maaşlarını Giriniz:"))
    b=int(input("İlk 6 Aylık Kira Giderlerini Giriniz:"))
    c=int(input("İlk 6 Aylık Donanım Maliyetlerini Giriniz:"))
    d=a+b+c
    print("İlk 6 Aylık Gideriniz:",d)
    e=t-d
    print("İlk 6 Aylık Karınız:",e)
    f=int(input("Son 6 Aylık Yazılım Gelirlerini Giriniz:"))
    g=int(input("Son 6 Aylık Sponsorluk Gelirlerini Giriniz:"))
    h=int(input("Son 6 Aylık E Ticaret Gelirlerini Giriniz:"))
    k=int(input("Son 6 Aylık Ürün Satış Gelirlerini Giriniz:"))
    l=f+g+h+k
    print("Son 6 Aylık Geliriniz:",l)
    m=int(input("Son 6 Aylık Çalışan Maaşlarını Giriniz:"))
    n=int(input("Son 6 Aylık Kira Giderlerini Giriniz:"))
    p=int(input("Son 6 Aylık Bakım Maliyetlerini Giriniz:"))
    r=m+n+p
    print("Son 6 Aylık Gideriniz:",r)
    o=l-r
    if(o<1000):
        print("İşletmeniz yeterince karda değil:",o)
    elif(1000<o<5000):
        print("İşletmenizin kar derecesi normal:",o)
    else:
        print("İşletmeniz çok karlı:",o)

		
##444444444444444444444444444444444444444444444444444444
	
def ortStok():
    a=100
    b=100
    c=100
    d=a+b+c
    print("Dönembaşı Koltuk Sayısı:",a)
    print("Dönembaşı Yatak Sayısı:",b)
    print("Dönembaşı Dolap Sayısı:",c)
    print("Dönembaşı Stok Miktarı:",d)
    x=10
    y=15
    z=5
    t=x+y+z
    print("Dönemiçi Koltuk Sayısı:",x)
    print("Dönemiçi Yatak Sayısı:",y)
    print("Dönemiçi Dolap Sayısı:",z)
    print("Dönemiçi Stok Miktarı:",t)
    e=25
    f=20
    g=10
    h=e+f+g
    print("Dönemsonu Koltuk Sayısı:",e)
    print("Dönemsonu Yatak Sayısı:",f)
    print("Dönemsonu Dolap Sayısı:",g)
    print("Dönemsonu Stok Miktarı:",h)
    o=(d+h)/2
    print("Ortalama Stok Değeri:",o)

