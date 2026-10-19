# T3 · Tutup dingin, batas metode, dan bagaimana saya tahu hasilnya benar

Di episode ini kita masuk ke separuh tesis yang lebih sulit: tutup yang didinginkan. Setelah itu kita latih pertanyaan yang hampir selalu ditanyakan di akhir sidang. Bagaimana Anda tahu hasilnya benar? Apa yang akan Anda lakukan secara berbeda? Dan paper mana yang paling mempengaruhi Anda?

## Ketika tutupnya menjadi dingin

Sejauh ini tutupnya terisolasi. Panas masuk bersama semburan dan keluar lewat outlet, hanya itu. Sekarang tutupnya melepas panas ke luar, dan fisikanya berubah. Air dingin terbentuk di bawah tutup, lebih berat, lalu turun dalam bentuk plume. Lapisan di atas front mulai berputar. Artinya, suhu sekarang menciptakan gerakannya sendiri. Umpan balik seperti inilah yang tidak bisa ditiru replay, karena gerakannya sudah terkunci dalam rekaman.

Setiap replay di bab ini memakai sifat fluida yang sama dengan referensi. Siapkan kalimat ini, karena kalimat ini menutup satu kelompok pertanyaan sekaligus.

## Apa yang sudah benar dalam replay

Sepanjang run, tangki mendingin sebesar 9,62 kelvin. Replay standar berakhir 0,66 kelvin terlalu dingin. Kedengarannya kecil, dan memang kecil, untuk kandungan panasnya. Tetapi lihat letak panasnya. Profil akhir replay standar menyimpang 2,79 kelvin: bagian tengah terlalu hangat, lapisan atas terlalu dingin. Panasnya sama, tempatnya salah.

Dengan koreksi, pada kekuatan antara 0,475 dan 0,55, galat akhir kandungan panas berada antara minus 0,04 dan plus 0,06 kelvin, dan profil akhirnya membaik menjadi antara 0,59 dan 0,41 kelvin. Jadi koreksi mengembalikan panas ke lapisan yang benar. Sekali lagi, sampaikan dengan jujur: kekuatan ini dipilih dengan referensi.

Karena itulah saya selalu melaporkan dua jenis ukuran. Suhu rata-rata menunjukkan berapa banyak panasnya. Profil dan lebar front menunjukkan di mana panas itu berada. Sebuah replay bisa benar di satu ukuran dan salah di ukuran lainnya.

## Apa yang tidak bisa diperbaiki

Sekarang cacat yang tersisa. Selama tangki terisi, lapisan-lapisannya terpisah terlalu lambat. Saya mencoba enam varian koreksi lokal, dan tidak satu pun mengubah keterlambatan ini. Kenapa?

Cara paling bersih menjelaskannya begini. Koreksi lokal hanya memindahkan panas antar tetangga. Ia bisa mengubah bentuk front, tetapi tidak bisa membawa panas dari satu lapisan ke lapisan lain yang jauh. Itu namanya transport. Jadi keterlambatan ini adalah kekurangan transport, bukan kekurangan ketajaman.

Lalu saya mencoba menyediakan transport itu. Selama perekaman, saya menyimpan vertical heat flux, yaitu bagian panas yang dibawa oleh kecepatan vertikal, relatif terhadap rata-rata satu pita horizontal. Dalam replay, flux itu saya terapkan. Hasilnya bekerja: keterlambatan pelapisan turun dari 2,25 menjadi 0,45 kelvin. Tetapi ada harganya. Tangki kemudian berakhir 0,86 kelvin terlalu dingin.

## Kenapa rekaman tidak bisa melakukannya sendiri

Bagian terakhir dari cerita ini adalah flow regime. Bandingkan seberapa cepat masing-masing rekaman berubah dalam selang waktu pendek. Setelah semburan berhenti, aliran dengan tutup dingin terus memperbarui dirinya, kira-kira sepuluh kali lebih cepat daripada aliran dengan tutup terisolasi. Jadi rekaman yang dibuat tanpa tutup dingin memang tidak berisi gerakan kasus yang didinginkan. Sebuah database berlaku untuk satu flow regime, bukan untuk satu kasus. Dalam bahasa machine learning: regime baru berarti out of distribution.

## Bagaimana Anda tahu hasilnya benar?

Pertanyaan ini pernah muncul di sidang sebelumnya. Jawab dengan tiga poin singkat.

Pertama, setiap replay bersifat deterministik. Kalau dijalankan ulang, hasilnya sama sampai ke bit. Jadi perbedaan antara dua run pasti berasal dari satu setelan yang saya ubah.

Kedua, replay dan referensi saya bandingkan pada waktu yang sama, dan pada jendela akhir yang sama, dari detik 580 sampai 599, di kedua sisi.

Ketiga, neraca energi setiap kasus saya tutup, suku demi suku. Kalau panasnya tidak cocok, saya sudah tahu sebelum menafsirkan apa pun.

## Kenapa bias dan RMSE?

Pada sebuah trace, bias memberi tahu arah galat, terlalu hangat atau terlalu dingin. Root mean square error memberi tahu besarnya. Ada identitas rapi yang bisa Anda turunkan di papan tulis. RMSE kuadrat sama dengan bias kuadrat ditambah variansi galat. Jadi identitas ini memisahkan pergeseran dari bentuk yang salah.

## Dua pemeriksaan fisika

Kenapa alirannya laminar? Semburan masuk dengan kecepatan 0,02 meter per detik lewat lubang lima milimeter, sehingga bilangan Reynolds sekitar 99, jauh di bawah transisi. Bilangan Richardson-nya 1,84: gaya apung sedikit lebih kuat daripada inersia, jadi semburan membelok ke atas dalam jarak beberapa kali lebar inlet.

Kenapa memakai Boussinesq approximation? Densitas hanya berubah sedikit pada rentang suhu ini. Jadi densitas dianggap konstan di mana-mana, kecuali pada suku gravitasi. Dan ada kaitan yang bagus dengan tesis: suku gaya apung itulah tepatnya hubungan yang diputus oleh replay.

## Apa yang akan Anda lakukan berbeda? Future work

Tiga hal. Biarkan recorded diffusivity bekerja, dengan exchange implisit atau langkah waktu yang lebih pendek. Bagi conservation constraint menjadi beberapa kompartemen, supaya tidak mendorong panas kembali ke front. Dan gunakan beberapa rekaman, dipilih berdasarkan keadaan suhu yang sedang di-replay, supaya lebih dari satu regime tercakup.

## Paper mana yang paling mempengaruhi Anda?

Lichtenegger dan Pirker, 2016, yang memperkenalkan recurrence CFD dan recurrence matrix. Pirker dan rekan, 2018, untuk face exchange dan conservation constraint. Dan Zalesak, 1979, untuk batas lokal flux-corrected transport yang dipakai limiter saya.

## Tiga hal untuk diingat

Pertama. Dengan tutup dingin, kandungan panasnya benar, tetapi lapisan terpisah terlalu lambat: itu kekurangan transport.

Kedua. Recorded flux menurunkan keterlambatan dari 2,25 menjadi 0,45 kelvin, tetapi tangki lalu berakhir 0,86 kelvin terlalu dingin.

Ketiga. Saya tahu hasilnya benar karena replay deterministik, satu perubahan per run, waktu pembanding yang sama, dan neraca energi yang tertutup.
