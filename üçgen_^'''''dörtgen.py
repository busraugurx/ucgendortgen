print("HOŞGELDİNİZ<3")

şekil= input("HANGİ ŞEKLİ ÖĞRENMEK İSTİYORSUN? ÜÇGEN Mİ DÖRTGEN Mİ? ")
print("İSTEDİĞİNİZ ŞEKİL ",şekil)


if(şekil == "üçgen"):
    a= float(input("ÜÇGENİN BİRİNCİ KENARINI GİRİNİZ: "))
    b= float(input("ÜÇGENİN İKİNCİ KENARINI GİRİNİZ: "))
    c= float(input("ÜÇGENİN ÜÇÜNCÜ KENARINI GİRİNİZ: "))
    if(abs(a - b)<c and abs(b-c) < a and abs(c-a)<b):
        print("BU BİR ÜÇGEN BELİRTİR.")
        if(a == b or a==c or b==c):
            print("BU BİR İKİZKENAR ÜÇGENDİR ")
        elif( (a != b and b != c and a!=c) and abs(a - b)<c and abs(b-c) < a and abs(c-a)<b ):
            print("BU BİR ÇEŞİTKENAR ÜÇGENDİR")
        elif((a == b == c)and abs(a - b)<c and abs(b-c) < a and abs(c-a)<b):
            print("BU BİR EŞKENAR ÜÇGEN")
    else:
        print("BU BİR ÜÇGEN DEĞİLDİR !")

elif( şekil == "dörtgen"):
    x = float(input("DÖRTGENİN 1. KENARINI GİRİN: "))
    y = float(input("DÖRTGENİN 2. KENARINI GİRİN: "))
    z = float(input("DÖRTGENİN 3. KENARINI GİRİN: "))
    q = float(input("DÖRTGENİN 4. KENARINI GİRİN: "))
    if(x == y == z == q ):
        print("BU BİR KARE BELİRTİR")
    elif((x == y and z == q) or (y == z and x == q) or (x == z and y == q)):
        print("BU BİR DİKDÖRTGEN BELİRTİR")
    else:
        print("BU SIRADAN BİR DÖRTGENDİR")

else:
    print("YANLIŞ GİRİŞ YAPTINIZ.")





