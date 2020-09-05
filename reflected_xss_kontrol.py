"""
Bu araç basit ve deneme/öğrenme amaçlı yazılmış bir araçtır!
Sadece get isteği gönderilen URL'ler üzerinde çalışır!
"""

from termcolor import colored
import requests
import argparse
import sys

uyari = """
Bu aracın bulduğu sonuçlar tam olarak doğru olmayabilir!

Yapı get isteğinde verilen parametrenin geri dönen site içeriğinde 
bulunup bulunmadığına bakarak karar vermek üzerine kurulmuştur.

DWVA uygulamasında çeşitli güvenlik düzeylerinde test edilerek oluşturulmuştur!

Aracı kullanarak doğacak hukuki sorumluluğu kendi üzerinize almış bulunursunuz!
"""

usg = """\npython3 dizinbulucu.py -t 192.168.1.2 -f xss_vectors.txt -c 'cookies'\npython3 dizinbulucu.py -t google.com -f xss_vectors.txt -c 'session=example_session_id'"""

print(colored(uyari, color="red"), colored("\nUsage:" + usg + "\n", color="yellow"))

parser = argparse.ArgumentParser(usage=usg)

parser.add_argument('-t', '--target', help="Target URL", required=True)
parser.add_argument('-f', '--filename', help="XSS Vectors file", required=True)
parser.add_argument("-c", "--cookie", help="Cookies")
args = parser.parse_args()

#http://127.0.0.1/dvwa/vulnerabilities/xss_r/?name=reg&user_token=86c41973894db422311a049dab319b72#

xss = open(args.filename, "r")
target = args.target
xss = xss.read()

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
sayi = 0
for i in xss.splitlines():
    url = target + str(i)
    
    try:
        if i == "":
            continue
        sonuc = requests.get(url, headers=cookie, timeout=2) # 2 saniye zamanaşımı belirledik!
        if i in str(sonuc.content):
        # websitesi içeriğinde gönderdiğimiz değerler varsa muhtemelen XSS açığı bulunuyordur! 
        # hata kodları için: https://www.restapitutorial.com/httpstatuscodes.html
            print("Muhtemel XSS Açığı Bulundu: ", url, sep="\t", end="\t")
            print("Değerler: " + i) 
            sayi += 1
    except requests.exceptions.ConnectTimeout: # zaman aşımı hatası gerçekleşirse
        print("Zamanaşımı Hatası!")
    except requests.exceptions.ConnectionError: 
        print("URL Bulunamadı veya Ulaşılamıyor! ")
        sys.exit(0)

print("Tarama Tamamlandı! {} adet muhtemel XSS açığı bulundu!".format(sayi))



