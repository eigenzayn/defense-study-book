# M3 · Training yang baik: optimizer, activation, regularisasi

Setelah gradient didapat, gradient itu harus dipakai dengan baik. Episode ini membahas pertanyaan-pertanyaan pendek yang biasanya menyusul setelah backpropagation: gradient descent, optimizer, activation function, regularisasi, dan inisialisasi. Pertanyaannya cepat, jadi jawabannya juga harus cepat. Satu kalimat yang jelas, lalu satu detail.

## Gradient descent dan mini-batch

Gradient descent menggeser bobot sedikit demi sedikit berlawanan arah dengan gradient empirical risk. Bobot baru sama dengan bobot lama dikurangi eta, dikali gradient. Eta adalah learning rate.

Kenapa mini-batch? Bayangkan seorang pendaki di tengah kabut yang mencoba turun gunung. Full batch ibarat mensurvei seluruh gunung sebelum setiap langkah: tepat, tetapi lambat. Satu sampel ibarat menebak dari satu batu di bawah kaki: murah, tetapi kacau. Mini-batch adalah jalan tengahnya. Mini-batch memberi perkiraan gradient yang tidak bias, berjalan cepat dan paralel di GPU, dan noise kecilnya bahkan membantu bobot keluar dari minimum yang tajam.

## Optimizer apa saja yang Anda tahu?

Gradient descent, stochastic gradient descent, momentum, AdaGrad, RMSprop, dan Adam.

Momentum menyimpan jumlah berjalan dari gradient sebelumnya, seperti bola yang menggelinding turun dan tetap melaju melewati gundukan kecil. AdaGrad dan RMSprop memberi setiap bobot ukuran langkahnya sendiri, berdasarkan kuadrat gradient sebelumnya. Adam menggabungkan keduanya, momentum dan RMSprop, ditambah bias correction untuk langkah-langkah awal. Adam adalah pilihan bawaan yang paling umum.

## Metode training lain

Profesor Klambauer pernah bertanya: apakah ada metode selain gradient descent? Ada. Model linear punya bentuk tertutup. Logistic regression bisa memakai iteratively reweighted least squares. RProp dan Quickprop hanya memakai tanda atau kelengkungan gradient. Newton, Gauss-Newton, Levenberg-Marquardt, dan conjugate gradient memakai informasi orde dua. Algoritma evolusioner atau random search sama sekali tidak butuh gradient.

## Activation function, dan yang berasal dari Linz

Pertanyaan favorit Profesor Hochreiter: activation function apa saja yang Anda tahu, dan mana yang berasal dari Linz?

Sigmoid dan tanh halus, tetapi mengalami saturasi, sehingga gradient-nya menjadi kecil sekali. ReLU murah dan tidak mengalami saturasi untuk input positif, tetapi unit bisa mati: kalau input sebuah unit terus negatif, unit itu tidak pernah belajar lagi.

Dan dari Linz: ELU dan SELU, dikembangkan di JKU. SELU, dari Klambauer dan rekan tahun 2017, membuat network self-normalizing. Rata-rata dan variansi activation ditarik ke nol dan satu, layer demi layer, tanpa layer normalisasi tambahan. Konstantanya: lambda sekitar 1,0507, dan alpha sekitar 1,6733. Titik tetapnya adalah rata-rata nol dan variansi satu.

Untuk layer output: linear untuk regresi, sigmoid untuk dua kelas, softmax untuk banyak kelas.

## Regularisasi

Weight decay, dropout, early stopping, data augmentation, dan noise.

Weight decay menambahkan penalti, lambda per dua dikali norma kuadrat bobot. Gradient-nya menambahkan lambda dikali w, sehingga di setiap langkah bobot menyusut dengan faktor satu dikurangi eta lambda sebelum update biasa. Dari situlah namanya berasal.

Dropout mematikan unit secara acak selama training, sehingga network tidak bisa bergantung pada satu unit tertentu. Bayangkan sebuah tim di mana anggota mana pun bisa absen di hari apa saja: semua orang harus menguasai pekerjaannya. Early stopping menghentikan training ketika validation error mulai naik.

## Inisialisasi dan batch normalization

Kenapa inisialisasi penting? Ada dua alasan. Pertama, bobot acak memecah simetri. Kalau semua bobot dimulai sama, semua unit mempelajari hal yang sama. Kedua, skalanya. Kalau skalanya salah, sinyal dan delta akan menghilang atau meledak saat melewati layer.

Penurunan singkatnya begini. Sebuah pre-activation adalah jumlah, untuk n in input, dari bobot dikali activation. Dengan bobot independen yang rata-ratanya nol, variansinya sama dengan n in, dikali variansi bobot, dikali rata-rata kuadrat activation. Supaya variansinya tetap, pilih variansi bobot satu per n in. Untuk ReLU, yang memotong rata-rata kuadrat menjadi setengah, pilih dua per n in. Itulah He initialization.

Batch normalization menstandarkan setiap pre-activation pada mini-batch, lalu mengatur ulang skala dan pergeserannya dengan parameter yang dipelajari.

## Tiga hal untuk diingat

Pertama. Mini-batch: perkiraan gradient yang murah, tidak bias, paralel, dengan noise yang berguna. Adam adalah momentum ditambah RMSprop dengan bias correction.

Kedua. Activation dari Linz adalah ELU dan SELU. SELU bersifat self-normalizing, dengan lambda sekitar 1,0507 dan alpha sekitar 1,6733.

Ketiga. Inisialisasi menjaga variansi tetap: satu per n in, atau dua per n in untuk ReLU. Regularisasi: weight decay, dropout, early stopping, augmentation, noise.
