LINK DEPLOY: https://juma-jordan-anythingfootballshop.pbp.cs.ui.ac.id/
NAMA: Juma Jordan Bimo Simanjuntak
NPM: 2406435843

## Pengimplementasian langkah

1. Saya membuat repo github terlebih dahulu sekaligus menentukan nama proyek

2. Repo github diikuti direktori yang ada di local dengan nama yang sama
3. kemudian saya memulai virtual environment, dan memasukan file requirements beserta melakukan instalasi
4. Baru kemudian saya memodifikasi file manage.py untuk melakukan test deploy jango ke local host sebelum ke PWS 
5. Di PWS saya membuat proyek baru, dan disitu saya menambahkan berkas-berkas yang dibutuhkan, ada di .env.prod, tidak juga lupa saya menambahkan tautan PWS ke ALLOWED HOST

6. melakukan deploy jango ke PWS
7. kemudian baru saya membuka proyek main di direktori proyek saya untuk memulai membuat tampilan
8. di main.html saya membuat templates yang diperlukan dan melakukan edit di views.py
9. di models.py ada beberapa hal yang saya buat, product view dan tentang product

10. Kemudian setelah variabel yang ada di views saya sesuaikan yang ada di main.html saya test deploy dulu di local sekiranya aman baru saya push di PWS. 
11. Kemudian saya push semuanya juga ke github. 

## Bagan Request 
Client (browser) --> HTTP GET / --> urls.py (main.urls) --> memanggil views.home --> (jika perlu baca/ubah) models.py (ORM ke DB) --> views memanggil `render(template, context)` --> Template HTML di-parse --> HTTP Response dikirim ke client

Penjelasan singkat:
-  `urls.py`: mapping URL ke fungsi/class view.
- `views.py`: menangani request, menjalankan logic, mengakses models bila perlu, diserahkan ke templates.
- `models.py`: definisi struktur data, saat view membutuhkan data, view memanggil model (contoh: `product_views = models.PositiveIntegerField(default=0)`).

## Peran `settings.py`
`settings.py` mengandung konfigurasi aplikasi Django, seperti **ALLOWED HOST**, **PRODUCTION**, **INSTALLED APPS**, **DATABASE**

## Cara kerja migrasi DB di Django
1. Melakukan modifikasi di (models.py).
2. `python manage.py makemigrations` membuat file migration.
3. `python manage.py migrate` menerapkan migration ke database.
Migrasi adalah langkah perubahan data atau model sehingga bisa direproduksi di environment lain. (virtual ke django)

## Mengapa Django sering dipilih sebagai permulaan pembelajaran web framework?
1. **Dokumentasi & komunitas besar**: banyak tutorial, plugin, dan paket siap pakai.
2. **Keamanan & best practices sudah built-in**
3. **Arsitekturnya Membantu Web Developing Lebih Cepat**
4. **Fleksibilitas yang besar**
Jadi Django cepat membuat MVP sambil mengajarkan banyak konsep penting (HTTP, ORM, migrations, templating).

Sumber: https://www.jagoanhosting.com/blog/django/