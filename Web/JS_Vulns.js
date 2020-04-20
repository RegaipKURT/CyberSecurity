function DOM_XSS_Vuln() {
	//deger kontrol edilmeden dökümana yazıldığı için kod çalıştırılabilir. 
	p = document.getElementById("prc").value;
	document.write(p);
};
