# A1 · Recurrence CFD, seperti diajarkan Profesor Pirker

Profesor Pirker adalah pembimbing Anda, dan beliau mengajar Numerical Methods in Fluid Mechanics. Kemungkinan besar beliau akan bertanya seputar recurrence CFD dan gambar-gambar di tesis Anda. Di episode ini kita telusuri recurrence CFD sesuai alur kuliah beliau, supaya jawaban Anda terdengar seperti bahasa kuliahnya, lalu setiap ide kita kaitkan dengan pekerjaan Anda sendiri.

## Kenapa recurrence CFD?

Mulai dari gambaran besar. Banyak aliran industri berjalan lama dan menunjukkan pola yang berulang. Contohnya bubble column, fluidized bed, atau stirred vessel yang turbulen. Menghitung momentum dan tekanan sepanjang waktu itu sia-sia ketika alirannya terus mengulang dirinya.

Jadi recurrence CFD membuat sebuah prediksi berani: pakai ulang aliran yang sudah direkam. Lalu prediksi itu dikoreksi dengan fisika, di mana pun pemakaian ulang tadi merusak sesuatu, misalnya neraca massa.

Ada cara bagus untuk mengaitkannya dengan kuliah. Algoritma SIMPLE melakukan hal yang serupa. SIMPLE menebak tekanan, menghitung kecepatan, lalu mengoreksi tekanan dari persamaan kontinuitas. Recurrence CFD menebak aliran dari rekaman, lalu mengoreksinya. Prediksi berani, lalu koreksi berbasis fisika. Kalau Anda mengucapkan kalimat itu dalam bahasa Inggris, bold prediction plus physics-based correction, Anda sedang berbicara dengan bahasa beliau.

## Flow-based dan transport-based

Ada dua keluarga. Flow-based recurrence CFD, dari Lichtenegger dan Pirker tahun 2016, menyambung potongan-potongan aliran terekam menjadi satu aliran buatan yang panjang, dan masih menyelesaikan persamaan transport di atasnya. Kira-kira 100 kali lebih cepat daripada CFD penuh.

Transport-based recurrence CFD, dari Pirker dan Lichtenegger tahun 2018, melangkah lebih jauh. Persamaan transport tidak diselesaikan sama sekali, melainkan diganti dengan cell shift dan face swap. Contoh di kuliah adalah ladle baja: 26 jam CFD penuh, dibandingkan 1,6 detik recurrence CFD berbasis transport.

Tesis Anda memakai bentuk transport-based, ditambah correction hook dan conservation constraint.

## Recurrence norm, matrix, plateau, dan prominence

Recurrence norm mengukur seberapa berbeda dua keadaan yang terekam. Hitung untuk semua pasangan, normalkan, dan hasilnya recurrence matrix.

Sekarang ambil satu baris matriks itu. Baris itu dimulai dari nol di diagonal, karena sebuah keadaan identik dengan dirinya sendiri. Lalu nilainya naik dan berosilasi di sekitar sebuah plateau. Kalau barisnya turun jauh di bawah plateau, aliran kembali ke keadaan yang mirip dengan keadaan sebelumnya. Itulah recurrence, dan replay bisa melompat ke sana. Prominence mengukur seberapa dalam penurunan itu, relatif terhadap plateau.

Metodenya meminta prominence sekitar 0,05 sampai 0,1. Tangki Anda punya median 0,028. Jadi penurunannya dangkal, dan replay memutar frame secara berurutan. Katakan dengan terus terang: aliran saya tidak recurrent, dan itu tidak masalah, karena penghematannya datang dari tidak menghitung kecepatan dan tekanan.

## Tiga kegagalan berani

Kuliahnya menyebut tiga bold failure dari recurrence CFD, masing-masing dengan koreksinya. Hafalkan sebagai tiga pasangan.

Pertama, ketidakseimbangan massa. Cell shift tidak menjaga massa secara lokal. Jadi sebuah monitor global mengoreksi totalnya, dengan face swap yang bekerja pada massa.

Kedua, difusi yang tidak fisis. Jumlah swap yang tetap memberi pencampuran yang sama di mana-mana. Jadi jumlah swap seharusnya mengikuti pencampuran lokal.

Ketiga, recurrence yang terlalu sedikit. Pada domain yang besar, frame yang cocok secara global belum tentu cocok secara lokal. Jadi domainnya dibagi menjadi recurrence island, masing-masing dengan matriksnya sendiri.

Tesis Anda menyentuh ketiganya. Conservation constraint adalah yang pertama. Recorded diffusivity adalah yang kedua. Dan aliran Anda, dengan prominence yang terlalu kecil, adalah yang ketiga.

## Kapan berhasil, kapan gagal?

Metode ini berhasil ketika gerakannya berulang dan scalar-nya tidak mengubah aliran. Metode ini gagal ketika scalar menggerakkan aliran, atau ketika keadaan operasinya berubah. Pada keadaan baru, rekaman memang tidak berisi gerakan yang akan dihasilkan keadaan itu.

Itulah hasil Anda. Dengan tutup dingin, aliran terus memperbarui dirinya lewat plume dingin, gerakan yang tidak pernah terlihat dalam rekaman tutup terisolasi. Jawaban dari kuliah adalah multi-state recurrence CFD: satu database untuk setiap keadaan proses.

## Digital twin

Profesor Pirker menyukai cerita digital twin. Model tangki dengan satu nilai rata-rata bekerja seketika, tetapi mengabaikan bagian dalam pabrik. CFD penuh menunjukkan bagian dalam, tetapi butuh berhari-hari. Contoh di kuliah: model tangki di bawah satu detik, eksperimen 750 detik, CFD dua hari, dan recurrence CFD 30 detik. Jadi recurrence CFD berada di tengah.

Tetapi kalau dijalankan maju tanpa pengawasan, galatnya menumpuk. Jadi data langsung dari proses harus terus menyelaraskannya. Dan tesis Anda menunjukkan apa yang harus diawasi oleh twin seperti itu: satu kondisi batas bisa memindahkan proses ke regime yang tidak dicakup database.

## Apakah recurrence CFD termasuk machine learning?

Jawablah dengan hati-hati. Recurrence CFD adalah simulasi berbasis data. Ground truth yang mahal menghasilkan data, model murah memakainya ulang, dan pertanyaan sebenarnya adalah seberapa jauh ia bisa digeneralisasi. Tidak ada training dengan gradient. Memilih frame berikutnya adalah nearest-neighbour search. Dan replay-nya adalah rangkaian operator linear yang sparse, mirip dengan learned propagator.

Langkah AI yang mungkin: mempelajari peta untuk keadaan yang belum pernah terlihat, mempelajari flux yang hilang sebagai fungsi keadaan, atau melatih neural operator pada database.

## Tiga hal untuk diingat

Pertama. Prediksi berani ditambah koreksi berbasis fisika, sama seperti SIMPLE yang menebak tekanan lalu mengoreksinya.

Kedua. Tiga bold failure: ketidakseimbangan massa, diatasi dengan neraca global; difusi tidak fisis, diatasi dengan swap lokal; recurrence terlalu sedikit, diatasi dengan island. Tesis Anda menyentuh ketiganya.

Ketiga. Sebuah database berlaku untuk satu flow regime. Jawaban kuliahnya adalah multi-state recurrence CFD, dan tutup dingin Anda adalah contohnya.
