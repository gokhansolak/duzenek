#!/usr/bin/python3
import re
import json

ALFABE = ' \'-aâbcçdefgğhıîijklmnoöprsştuüvyz'
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

    kelime_isle = kelime
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


        # yoksa devam et



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
        sort_sira = {i:ALFABE.index(i) for i in ALFABE}
        kokler.sort(key=sort_sira.get)

    print(kokler)

    cekim_ayir("Elmalarımızdakiyle")
