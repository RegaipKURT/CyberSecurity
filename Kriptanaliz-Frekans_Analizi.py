from tkinter import *
import matplotlib.pyplot as plt
import sys
from tkinter import messagebox

"""
Messages encrypted by their ascii sequence numbers.
We are going to create two pieces of dictionary and append our encypted and decrypted
text's letters to these dictionaries. Sozluk dictionary will take any open message from language where
using in encrypting process. Sozluk2 dict will take the crypted message. Then we will take 
it and visualize with matplotlib pyplot libraries. Finally, after the save graphics 
we can compare both of these graphics and discover shifting. If we want, 
we can do a reverse shifting process and we can encrypt the message.
WE DID NOT EXPLAIN THE ENCRYPTING PROCESS. ONLY GRAPHIC VISUALITAION FOR COMPREHENSION TO ALGORITM.
"""

"""
Program gizli metin için ve verilen örnek dil için harf frekanslarının grafiğini
oluşturacak. Biz de grafiklere bakarak kaç adet kaydırma yapıldığını görebileceğiz.
Grafikler programın bulunduğu dizine kaydedilecektir.

Örnek mesajlar ascii sıra numaralarına göre şifrelenmiştir. İki adet sözlük kullanarak şifrelemede
kullanılan dilde bir yazı göndereceğiz. Bu şifrelenmemiş metnin içindeki harfler sozluk isimli
sözlüğe atılacak. Ardından şifreli mesajı sozluk2'ye yollayacağız ve her iki yazının da grafiğini alıp
kaydettikten sonra açık metinden gizli metne geçiş yapılırken ne kadar kaydırma yapıldığını
böylece grafik üzerinden görebileceğiz.
ŞİFRELEME VE ÇÖZME İŞLEMİNİ YAPMADIK. BUNUN İÇİN İNTERNETTE ÖRNEK KODLAR BOLCA BULUNABİLİR.
SADECE GRAFİK İŞLEME VE GÖRSELLEŞTİRME İLE ŞİFRE ÇÖZME İŞLEMLERİNİ KAVRAMAYA ÇALIŞTIK.
"""

#açık mesaj dışardan alınabilir. sonuç değişmeyecektir. çünkü bir dildeki harf kullanım sıklığı 
#bütün metinlerde aşağı yukarı aynıdır. her halükarda kaydırma belli olacaktır. 
#önemli olan gizli mesajın harf kullanım sıklığını gösterecek kadar uzun olmasıdır.
# bu uzunluk ise yaklaşık olarak bir paragraf bir yazıya denk uzunluktur. Hatta daha kısa da olabilir.

#dmniogvŢrxjĴumrpùyf}vqyrĴxĢvudmiznygjevdĢl  (bu gizli yazı) (ENCRYPTED MESSAGE)
#ajkfldsşougırjomövczsnvoıuğsrajfwkvdgbsaği  (bu açık yazı)  (DECRYPTED MESSAGE)


sozluk={"a":0,"b":0,"c":0,"ç":0,"d":0,"e":0,"f":0,"g":0,"ğ":0,"h":0,"ı":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"ö":0,"p":0,"r":0,"s":0,"ş":0,"t":0,"u":0,"ü":0,"v":0,"w":0,"x":0,"y":0,"z":0}
sozluk2={"a":0,"b":0,"c":0,"ç":0,"d":0,"e":0,"f":0,"g":0,"ğ":0,"h":0,"ı":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"ö":0,"p":0,"r":0,"s":0,"ş":0,"t":0,"u":0,"ü":0,"v":0,"w":0,"x":0,"y":0,"z":0}

def olustur():
    global metin
    metin=acikentry.get(0.0, END).lower()
    global metin2
    metin2=sifrelientry.get(0.0, END).lower()
    def acik_metin():
        for i in metin:
            if i in sozluk:
                sozluk[i] = sozluk[i] + 1
            else:
                pass
        plt.figure()
        plt.bar(range(len(sozluk)), list(sozluk.values()), align='center')
        plt.xticks(range(len(sozluk)), list(sozluk.keys()))
        plt.ylabel('Harf Sayısı')
        plt.xlabel('Harfler')
        plt.title('Açık Metin Harf Frekansı Grafiği')
        #plt.show()
        plt.savefig("Acik_Metin_Grafik.png")
        
    def gizli_metin():
        for i in metin2:
            if i in sozluk2:
                sozluk2[i] = sozluk2[i] + 1
            else:
                pass
        plt.figure()
        plt.bar(range(len(sozluk2)), list(sozluk2.values()), align='center')
        plt.xticks(range(len(sozluk2)), list(sozluk2.keys()))
        plt.ylabel('Harf Sayısı')
        plt.xlabel('Harfler')
        plt.title('Şifreli Metin Harf Frekansı Grafiği')
        #plt.show()
        plt.savefig("Gizli_Metin_Grafik.png")
        
    
    try:
        acik_metin(), gizli_metin()
        messagebox.showinfo("Başarılı!", "Grafikler başarıyla kaydedildi.")
    except Exception as e:
        messagebox.showerror("HATA!", "Bir hata oluştu!")

pencere = Tk()
pencere.title("Sezar Şifre Kırma")
pencere.geometry("400x450")

sifrelilabel = Label(pencere,text="Şifreli Metin:")
sifrelilabel.pack()
sifrelientry = Text(pencere,width=40,height=10)
sifrelientry.pack()

aciklabel=Label(pencere,text="Açık Dilde Metin Örneği:")
aciklabel.pack()
acikentry = Text(pencere,width=40,height=10)
acikentry.pack()

coz = Button(pencere,text="Grafikleri Oluştur")
coz.config(command=olustur)
coz.pack()

mainloop()
sys.exit(0)