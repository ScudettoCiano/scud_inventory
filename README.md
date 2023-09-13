# Tugas 2 BPB 
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




