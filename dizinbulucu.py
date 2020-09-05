#! /usr/bin/python3
import requests
import argparse

usg = """\npython3 dizinbulucu.py -t 192.168.1.2 -f wordlist.txt -c 'cookies'\nnpython3 dizinbulucu.py -t google.com -f wordlist.txt -c 'session=example_session_id'"""
parser = argparse.ArgumentParser(usage=usg)

parser.add_argument('-t', '--target', help="IP address of target website", required=True)
parser.add_argument('-f', '--filename', help="Wordlist file", required=True)
parser.add_argument("-c", "--cookie", help="Cookies")
args = parser.parse_args()



icerik = open(args.filename, "r")
target = args.target
icerik = icerik.read()

if target.startswith("http://") or target.startswith("https://"):
    pass
else:
    target = "http://" + target

cookie = {"Cookie":""}
if args.cookie != None:
    cookie["Cookie"] = args.cookie


print("-" * 60)
print("Hedef üzerinde tarama gerçekleştiriliyor... \nHedef Adres: ", target)
print("-" * 60)

for i in icerik.splitlines():
    if i.startswith("/"):
        url = target + i 
    else:
        url = target + "/" + i
    try:
        sonuc = requests.get(url, headers=cookie, timeout=2) # 2 saniye zamanaşımı belirledik!
        if "200" in str(sonuc.status_code):
        #Sadece 200 dönen sonuçları göstermek doğru değil başka hata kodları ile de dizinler bulunabilir! 
        # Sadece basit bir örnek yaptığmız için başka hata kodlarını kullanmadık.
        # hata kodları için: https://www.restapitutorial.com/httpstatuscodes.html
            print("Bulundu: ", url) 
    except requests.exceptions.ConnectTimeout: # zaman aşımı hatası gerçekleşirse
        print("URL Bulunamadı veya Ulaşılamıyor! Zamanaşımı Hatası!")

print("Tamamlandı!")