import requests
import sys
url = "http://10.10.169.100:3000/"

#sonucu daha sonra stringe çevirmnek yerine direk string tanımlayıp atama yapılırsa daha kısa olur.
liste = [] 

try:
    while True:

        sonuc = requests.get(url)
        deger = eval(sonuc.content)
        
        if deger["value"]=="end":
        	print("Y")
        	liste.append("Y")
        	break
        print(str(deger["value"]))
        liste.append(deger["value"])

        if url == "http://10.10.169.100:3000/":
            url = url + deger["next"]        	
        else:
            url = url[:-1] + deger["next"]
except:
	print("Bir hata oluştu!")

enson = ""

for i in liste:
	enson = enson + i

print("\n\n Sonuc: ", enson)

