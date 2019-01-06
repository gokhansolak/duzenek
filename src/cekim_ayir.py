
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
    if(type(kelime) is not str):
        return

    kelime_isle = kelime
    # isim cekim
    # reverse iterate: sondan başa
    for ek in reversed(ptr["çekim"]["isim"]):

        print(ek["tip"]+" eki inceleniyor.")
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
    with open('data/patterns.json') as json_file:
        ptr = json.load(json_file)

    cekim_ayir("Elmalarımızdakiyle")
