#!/usr/bin/python3
"""
Bu program sadece linux icin yazılmıştır.
Çalışmak için yönetici hakları ister.
"""

import os
import sys

#gerekli komutu çalıştırıp tmp içinde sonuc.txt'ye kaydediyoruz.
if str(os.name).startswith("pos"):
	str(os.system("sudo cat /etc/NetworkManager/system-connections/* > /tmp/sonuc.txt"))
else:
	print("Bu program sadece linux işletim sistemi üzerinde çalışmaktadır.")
	sys.exit(0)

#sonuc.txt içinden okuyarak aradığımız değerleri bulup yazdıralım.
with open("/tmp/sonuc.txt", "r") as sonuc_dosyası:
	degerler = sonuc_dosyası.readlines()
	for deger in degerler:
		sonuc = str(deger).strip("=")
		if sonuc[:2] =="id":
			sonucum = sonuc[3:-1] + ": "
			print(sonucum, end="") 
		if sonuc[:3] =="psk":
			print(sonuc[4:-1]) 

#en son kullandığımız geçici dosyayı siliyoruz.
os.system("rm /tmp/sonuc.txt")
