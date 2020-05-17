"""
İlk dışarıdan bir api üzerinden konum bilgisini almamız gerekecektir. 
Bizim kullanacağımız api https://ip-api.com/ adresinde bulunabilir. 
Siteye request isteği ile sorgu göndererek, dönen değeri alıp kullanacağız. 
Sİte bize json, xml, css vb. formatlarda değer dönebiliyor. 
Diğer dönüş tiplerine de bakabilirsiniz. 

Sonuç tam olarak doğru dönmeyecektir. 
Çünkü bulunan konum genellikle servis sağlayıcının verdiği konumdur. 
İnternetten baktığınız zaman görünen ip konumuna benzer sonuçlar dönecektir.
"""

import requests
import json
import argparse


if __name__ == "__main__":
    #argparse ile argümanlarımızı belirliyoruz. (sadece ip olacak.)
    parser = argparse.ArgumentParser()

    #ip adresi argümanını ekliyoruz.
    parser.add_argument("-i", "--ip_address", help="Konumu belirlenecek olan ip adresi")

    #argümanları parse ediyoruz.
    args = parser.parse_args()

    #aldığımız argümanı ip isimli değişkene atayalım ve url oluşturalım
    ip = args.ip_address
    print(ip)
    url = "http://ip-api.com/json/"+ip

    #request istegimizi yapıp sonucumuzu alalım
    response = requests.get(url) 
    sonuc = json.loads(response.content) 
    for i, j in enumerate(sonuc):
        print(str(j) + " :  " + str(sonuc[j]))