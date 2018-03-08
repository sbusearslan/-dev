##1. Soru	
def karHesapla():
    x=int(input("Finansman gelirlerini giriniz:"))
    y=int(input("Pazar gelirlerini giriniz:"))
    z=int(input("Kira gelirlerini giriniz:"))
    gelir=x+y+z
    a=int(input("Ücreti giriniz:"))
    b=int(input("Finansman giderlerini giriniz:"))
    c=int(input("Pazar giderlerini giriniz:"))
    d=int(input("Kira giderlerini giriniz:"))
    e=int(input("Muhasebe giderlerini giriniz:"))
    gider=a+b+c+d+e
    kar=gelir-gider
    if (kar>1000):
        print("Şirket kar sağlamıştır.")
    else:
        print("Şirket zarar sağlamıştır.")
    return kar

#2.Soru
def oeeHesapla():
    x=int(input("Planlanmış üretim süresini giriniz:"))
    y=int(input("Plansız duruşu girniz:"))
    a=int(input("Standart çevrim zamanını giriniz:"))
    b=int(input("Üretim miktarını giriniz:"))
    c=int(input("Sağlam ürün miktarını giriniz:"))
    d=int(input("Toplam üretim miktarını giriniz:"))
    oran=1
    kullanilabilirlik=(x-y)/x
    if x!=y:
        performans=(a*b)/(x-y)
        kalite=(c/d)
        oee=kullanilabilirlik*performans*kalite*oran
        print("%",oee)
    else:
        print("Üretim süresi ile duruş süresi aynı olamaz.")
    

    


##3.Soru
	
def ciro():
    x=int(input("Satış miktarını giriniz:"))
    y=int(input("Birim satış fiyatını giriniz:"))
    global ciro
    ciro=x*y
    return ciro

def adambasiCiro():
    z=int(input("Toplam çalışan sayısını giriniz:"))
    adambasiCiro=(ciro/z)
    return adambasiCiro
