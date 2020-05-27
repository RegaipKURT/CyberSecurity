#!/usr/bin/python3
"""
Bu program sadece linux icin yazılmıştır.
Çalışmak için yönetici hakları ister.
"""
# ÜZERİNDE ÇALIŞACAĞIMIZ LİNUX KONFİGRASYON DOSYASI AŞAĞIDAKİ GİBİ GÖRÜNÜYOR.
# ŞU KOMUTLA ULAŞILABİLİR: sudo cat /etc/NetworkManager/system-connections/*
"""
[wifi]
mac-address-blacklist=
mode=infrastructure
ssid=BAĞLANTININ ADI
[wifi-security]
auth-alg=open
key-mgmt=wpa-psk
psk=PAROLA

[wifi]
mac-address-blacklist=
mode=infrastructure
ssid=BAĞLANTININ ADI
[wifi-security]
key-mgmt=wpa-psk
psk=PAROLA
"""

import os
import sys

#gerekli komutu çalıştırıp tmp içinde sonuc.txt'ye kaydediyoruz.
#tmp dizini geçici dosyaları barındırır. Bilgisayar kapandığında bu dosyalar otomatik silinir.
if str(os.name).startswith("pos"):
	#yaptığımız bütün bağlantıları bir sonuç dosyasına yazdıralım
	str(os.system("sudo cat /etc/NetworkManager/system-connections/* > /tmp/sonuc.txt"))
else:
	print("Bu program sadece linux işletim sistemi üzerinde çalışmaktadır.")
	sys.exit(0)

#sonuc.txt içinden okuyarak aradığımız değerleri bulup yazdıralım.
with open("/tmp/sonuc.txt", "r") as sonuc_dosyası:
	degerler = sonuc_dosyası.readlines()
	#bağlantılar içindeki konfigrasyon ayarlarından şifrelere ve bağlantının adına ait olanları bulalım
	#sonuç dosyasının içindeki satırlarda teker teker ilerleyelim.
	for deger in degerler:
		# "=" işaretine göre ayırıp id ve psk'ya karşılık gelen değerleri bulacağız. 
		sonuc = str(deger).strip("=")
		if sonuc[:2] =="id":
			sonucum = sonuc[3:-1] + ": "
			print(sonucum, end="") 
		if sonuc[:3] =="psk":
			print(sonuc[4:-1]) 

#en son kullandığımız geçici dosyayı siliyoruz.
#silmesek bile bilgisayar yueniden başladığında kendiliğinden silinecek(tmp içinde olduğu için)
os.system("rm /tmp/sonuc.txt")
