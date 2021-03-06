#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
import json
import araclar as arc

YUMUSAT = {'ç': 'c', 't': 'd', 'p': 'b', 'k': 'ğ', 'g':'ğ'}
SERTLES = {'c': 'ç', 'd': 't', 'b': 'p', 'g': 'k'}
SESLILER = {'hepsi':'aeıioöuü',
    'kalın':'aıou',
    'ince':'eiöü',
    'dar':'ıiuü',
    'geniş': 'aeoö'}


def cekim_grup(kelime, grup):
    # reverse iterate: sondan başa
    for ek in reversed(grup):

        ptr_ek = ek["örüntü"]

        # kelime sonu yakala
        ptr_ek += "$"

        # eşleştir
        match = re.search(ptr_ek, kelime)
        if match:
            # bilgilendir
            print(ek["tip"] + " eki bulundu: "+match.group(0))
            parca_say=len(match.groups())

            kelime_tmp = kelime
            # birden fazla grubu ters sırayla temizle
            for i in range(parca_say,0,-1):
                # boş eşleşmeyi atla
                if not match.group(i) or len(match.group(i)) == 0:
                    continue
                # ek temizle
                kelime_tmp = kelime[:match.start(i)]
                # eşleşen kök bak, varsa bitir
                if arc.ikili_ara(kokler_veri, kelime_tmp) >= 0:
                    print("\tKök bulundu: "+ kelime_tmp)
                    return kelime_tmp, True
            # hiçbiri kök değilse de kelimeyi güncelle
            kelime = kelime_tmp

    # bulunamadıysa en küçük parçayı döndür
    print("\tSözlükte olmayan kök: " + kelime)
    return kelime, False

def cekim_ayir(kelime):
    # type safety
    if(type(kelime) is not str):
        return

    kelime_isle = arc.kucult_str(kelime)

    # zaten kökse aynen döndür
    if arc.ikili_ara(kokler_veri, kelime_isle) >= 0:
        return kelime_isle

    # sadece zaten ayrıştırılması gerekenleri say
    sayac["toplam"]+=1;

    kokler_bulunan = []
    # isim ve fiil cekim ekleri
    for ek_tipi in ["isim", "fiil"]:
        # ek tipi için kök ara
        ek_grubu = oruntu_veri["çekim"][ek_tipi].copy()
        # ek-fiiller hem isimlerin hem de fiillerin sonuna eklenebilir
        ek_grubu += oruntu_veri["çekim"]["ek-fiil"]
        # çekim grubunu ayır
        kok, mesru = cekim_grup(kelime_isle, ek_grubu)
        # meşruysa (sözlükte bulunduysa) bitir
        if mesru:
            sayac["doğru"]+=1;
            return kok
        else:
            kokler_bulunan.append(kok)

    # hiçbir ek tipiyle meşru kök bulunmadıysa en kısayı döndür
    kok_kisa = None
    for kok in kokler_bulunan:
        if not kok_kisa:
            kok_kisa = kok
        elif len(kok) < len(kok_kisa):
            kok_kisa = kok
    return kok_kisa + '(!'+kelime+'!)'



if __name__ == "__main__":

    # usage safety check
    if len(sys.argv) < 2:
        print("Kullanım: python cekim_ayir.py girdi_dosyası")
        sys.exit()

    global oruntu_veri
    global kokler_veri
    global sayac

    # kök bulma basarısı doğru/toplam
    sayac = {"doğru":0, "toplam":0}

    # ekler örüntü verisini oku
    with open('data/patterns.json') as json_file:
        oruntu_veri = json.load(json_file)
    # kökler verisini oku
    with open('data/kokler.txt') as kok_file:
        kokler_veri = [line.strip() for line in kok_file]
        # sort for binary search
        kokler_veri.sort()
    # girdi dosyasını oku
    with open(sys.argv[1]) as test_file:
        girdi_list = []
        for line in test_file:
            girdi_list += [w for w in line.strip().split()]

    # her kelimeyi işleyerek çıktı metnine ekle
    cikti_str = ""
    for k in girdi_list:
        cikti_str += cekim_ayir(k) + " "

    print(cikti_str)
    print(str(sayac))
