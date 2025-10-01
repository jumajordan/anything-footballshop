LINK DEPLOY: https://juma-jordan-anythingfootballshop.pbp.cs.ui.ac.id/
NAMA: Juma Jordan Bimo Simanjuntak
NPM: 2406435843

## 1. Prioritas Pengambilan CSS Selector
Urutan prioritas ketika browser menentukan style:
1. **Importance**: aturan dengan `!important` akan selalu menang.
2. **Origin**: urutan prioritas style dari author, user, dan default browser.
3. **Specificity**: semakin spesifik selector, semakin tinggi prioritasnya.
   - Inline style > ID > Class/attribute/pseudo-class > Element/pseudo-element.
4. **Source Order**: jika semua sama, aturan yang ditulis terakhir akan digunakan.

---

## 2. Responsive Design
**Mengapa penting:**
- Menyesuaikan tampilan di berbagai ukuran layar (mobile, tablet, desktop).
- Meningkatkan pengalaman pengguna dan keterbacaan.
- Mendukung SEO dan performa.
- Mengurangi biaya maintenance karena hanya satu basis kode.

**Contoh:**
- Aplikasi dengan responsive design: layanan besar seperti e-commerce, sosial media, dan mesin pencari.
- Aplikasi tanpa responsive design: aplikasi lama/legacy atau sistem internal yang dibuat hanya untuk desktop.

---

## 3. Margin, Border, Padding
- **Margin**: ruang di luar elemen, memisahkan dengan elemen lain.
- **Border**: garis pembatas yang mengelilingi elemen.
- **Padding**: ruang di dalam elemen, antara konten dan border.

---

## 4. Flexbox & Grid Layout
- **Flexbox**: sistem layout satu dimensi (baris atau kolom). Cocok untuk mengatur alignment horizontal/vertikal dan distribusi ruang antar elemen.
- **Grid**: sistem layout dua dimensi (baris dan kolom). Cocok untuk membuat layout halaman kompleks atau grid produk.


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Pertama-tama saya menambahkan fungsi edit, delete product di views.py, mengedit urls.py dan membuat page htmlnya 
2. kemudian saya mendeklarasikan bahwa saya akan menggunakan css tailwind, di base.html
3. saya menambahkan category di fungsi show main di views.py karena navigation bar perlu menampilkan kategori
4. saya membuat file html khusus untuk navigation bar bernama navbar.html dan dihubungkan dengan main.html
5. Saya membuat file html product_box untuk membuat kotak untuk setiap product di main 
6. Saya mengedit semua file html jadi menggunakan css untuk styling 
7. memastikan styling berjalan dengan baik
8. push git ke pws dan github
