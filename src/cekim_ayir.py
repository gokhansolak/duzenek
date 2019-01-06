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

def cekim_ayir(kelime):
    # type safety
    if(type(kelime) is not str):
        return

    kelime_isle = arc.kucult_str(kelime)
    # isim cekim
    # reverse iterate: sondan başa
    for ek in reversed(ptr["çekim"]["isim"]):

        ptr_ek = ek["örüntü"]

        # kelime sonu yakala
        ptr_ek += "$"

        # eşleştir
        match = re.search(ptr_ek, kelime_isle)
        if match:
            # bilgilendir
            print(ek["tip"] + " eki bulundu: "+match.group(1))
            # ek temizle
            kelime_isle = kelime_isle[:match.start()]
            # eşleşen kök bak, varsa bitir
            if arc.ikili_ara(kokler, kelime_isle) >= 0:
                print("Kök bulundu: "+ kelime_isle)
                return kelime_isle

    # bulunamadıysa en küçük parçayı döndür
    print("Sözlükte olmayan kök: " + kelime_isle)
    return kelime_isle



if __name__ == "__main__":

    global ptr
    global kokler

    # ekler örüntü verisi
    with open('data/patterns.json') as json_file:
        ptr = json.load(json_file)
    # kökler listesi
    with open('data/KOKLER.txt') as kok_file:
        kokler = [line.strip() for line in kok_file]
        # sort for binary search
        kokler.sort()

    cekim_ayir("Elmalarımızdakiyle")
    cekim_ayir("Evleriyle")
    cekim_ayir("Gözlerinin")
    cekim_ayir("İnsanlarca")
