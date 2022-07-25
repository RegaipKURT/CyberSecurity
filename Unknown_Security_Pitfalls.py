from asyncio import subprocess
import os, tempfile, zipfile, re
from threading import local
from time import sleep


# #İç içe oluşturulan dosyaların yetkisi
# def make_dirs():
#     os.makedirs("A/B/C", mode=0o700)

# make_dirs()



# #Çoklu dosya yolunu birleştirme
# def read_file(filename):
#     file_path = os.path.join("data_manipulation", "csv", filename)
#     if file_path.find(".") != -1:
#         print("Failed!")
#     with open(file_path) as f:
#         print(f.read())

# read_file("/etc/passwd")




# # Geçici dosya tempfile prefix ve suffix parametrelerinde açıklıklar
# # def touch_tmp_file(id):
# #     tmp_file = tempfile.NamedTemporaryFile(prefix=id)
# #     sleep(3)
# #     tmp_file.write(bytes("test", encoding="utf-8"))
# #     print(f"tmp file: {tmp_file} created!")

# # touch_tmp_file("../home/pars/Desktop/Programs/training/")



# #HTTP üzerinden gelen dosyaların extract edilmesi - Zip Slip 
# def extract_html(filename):
#     zf = zipfile.ZipFile(filename.temporary_file_path(), "r")
#     for entry in zf.namelist():
#         if entry.endswith(".html"):
#             file_content = zf.read(entry)
#             with open(entry, "wb") as fp:
#                 fp.write(file_content)
#     zf.close()
#     return "Files extracted!"

# extract_html("x.zip")



# def is_sql_injection(query):
#     pattern = re.compile(r".*(union)|(select).*")

#     print("Match metodu:", re.match(pattern, query))
#     print("Search metodu:", re.search(pattern, query))

#     return re.search(pattern, query)

# is_sql_injection("123\nselect * from users;")



# # Aşağıdaki login fonksiyonu optimize kod olarak çalıştırıldığında assert kısmı çalıştırılmadığından
# # ilgili kontrolün atlatılması mümkün olmaktadır.
# def isSuperUser():
#     condition = False
#     return condition

# def login():
#     assert isSuperUser(), "Yetkisiz Giriş"
#     print("Giriş Başarılı")

# login()





# Library Hijacking
# python3 -m http.server komutu çalıştırıldığında aynı dizinde socket.py isimli bir python dosyası olursa çalıştırılır.



#Dependency Confusion
# Yereldeki kütüphane ile PyPi arasında çatışma olursa ve >= şeklinde belirtme varsa büyük olan versiyon yüklenir.
