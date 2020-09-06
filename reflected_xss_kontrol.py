"""
Bu araç basit ve deneme/öğrenme amaçlı yazılmış bir araçtır!
Sadece get isteği gönderilen URL'ler üzerinde çalışır! 
"""

from termcolor import colored
import requests
import argparse
import sys
from pyfiglet import figlet_format
import time

print(colored(figlet_format("XSS Controller"), color="blue"))
time.sleep(1)

uyari = """
Bu aracın bulduğu sonuçlar tam olarak doğru olmayabilir!

Yapı get isteğinde verilen parametrenin geri dönen site içeriğinde 
bulunup bulunmadığına bakarak karar vermek üzerine kurulmuştur.

DWVA uygulamasında çeşitli güvenlik düzeylerinde test edilerek oluşturulmuştur!

Aracı kullanarak doğacak hukuki sorumluluğu kendi üzerinize almış bulunursunuz!
"""

usg = """\npython3 reflected_xss_kontrol.py -u 192.168.1.2 -f xss_vectors.txt -c 'cookies'  -r return_address -t timeout_seconds\npython3 reflected_xss_kontrol.py -u google.com -f xss_vectors.txt -c 'session=example_session_id' -r return_address -t timeout_seconds"""

print(colored(uyari, color="red"), colored("\nUsage:" + usg + "\n", color="yellow"))
time.sleep(1)


parser = argparse.ArgumentParser(usage=usg)

parser.add_argument('-u', '--url', help="Target URL", required=True)
parser.add_argument('-f', '--filename', help="XSS Vectors file", required=True)
parser.add_argument("-c", "--cookie", help="Cookies")
parser.add_argument("-r", "--returned_addrres", help="Return back address for find xss content")
parser.add_argument("-t", "--timeout", help="Timeout in seconds")
args = parser.parse_args()

#http://127.0.0.1/dvwa/vulnerabilities/xss_r/?name=

xss = open(args.filename, "r")
target = args.url
xss = xss.read()
returned = args.returned_addrres
cookie = {"Cookie":""}

timeout = int(args.timeout) if args.timeout != None else 2

if target.startswith("http://") or target.startswith("https://"):
    pass
else:
    target = "http://" + target

if returned != None:
    if returned.startswith("http://") or returned.startswith("https://"):
        pass
    else:
        returned = "http://" + returned

if args.cookie != None:
    cookie["Cookie"] = args.cookie


print("-" * 60)
print("Hedef üzerinde tarama gerçekleştiriliyor... \nHedef Adres: ", target)
if args.returned_addrres != None:
    print("Geri dönüş için bakılan adres: ", str(args.returned_addrres))
print("-" * 60)
sayi = 0
for i in xss.splitlines():
    url = target + str(i)
    
    try:
        #geri dönüş başka bir sayfaya mı yapılıyor yoksa aynı sayfada mı kıntrol edip ona göre sonuc belirleyelim.
        if args.returned_addrres == None:
            sonuc = requests.get(url, headers=cookie, timeout=timeout) # default 2 saniye zamanaşımı belirledik!
        else:
            sonuc = requests.get(returned, headers=cookie, timeout=timeout) # default 2 saniye zamanaşımı belirledik!
        
        if i in str(sonuc.content):
        # websitesi içeriğinde gönderdiğimiz değerler varsa muhtemelen XSS açığı bulunuyordur! 
            print("Muhtemel XSS Açığı Bulundu: ", url, sep="\t", end="\t")
            print("Değerler: " + i) 
            sayi += 1
    except requests.exceptions.ConnectTimeout: # zaman aşımı hatası gerçekleşirse
        print("Zamanaşımı Hatası!")
    except requests.exceptions.ConnectionError: #bağlantı hatası gerçekleşirse
        print("URL Bulunamadı veya Ulaşılamıyor! ")
        sys.exit(0)

print("Tarama Tamamlandı! {} adet muhtemel XSS açığı bulundu!".format(sayi))



