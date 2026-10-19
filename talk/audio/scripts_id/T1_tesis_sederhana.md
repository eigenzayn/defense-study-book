# T1 · Tesis saya dalam bahasa sederhana

Ada satu pertanyaan yang hampir pasti muncul saat sidang: masalah apa yang Anda selesaikan? Jadi mari kita latih jawabannya pelan-pelan, sampai terasa seperti cerita Anda sendiri.

Mulai dari metodenya. Recurrence CFD adalah cara untuk membuat simulasi jadi murah. Anda menjalankan satu simulasi penuh yang normal. Selama simulasi berjalan, Anda merekam, frame demi frame, berapa bagian dari setiap sel yang berpindah ke sel lain. Setelah itu, kecepatan dan tekanan tidak pernah dihitung lagi. Gerakan yang sudah direkam cukup diputar ulang, lalu dipakai untuk membawa sesuatu di dalam tangki. Karena itu metodenya cepat. Dalam kasus saya, simulasi penuh butuh 569 menit waktu solver. Satu replay hanya sekitar dua menit. Kira-kira 260 kali lebih cepat.

Sekarang masalahnya. Metode ini dibuat untuk passive scalar, yaitu sesuatu yang ikut terbawa aliran tetapi tidak mengubah aliran itu, seperti zat pewarna. Suhu tidak begitu. Air hangat lebih ringan, jadi naik ke atas. Suhu ikut menggerakkan aliran lewat gaya apung. Jadi ketika replay memakai gerakan rekaman yang tetap, umpan balik tersebut terputus.

Maka jawaban untuk pertanyaan "masalah apa yang Anda selesaikan" kira-kira begini. Saya menguji recurrence CFD pada suhu, sebuah scalar yang menggerakkan alirannya sendiri. Saya mengukur apa yang hilang dalam replay, dan seberapa banyak yang bisa diperbaiki tanpa menghitung aliran lagi.

## Mengapa orang harus peduli?

Pertanyaan kedua sering berbunyi: kenapa saya harus peduli? Jawaban singkat dan jujurnya begini. Proses termal berjalan berjam-jam, dan CFD penuh untuk waktu sepanjang itu terlalu lambat untuk dipakai sehari-hari. Replay yang 260 kali lebih cepat terdengar bagus sekali. Tetapi model yang cepat hanya berguna kalau galatnya diketahui. Tesis saya mengukur galat tersebut, pada kasus di mana suhu berperan, dan menunjukkan bagian mana yang bisa diperbaiki.

Cepat itu berguna hanya kalau galatnya diketahui. Ucapkan kalimat ini pelan-pelan dalam bahasa Inggris: fast is useful only with a known error. Kalimat ini bagus untuk diingat.

## Recurrence CFD dengan kata-kata sederhana

Kalau diminta menjelaskan recurrence CFD secara sederhana, pakai gambaran kamera lalu lintas. Bayangkan sebuah kamera yang merekam rute setiap mobil di sebuah kota. Lain kali, Anda tidak perlu mensimulasikan para pengemudi. Rute yang sudah terekam dipakai ulang untuk memindahkan paket. Begitulah replay bekerja.

Tetapi setiap analogi punya batas, dan penguji senang menanyakan batas itu. Batasnya begini: rekaman tidak menyimpan gambar. Yang disimpan adalah peta berapa banyak fluida berpindah dari sel ke sel. Dan kalau paketnya cukup berat sampai mengubah lalu lintas, rute lama menjadi salah. Begitulah suhu.

Satu langkah replay punya empat tahap. Ingat urutannya dalam bahasa Inggris: map, swap, correct, balance. Map: peta rekaman memindahkan panas. Swap: face exchange menambah sedikit pencampuran antar sel tetangga. Correct: tahap koreksi, dan di sinilah kontribusi saya. Balance: conservation constraint membetulkan total panas. Pada recurrence CFD standar, tahap koreksi tidak melakukan apa-apa. Dalam tesis saya, justru tahap inilah yang bekerja.

## Mengapa ini termasuk AI, bukan hanya CFD?

Pertanyaan ini pernah muncul di sidang sebelumnya, jadi siapkan jawabannya. Recurrence CFD termasuk simulasi berbasis data. Solver yang mahal menghasilkan data, lalu model yang murah memakainya ulang. Database berisi keadaan aliran yang terekam berperan sebagai data latih. Memilih frame berikutnya sama dengan nearest-neighbour search di dalam database itu, yang dikenal sebagai method of analogues.

Temuan utama saya sebenarnya soal generalisasi. Sebuah database berlaku untuk satu flow regime. Kalau satu kondisi batas mengubah regime-nya, database tersebut menjadi out of distribution. Dalam bahasa machine learning: data uji tidak lagi mirip dengan data latih. Persis itulah yang terjadi ketika tutup tangki saya didinginkan.

## Kasus uji

Anda harus bisa menggambarkan tangkinya tanpa catatan. Tangki tertutup, tujuh puluh lima kali tujuh puluh lima kali lima belas milimeter, dengan sel berukuran satu milimeter. Semburan hangat masuk di tengah ketinggian, bersuhu 333 kelvin dengan kecepatan 0,02 meter per detik, selama 315 detik. Bilangan Reynolds sekitar 99, jadi alirannya laminar. Tutupnya ada dua versi: satu terisolasi, satu didinginkan.

## Tiga hal untuk diingat

Pertama. Masalahnya: recurrence CFD dibuat untuk zat pewarna, dan saya mengujinya pada suhu, yang balik mempengaruhi aliran.

Kedua. Nilainya: 260 kali lebih cepat, tetapi cepat itu berguna hanya kalau galatnya diketahui, dan galat itulah yang saya ukur.

Ketiga. Sudut pandang AI: database adalah data latih, dan flow regime yang baru berarti datanya out of distribution.
