# Tugas 6 

## Perbedaan Antara Asynchronous Programming dan Synchronous Programming
**Synchronous programming** berarti program dieksekusi berurutan, dimana setiap operasi harus menunggu operasi sebelumnya selesai sebelum menjalankan operasi selanjutnya. Sebaliknya, **asynchronous programming** memungkinkan program untuk menjalankan beberapa operasi secara bersamaan tanpa harus menunggu operasi sebelumnya selesai. Dalam asynchronous programming, operasi yang memakan waktu dapat berjalan di latar belakang, sehingga program tidak terblokir.

## Paradigma Event-Driven Programming dalam JavaScript dan AJAX
Paradigma event-driven programming adalah pendekatan dimana program merespon event atau peristiwa yang terjadi. Dalam JavaScript dan AJAX, ini berarti program merespon tindakan pengguna, seperti klik tombol atau mengirim formulir. Sebuah contoh penerapannya dalam tugas ini adalah ketika pengguna menekan tombol "Tambah Produk", kode akan merespon dengan membuka modal yang memungkinkan pengguna memasukkan data produk.

## Penerapan Asynchronous Programming pada AJAX
Asynchronous programming pada AJAX memungkinkan aplikasi web untuk berinteraksi dengan server tanpa menghentikan operasi lain di halaman. Ini dicapai dengan menggunakan metode seperti `fetch()` untuk membuat permintaan ke server tanpa memblokir operasi lain, `await()` untuk menunggu kode berjalan selesai, dan `then()` untuk menangani respons dari server setelah permintaan selesai. Dengan ini, halaman web tetap responsif dan tidak terblokir saat data diambil dari server.

## Perbandingan Fetch API dengan jQuery untuk Penerapan AJAX
**Fetch API** adalah standar JavaScript yang disediakan oleh browser modern. Ia merupakan cara bawaan untuk membuat permintaan HTTP dan mengelola responsnya. Fetch API lebih modern, lebih ringan, modular, dan efisien dalam hal ukuran dan kinerja. Ini sangat cocok untuk pengembangan aplikasi web modern di mana kinerja dan kejelasan kode penting.

**jQuery**, di sisi lain, adalah pustaka JavaScript yang lebih besar dan tua yang menyediakan banyak fitur dan utilitas, termasuk AJAX. Kelebihan jQuery adalah kompatibilitas lintas browser yang baik karena menangani perbedaan implementasi di berbagai browser.

Jika ingin mengembangkan aplikasi web modern, menggunakan Fetch API bisa menjadi pilihan yang lebih baik karena lebih efisien dan ringan.

## Implementasi Checklist
Berikut adalah langkah-langkah implementasi pada tugas ini:
1. Membuat method `add_product` dan `delete_product` menggunakan AJAX dan `get_product` dari JSON di `views.py`.
2. Mendaftarkan method-method tersebut pada `urls.py` pada aplikasi utama.
3. Mengubah tabel pada `main.html` menjadi sebuah fungsi yang mengimplementasikan method `get_product_json`.
4. Membuat tombol yang menampilkan modal dan tombol untuk menghapus produk.
5. Menambahkan modal pada `main.html` yang menampilkan form dan tombol untuk mengirim data form menggunakan method `add_product_ajax`.
6. Melakukan perintah `collectstatic` untuk mengumpulkan file static dari setiap aplikasi ke dalam folder yang dapat dengan mudah disajikan pada produksi.


# Tugas 5

## Manfaat Element Selector
Element selector digunakan untuk menerapkan gaya tampilan kepada suatu element HTML yang sama. Manfaat utama dari element selector adalah:

- Menerapkan gaya tampilan secara konsisten pada semua elemen dengan nama yang sama.
- Memudahkan pemeliharaan dan perubahan gaya tampilan global pada elemen-elemen dasar di seluruh halaman web.
- Mengikuti aturan semantik, menjaga struktur dan semantik HTML tetap utuh.

Contoh : 
1. Selector Universal (*)

- Selector ini memilih semua elemen di halaman web.
- Digunakan ketika ingin menerapkan gaya tampilan global pada semua elemen.

2. Selector Tag (Contoh: p, h1, div)

- Selector ini memilih semua elemen dengan nama tag yang sesuai.
- Digunakan ketika ingin menerapkan gaya tampilan pada semua elemen dengan tag yang sama.

3. Selector Class (Contoh: .btn, .header)

- Selector ini memilih semua elemen dengan atribut class yang sesuai.
- Digunakan ketika ingin menerapkan gaya tampilan pada elemen-elemen yang memiliki class tertentu.

4. Selector ID (Contoh: #container, #header)

- Selector ini memilih elemen dengan atribut id yang sesuai.
- Digunakan ketika ingin menerapkan gaya tampilan pada elemen dengan ID tertentu.

## HTML5 Tag
Beberapa tag HTML5 yang umum digunakan:

- `<header>`: Digunakan untuk mengatur bagian atas aplikasi web seperti judul dan logo.
- `<nav>`: Digunakan untuk mengelompokkan elemen-elemen yang terkait dengan navigasi seperti menu.
- `<main>`: Berisi dari konten utama suatu halaman web.
- `<footer>`: Digunakan untuk mengatur bagian bawah dari aplikasi web, sering digunakan untuk menampilkan hak cipta.
- `<section>`: Digunakan untuk mengelompokkan elemen-elemen dengan konten terkait.

Terdapat banyak tag lain juga selain diatas, misalnya 
HTML5 Tag adalah tag HTML yang diperkenalkan atau dimodifikasi pada versi HTML5. Beberapa contoh HTML5 Tag adalah:

- `<article>`: Menentukan konten yang mandiri, seperti artikel, blog post, komentar, dan sebagainya.
- `<aside>`: Menentukan konten yang terkait dengan konten utama, tetapi kurang penting, seperti sidebar, kotak iklan, dan sebagainya.
- `<audio>`: Menentukan konten suara yang tertanam, seperti musik, podcast, rekaman, dan sebagainya.
- `<canvas>`: Menentukan area untuk menggambar grafik, pada umumnya menggunakan JavaScript.
- `<datalist>`: Menentukan daftar opsi yang telah ditentukan untuk kontrol input, seperti input teks, input pencarian, dan sebagainya.
- `<detaild>`: Menentukan detail tambahan yang dapat dilihat atau disembunyikan oleh pengguna, seperti FAQ, petunjuk, dan sebagainya.

dan lainnya

## Perbedaan antara Margin dan Padding
Perbedaan utama antara margin dan padding adalah:

- Margin mengatur jarak antara elemen dengan elemen lain di sekitarnya, sedangkan padding mengatur jarak antara konten elemen dan batas elemen itu sendiri.

- Ketika ingin mengatur jarak antara elemen-elemen di halaman web ,maka akan menggunakan margin. Sedangkan ketika ingin mengatur jarak antara konten dalam elemen dan batas elemen itu sendiri, maka akan menggunakan padding.

agar lebih jelas berikut lampiran padding dan margin : 
![XML_id](images/paddingMargin.png)


## Perbedaan antara Framework CSS Tailwind dan Bootstrap
Perbedaan antara Tailwind dan Bootstrap meliputi:

- **Tailwind**: Tailwind adalah framework CSS yang memberikan banyak kelas yang bisa digunakan langsung dalam HTML. Ini memberi Anda kontrol tinggi dalam desain tampilan , tetapi memerlukan penulisan banyak kelas dalam HTML. Tailwind cocok digunakan ketika ingin tingkat kustomisasi tinggi dalam desain tampilan  .

- **Bootstrap**: Bootstrap adalah framework CSS yang memiliki banyak komponen siap pakai dan gaya yang sudah ada. Hal ini cukup menggabungkan komponen-komponen tersebut dalam HTML yang digunakan. Bootstrap cocok digunakan ketika kita ingin membuat tampilan dengan cepat atau dalam proyek-proyek kecil.

Kapan sebaiknya menggunakan Bootstrap atau Tailwind tergantung pada kebutuhan  . Jika ingin membuat tampilan dengan cepat dan tidak memiliki banyak waktu untuk desain, Bootstrap bisa menjadi pilihan. Sementara jika siap untuk menghabiskan waktu untuk mengkustomisasi tampilan sesuai keinginan, Tailwind bisa menjadi pilihan yang baik.

## Implementasi Checklist
- memberikan link bootstrap dan menambahkan create_product dan delete_product
- mengecek style yang ada di bootstrap
- setelah ketemu, menginspek dan mengambil komponen yang saya perlukan (saya mengambil pada section example)
- mengimplementasikan bootstrap dan css lainnya untuk ke empat file html saya (login,register,main dan edit product)
- melakukan push github

# TUGAS 4

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah formulir bawaan Django yang memudahkan pembuatan fitur registrasi untuk aplikasi web. Formulir ini dirancang untuk terintegrasi dengan Django authentication system.

Kelebihan:
- Mempercepat proses pembuatan fitur registrasi.
- Terintegrasi dengan baik dengan sistem otentikasi Django.
- Memiliki validasi bawaan untuk password untuk memastikan keamanannya.

Kekurangan:
- Kurang fleksibel untuk kostumisasi yang kompleks.
- Tampilan bawaannya terbatas dan membutuhkan penyesuaian lebih lanjut untuk desain tertentu.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Perbedaan terlihat pada definisi berikut.
Autentikasi: Proses verifikasi identitas pengguna, biasanya melalui kombinasi username dan password.
Otorisasi: Proses memberikan atau menolak izin kepada pengguna yang telah terotentikasi untuk mengakses sumber daya atau fitur tertentu.
Keduanya penting karena memastikan bahwa hanya pengguna yang memiliki hak akses yang dapat mengakses dan memodifikasi data atau fitur tertentu, meningkatkan keamanan dan privasi dalam aplikasi.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah potongan data kecil yang disimpan di browser pengguna. Saat pengguna mengunjungi sebuah website, server dapat mengirim cookie ke browser pengguna dan pada kunjungan selanjutnya, browser akan mengirim kembali cookie tersebut ke server. Django menggunakan cookies untuk mengidentifikasi sesi pengguna, memastikan bahwa data pengguna tetap aman dan konsisten selama mereka berinteraksi dengan aplikasi.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Meskipun cookies aman untuk sebagian besar kasus penggunaan, ada beberapa risiko yang harus diperhatikan:

- Cross-Site Scripting (XSS): Serangan ini dapat memungkinkan penyerang untuk mencuri cookies pengguna.
- Third-Party Cookies: Cookies dari domain pihak ketiga yang bisa digunakan untuk melacak aktivitas pengguna.
- Over-reliance on Cookies: Menyimpan informasi sensitif dalam cookies tanpa enkripsi dapat berisiko.
Untuk mengatasi risiko tersebut, selalu gunakan HTTPS dan pastikan aplikasi Anda terlindungi dari serangan XSS.

## Implementasi Step-by-Step:
1. Pembuatan Fungsi Register dan Login:
- Buat fungsi register dalam views.py.
- Tambahkan UserCreationForm untuk form registrasi.
- Buat fungsi login_user dan gunakan authenticate dan login untuk proses login.

2. Pembuatan Halaman Register dan Login:
- Buat register.html dan login.html dalam folder templates.

3. Routing:
- Tambahkan rute untuk halaman register, login, dan logout dalam urls.py.

4. Penggunaan Cookies:
- Set cookie last_login saat pengguna berhasil login.
- Akses cookie saat menampilkan halaman utama untuk menampilkan informasi terakhir login.
- Hapus cookie saat logout.

5. Integrasi dengan Model:
- Tambahkan relasi ke model User dalam model Item.
- Modifikasi fungsi yang berhubungan dengan item untuk mempertimbangkan pengguna yang sedang login.

6. Finalisasi:
- Lakukan run server untuk mengakomodasi perubahan model.
- Uji coba fitur-fitur yang telah dibuat.
- Push ke repositori GitHub.

# TUGAS 3

## Perbedaan antara Form POST dan Form GET dalam Django
Form POST dan Form GET merupakan cara untuk mengirim data klien/pengguna ke server pada Django

1. Form POST:
   - Data dikirim dalam tubuh permintaan HTTP.
   - Data yang dihasilkan dari form terkirim sebagai bagian dari body request, bukan  sebagai bagian dari URL.
   - Data tidak terlihat dalam URL, sehingga lebih aman untuk mengirim data sensitif seperti kata sandi.
   - Dapat digunakan untuk mengirim data yang lebih besar daripada Form GET.
   - Biasanya digunakan untuk operasi yang merubah data, seperti menambahkan, mengedit, atau menghapus entitas dalam basis data.
   - Pada Django data yang dikirim melalui metode POST biasanya diakses melalui atribut request.POST 
   - contoh URL POST :  https://www.contohpost.com/submit



2. Form GET:
   - Data dikirim melalui URL sebagai parameter-query.
   - Data terlihat dalam URL, sehingga kurang aman untuk data sensitif.
   - Biasanya digunakan untuk operasi bacaan, seperti pencarian atau filtrasi data.
   - Dapat dengan mudah dibagikan melalui tautan, karena data ada dalam URL.
   - metode GET sebaiknya tidak digunakan untuk mengirim data sensitif seperti password dan lainnya
   - Metode GET juga tidak cocok untuk mengirim data besar karena keterbatasan panjang URL
- contoh URL GET : https://www.contohsearch.com/search?query=contoh

## Perbedaan Utama antara XML, JSON, dan HTML dalam Konteks Pengiriman Data
XML, JSON, dan HTML merupakan tiga format yang berbeda untuk mengelola dan mengirim informasi dalam pengiriman data. Berikut beberapa perbedaan utama mereka :

1. XML (Extensible Markup Language):
   - Didesain untuk menyimpan dan mengirim data terstruktur dan dapat mendefinisikan skema sendiri.
   - Lebih rumit karena memiliki banyak tag dan atribut yang menyertai data.
   - sering digunakan dalam pertukaran data antara aplikasi yang tidak terkait secara langsung 
   - Digunakan dalam banyak aplikasi, terutama dalam pertukaran data antar sistem dan dalam konfigurasi file.
   - Harus diurai (parsed) untuk mengakses data di dalamnya.
   - parsing XML biasanya memerlukan lebih banyak kode karena struktur yang kompleks.
   


2. JSON (JavaScript Object Notation):
   - Didesain dan memiliki representasi data dalam format ringan serta mudah dibaca oleh manusia dan mesin.
- Lebih sederhana dibandingkan XML dengan sintaksis yang lebih ringkas.
- Umumnya digunakan dalam pertukaran data antara aplikasi web modern karena keterbacaan dan keringkasan sintaksisnya.
- Menggunakan format pasangan nama-nilai (key-value) yang sederhana.
- Parsing JSON lebih mudah karena keringanan format dan kemiripan objek dalam bahasa pemrograman


3. HTML (Hypertext Markup Language):
- Didesain untuk membangun struktur halaman web dan tampilan di web browser.
- Digunakan untuk mengatur tampilan dan hierarki elemen di halaman web.
- HTML memiliki syntax  yang terdiri dari atribut,elemen,dan nilai yang mengatur cara elemen konten ditampilkan dalam halaman web
- Tidak cocok untuk pertukaran data mentah antar aplikasi, karena fokusnya adalah pada tampilan dan interaktivitas di web.
- Parsing HTML dilakukan oleh peramban web


## Mengapa JSON Sering Digunakan dalam Pertukaran Data antara Aplikasi Web Modern

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan:
- JSON memiliki syntax yang ringkas dan lebih mudah dibaca oleh manusia dibandingkan XML atau yang lainnya, sehingga lebih efisien dan mudah digunakan
- JSON lebih mudah saat melakukan proses debugging
- JSON mendukung struktur data yang kompleks, termasuk objek dan larik bersarang, sehingga cocok untuk mengirim data yang lebih kompleks.
- Parsing lebih muda karena mendukung banyak bahasa pemrograman dan menghasilkan data dalam format JSON, sehingga dapat dengan mudah diintegrasi ke berbagai aplikasi.
- 
Sebagai hasilnya, JSON telah menjadi salah satu format standar untuk pertukaran data antar aplikasi web modern, menggantikan format lain seperti XML dalam banyak kasus.


## Implementasi Checklist Step-by-Step

- Membuat Form POST dan Form GET dalam Django:

Pertama, buat berkas forms.py dalam direktori main dan isinya dengan atribut yang akan diminta untuk Item.

- Implementasi Form POST:

Selanjutnya, impor modul HttpResponseRedirect, ItemForm, dan reverse. Buat fungsi create_item dalam tampilan (view) dengan menggunakan ItemForm untuk menangani pengiriman data melalui metode POST.

- Mengubah Fungsi show_main:

Di dalam fungsi show_main, tambahkan 'items': items pada bagian context agar daftar Item dapat dikirim ke template.

- Routing untuk Form POST:

Impor fungsi create_item pada berkas urls.py di direktori main dan tambahkan path untuk create_item sehingga halaman create_item dapat diakses melalui URL.

- Membuat Template HTML:

Buat berkas create_item.html dalam direktori main/templates dan isi dengan formulir yang akan ditampilkan pada halaman create_item. Pastikan formulir ini terkait dengan ItemForm yang telah didefinisikan.

- Menampilkan Data di main.html:

Edit berkas main.html agar nantinya data dari Item dapat ditampilkan pada halaman main.

- Implementasi Format Data Lainnya:

Melakukan impor HttpResponse dan serializers pada views.py.

Buat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id dalam views.py.

Mengisi fungsi show_xml 

Mengisi fungsi show_json 

Mengisi fungsi show_xml_by_id 

Mengisi fungsi show_json_by_id 

- Routing untuk Format Data:

Melakukan impor fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id pada urls.py di direktori main.
Menambahkan path pada urlpatterns di urls.py.

- Menguji Fungsi-fungsi:
Mencoba kelima fungsi tersebut pada Postman dengan membuat permintaan baru dan memasukkan URL localhost + path fungsi yang ingin diuji.

## Gambar
![XML_id](images/XML_id.png)
![XML](images/XML.png)
![JSON](images/JSON.png)
![JSON_id](images/JSON_id.png)
![HTML](images/HTML.png)








# Tugas 2 BPB 
link : https://scudinventory.adaptable.app/main/
## Implementasi checklist

## Bagan Serta Keterkaitan antar Berkas
![skema](images/skema.png)
- urls.py berfungsi sebagai pemilih tampilan/view sesuai request user
- models.py berfungsi sebagai penghubung database dan view saat melakukan pengolahan data
- views.py berfungsi sebagai melakukan logika bisnis yang akan dibantu oleh model dan template
- berkas HTML berfungsi untuk menampilkan data-data yang dimiliki

### Membuat direktori dan projek django
Hal pertama yang saya lakukan adalah membuat direktori untuk projek django tersebut. Membuat direktori dilakukan mulai dari inisiasi git, membuat virtual environment,menambah requirements.txt sampai menambahkan depenciesnya. Setelah itu barulah saya membuat proyek django yang saya inginkan. 

### Membuat aplikasi main dan routing
Selanjutnya setelah memastikan virtual environment aktif, saya membuat main dengan perintah python manage.py startapp main yang kemudian membuat direktori templates. Didalam templates tersebut kemudian saya mengedit tampilan web dengan mengandalkan unsur html dan css seperti card dan div, tidak lupa saya juga menggunakan atribut name, amount, dan description di dalamnya. Setelah itu saya memberikan routing dengan cara mengimport beberapa modul dan menambahkan rute untuk aplikasi main yang saya buat. 

## Virtual environment

### Jelaskan mengapa kita menggunakan virtual environment?
Virtual environment digunakan untuk memisahkan dan mengisolasi lingkungan kerja proyek secara terpisah. Ada beberapa alasan mengapa kita menggunakan virtual environmen.Dengan virtual environment, setiap proyek akan memiliki lingkungan kerjanya sendiri yang terisolasi. Hal ini membuat setiap proyek dependensi, yang memungkinkan proyek dapat diinstal secara terpisah tanpa saling mempengaruhi dan menghindari konflik satu sama lain. Virtual environment juga mendukung fleksibilitas versi phyton yang kita gunakan sehingga dapat menyesuaikan dengan kebutuhan proyek kita. 

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita dapat melakukan hal tersebut, namun meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, saya sangat menyarankan untuk menggunakan virtual environment agar menjaga kerapihan dan keteraturan proyek. Dengan virtual environment kita dapat lebih mudah mengelola banyak proyek tanpa konflik serta memastikan konsistensi dalam pengembangan proyek django yang dikembangkan. 


## MVC, MVT, MVVM dan perbedaannya
### MVT (Model-View-Template)
- Pengguna mengakses satu URL tertentu.
- Django akan mencocokkan URL dengan pola yang sesuai dalam berkas urls.py dan menentukan View yang akan menangani permintaan tersebut.
- View menerima permintaan dan menjalankan logika bisnis yang dibutuhkan oleh aplikasi.
- Jika View memerlukan data dari basis data, View akan berkomunikasi melalui Model sebagai perantara.
- Setelah Model selesai memproses data dalam basis data, View akan menggunakan templat (HTML) untuk merender data tersebut ke dalam tampilan yang diinginkan.
- Setelah templat selesai mengatur tampilan, View akan menghasilkan halaman HTML yang telah dirender bersama dengan respons HTTP yang sesuai.
- Respons HTTP tersebut berisi halaman HTML yang diminta oleh pengguna.
### MVC (Model-View-Controller)
- user berinteraksi dengan view dengan melakukan suatu action.
- action kemudian diteruskan ke Controller, pada Controller action tersebut diproses sesuai kebutuhan aplikasi.
- Controller akan berinteraksi dengan Model untuk mengambil atau mengubah data pada Model.
- Setelah berinteraksi dengan Model, Controller akan  mengupdate data yang akan ditampilkan dan mengirimkan ke View.
- View menerima data dari Controller kemudian mengupdate tampilan interface.
### MVVM (Model-View-ViewModel)
- Pengguna berinteraksi dengan Tampilan melalui tindakan yang dilakukan.
- Tindakan yang diterima oleh Tampilan akan diteruskan ke Model Tampilan (ViewModel).
- ViewModel mengelola logika bisnis aplikasi dan berfungsi sebagai perantara antara Tampilan dan Model.
- Jika diperlukan untuk berinteraksi dengan basis data, Model akan melakukan interaksi tersebut.
- Setelah data dari basis data diperoleh, Model akan meneruskannya ke ViewModel.
- Kemudian, ViewModel akan menjalankan proses yang dibutuhkan oleh aplikasi pada data yang diterima sebelum mengirimkannya kembali ke Tampilan.
- Setelah data yang telah diproses diteruskan ke Tampilan, Tampilan akan melakukan pengaturan tampilan sesuai dengan kebutuhan.
- Setelah itu, pengguna dapat melihat tampilan yang telah diperbarui dan siap untuk melakukan interaksi selanjutnya.




