LINK DEPLOY: https://juma-jordan-anythingfootballshop.pbp.cs.ui.ac.id/
NAMA: Juma Jordan Bimo Simanjuntak
NPM: 2406435843

## 1. Perbedaan: Synchronous vs Asynchronous Request

### Synchronous request

Klien (browser) mengirim request ke server dan menunggu seluruh respons sebelum bisa melakukan aksi lain pada konteks tersebut.
Pada aplikasi web tradisional, pengiriman form atau navigasi halaman sering bersifat synchronous: browser memuat ulang halaman (full page reload).
Dampak: user menunggu selama round-trip; interaksi terasa blok sampai server merespons.

### Asynchronous request

Klien mengirim request tetapi tidak memblokir UI — JavaScript dapat menangani respons ketika tersedia.
Umumnya menggunakan API seperti XMLHttpRequest atau fetch (dikenal sebagai AJAX: Asynchronous JavaScript And XML, walau payload modern biasanya JSON).
Dampak: partial update (hanya sebagian halaman yang diubah), interaksi terasa lebih responsif.


---

## 2. Bagaimana AJAX bekerja di Django — alur request–response

- Event pemicu di klien: pengguna klik tombol, submit form dicegah (event.preventDefault()), atau otomatis di background.

- JavaScript mengirim request: memakai fetch() atau XMLHttpRequest ke endpoint Django (biasanya URL yang mengembalikan JSON). Sertakan header X-CSRFToken untuk POST/PUT/DELETE bila CSRF diperlukan. Gunakan Content-Type: application/json bila mengirim JSON.

- Django menerima request: URL routing -> view. Jika view dibangun untuk AJAX, biasanya mengembalikan JsonResponse atau HttpResponse dengan kode status yang sesuai.
Proses otentikasi/validasi/penyimpanan tetap dilakukan di server (server always trusted).

- Client menerima respons: JavaScript mem-parse JSON dan melakukan DOM update (menyisipkan HTML partial, menampilkan pesan, redirect, dll). Bisa menampilkan spinner/loader selama menunggu.

- Progressive enhancement & fallback: Biasanya sediakan fallback HTML form tradisional agar tetap bekerja apabila JavaScript disabled.

---

## 3. Keuntungan menggunakan AJAX dibandingkan render biasa (full render) di Django

- Respons lebih cepat (perceived performance): hanya partial content yang diambil, bukan seluruh HTML.

- Pengalaman pengguna lebih mulus: tidak ada full page reload, sehingga state UI (mis. posisi scroll, data form yang tidak berubah) bisa dipertahankan.

- Interaksi dinamis: inline validation, autocomplete, live search, infinite scrolling, update konten real-time.

- Hemat bandwidth: hanya data yang diperlukan (JSON) dikirim, bukan template lengkap.


---

## 4. Keamanan saat menggunakan AJAX untuk Login & Register di Django
- CSRF protection: Django menyediakan CSRF protection built-in. Untuk request berbasis AJAX yang mengubah state (POST/PUT/DELETE), pastikan mengirim token CSRF.
- Transport layer security (HTTPS): Selalu gunakan HTTPS; jangan kirim kredensial lewat koneksi tidak terenkripsi.
- Autentikasi dan sesi: Jika menggunakan session cookies, pastikan HttpOnly, Secure, dan SameSite di-set dengan benar. Jika menggunakan token, simpan token aman (jangan simpan token sensitif di localStorage jika risiko XSS tinggi)


## Bagaimana AJAX mempengaruhi UX (User Experience)

- Performa terasa lebih cepat: pengambilan data partial membuat respons terasa instan.

- Interaksi lebih halus: tidak ada flicker full page reload; animasi dan transisi bisa dipertahankan.

- Fitur interaktif: live validation, auto-save, infinite scroll, real-time update.

- Kontrol UI yang lebih besar: developer bisa menampilkan state loading, success, atau inline error lebih baik.
