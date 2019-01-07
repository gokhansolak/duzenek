# DÜZEN-EK

_Düzenli ifade kullanarak ek ayırma_

Bu projenin amacı Türkçe kelimeleri eklerinden ayırarak kelime kökünü bulmak (stemming). [Yöntem](docs/yontem.md) olarak, eklerin ve köklerin düzenli ifadeler (regex) olarak tanımlanmasına dayanıyor.

Henüz çok yeni olduğu için birçok eksiği bulunuyor. Şimdilik sadece isim ve fiil çekim eklerini ayırt edebiliyor.

### Kullanım

Bir dosyadaki tüm kelimelerin kökünü bulmak için:
```
python3 cekim_ayir.py girdi_dosyası
```

### Yapılacaklar
- [ ] Çekim ekleri
  - [x] İsim
  - [x] Fiil
  - [ ] Ek-fiil
- [ ] Ses değişimleri
  - [ ] Ünsüz yumuşaması
  - [ ] Ünlü düşmesi
  - [ ] Ünlü/ünsüz türemesi
- [ ] Kök sözlüğü geliştirme aracı
- [ ] Yapım ekleri (?)
