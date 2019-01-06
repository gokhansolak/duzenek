#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
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
            print(ek["tip"] + " eki bulundu: "+match.group(1))
            # ek temizle
            kelime = kelime[:match.start()]
            # eşleşen kök bak, varsa bitir
            if arc.ikili_ara(kokler_veri, kelime) >= 0:
                print("Kök bulundu: "+ kelime)
                return kelime, True

    # bulunamadıysa en küçük parçayı döndür
    print("Sözlükte olmayan kök: " + kelime)
    return kelime, False

def cekim_ayir(kelime):
    # type safety
    if(type(kelime) is not str):
        return

    kelime_isle = arc.kucult_str(kelime)
    kokler_bulunan = []
    # isim ve fiil cekim ekleri
    for ek_tipi in ["isim", "fiil"]:
        # ek tipi için kök ara
        ek_grubu = oruntu_veri["çekim"][ek_tipi]
        kok, mesru = cekim_grup(kelime_isle, ek_grubu)
        # meşruysa (sözlükte bulunduysa) bitir
        if mesru:
            return kok
        else:
            kokler_bulunan += kok

    # hiçbir ek tipiyle meşru kök bulunmadıysa en kısayı döndür
    kok_kisa = None
    for kok in kokler_bulunan:
        if not kok_kisa:
            kok_kisa = kok
        elif len(kok) < len(kok_kisa):
            kok_kisa = kok
    return kok_kisa



if __name__ == "__main__":

    global oruntu_veri
    global kokler_veri

    # ekler örüntü verisi
    with open('data/patterns.json') as json_file:
        oruntu_veri = json.load(json_file)
    # kökler listesi
    with open('data/KOKLER.txt') as kok_file:
        kokler_veri = [line.strip() for line in kok_file]
        # sort for binary search
        kokler_veri.sort()

    cekim_ayir("Elmalarımızdakiyle")
    cekim_ayir("Evleriyle")
    cekim_ayir("Gözlerinin")
    cekim_ayir("İnsanlarca")
    cekim_ayir("almıştık")
    cekim_ayir("yapmayacaktınız")
    cekim_ayir("gelmeliydiler")
    cekim_ayir("sevmiyorsun")
    cekim_ayir("koşmazsınız")
    cekim_ayir("gezsinler")
