
import re
import json

YUMUSAT = {'ç': 'c', 't': 'd', 'p': 'b', 'k': 'ğ', 'g':'ğ'}
SERTLES = {'c': 'ç', 'd': 't', 'b': 'p', 'g': 'k'}
SESLILER = {'hepsi':'aeıioöuü',
    'kalın':'aıou',
    'ince':'eiöü',
    'dar':'ıiuü',
    'geniş': 'aeoö'}

def cekim_ayir(kelime):
    # type safety
    if(type(kelime) is not string) return;

    # isim cekim
    # reverse iterate: sondan başa
    for ek in reversed(ptr["çekim"]["isim"]):

        ptr_ek = ek["örüntü"]

        # kelime sonu yakala
        ptr_ek += "$"
        # escape chars
        ptr_ek = re.escape(ptr_ek)

        # eşleştir
        match = re.match(ptr_ek, kelime)
        if match:
            # bilgilendir

            # ek temizle

            # eşleşen kök bak, varsa bitir

        # yoksa devam et



if __name__ == "__main__":

    with open('data/patterns.json') as json_file:
        global ptr = json.load(json_file)

    cekim_ayir("Elmalarımızdakiyle")
