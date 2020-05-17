#!/usr/bin/python3

import argparse
import requests
import json
import sys

if __name__ == "__main__":

	#ip adresini almak için argüman oluşturalım
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--ip_address", help="Konumu bulunmak site veya istenen ip adresi")
	args = parser.parse_args()
	
	#eğer ip veya argüman verilmemişse yardım mesajı yazdıralım ve çıkalım.
	#print(sys.argv) # programın adının da sys.argv listesinde sayıldığını görelim. 
	if len(sys.argv) <= 1: 
		parser.print_help()
		sys.exit(0)

	#ip isimli değişkene argümanı atayıp request ile siteden sorgulayalım
	ip = args.ip_address
	url = "http://ip-api.com/json/"+ip
	resp = requests.get(url).content

	#biz sonuçları json objesi olarak aldık. 
	# json, xml, csv vb. formatlarda alınabilir (siteden ulaşılabilir.)
	sonuc = json.loads(resp)
	
	#sonuçları ekrana yazdırma
	print(ip + " için sonuçlar:")
	for i, j in enumerate(sonuc):
		print(str(j.upper()) + ": " + str(sonuc[j]))
