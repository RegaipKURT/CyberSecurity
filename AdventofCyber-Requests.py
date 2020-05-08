import requests
import sys
url = "http://10.10.169.100:3000/"

try:
    while True:
        sonuc = requests.get(url)
        deger = eval(sonuc.content)
        print(str(deger["value"]))
        if url == "http://10.10.169.100:3000/":
            url = url + deger["next"]
        else:
            url = url[:-1] + deger["next"]
except:
    sys.exit()