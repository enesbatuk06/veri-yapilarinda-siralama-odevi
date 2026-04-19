# Veri Yapıları Ödevi – Arama ve Sıralama Algoritmaları

## 📌 Proje Açıklaması

Bu projede temel arama ve sıralama algoritmaları Python programlama dili kullanılarak uygulanmıştır. Amaç, algoritmaların çalışma mantığını anlamak, performanslarını karşılaştırmak ve veri yapıları konusundaki bilgileri pekiştirmektir.

---

## 🔍 Arama Algoritmaları

### 1. Linear Search (Doğrusal Arama)

Linear Search algoritması, dizideki elemanları baştan sona tek tek kontrol ederek aranan değeri bulur.

* En iyi durum: O(1)
* Ortalama durum: O(n)
* En kötü durum: O(n)

✔ Avantaj: Basit ve her durumda çalışır
❌ Dezavantaj: Büyük verilerde yavaştır

---

### 2. Binary Search (İkili Arama)

Binary Search algoritması sadece sıralı dizilerde çalışır. Diziyi sürekli ikiye bölerek arama yapar.

* En iyi durum: O(1)
* Ortalama durum: O(log n)
* En kötü durum: O(log n)

✔ Avantaj: Çok hızlıdır
❌ Dezavantaj: Veri önceden sıralı olmalıdır

---

## 🔄 Sıralama Algoritmaları

### 1. Bubble Sort

Komşu elemanları karşılaştırarak büyük olanı sona iter.

* En iyi: O(n)
* Ortalama: O(n²)
* En kötü: O(n²)

---

### 2. Selection Sort

Her adımda en küçük elemanı bulup başa koyar.

* En iyi: O(n²)
* Ortalama: O(n²)
* En kötü: O(n²)

---

### 3. Insertion Sort

Elemanları doğru pozisyona yerleştirerek sıralar.

* En iyi: O(n)
* Ortalama: O(n²)
* En kötü: O(n²)

---

### 4. Merge Sort

Böl ve fethet mantığıyla çalışır, diziyi parçalayarak sıralar.

* En iyi: O(n log n)
* Ortalama: O(n log n)
* En kötü: O(n log n)

---

### 5. Quick Sort

Pivot seçerek diziyi parçalara ayırır ve sıralar.

* En iyi: O(n log n)
* Ortalama: O(n log n)
* En kötü: O(n²)

---

## ⚖️ Algoritmaların Karşılaştırılması

* Küçük veri setlerinde Insertion Sort oldukça hızlıdır.
* Büyük veri setlerinde Merge Sort ve Quick Sort daha verimlidir.
* Binary Search en hızlı arama algoritmalarından biridir ancak sıralı veri gerektirir.
* Bubble ve Selection Sort daha basit ama performans olarak zayıftır.

---

## ▶️ Program Nasıl Çalıştırılır?

1. Python yüklü olmalıdır
2. Terminal veya komut satırında proje klasörüne gidilir
3. Aşağıdaki komut çalıştırılır:

python main.py

---

## 🧪 Örnek Kullanım

Program çalıştırıldığında sıralama algoritmalarının çıktıları ve arama sonuçları ekrana yazdırılır.

---

## 🧠 Sonuç

Bu proje sayesinde arama ve sıralama algoritmalarının çalışma mantığı öğrenilmiş ve farklı algoritmaların performansları karşılaştırılmıştır.

---

## 👨‍💻 Geliştirici

Ad Soyad: Enes batuk
Ders: Veri Yapıları
Tarih: 2026
