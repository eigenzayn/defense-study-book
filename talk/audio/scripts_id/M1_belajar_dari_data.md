# M1 · Belajar dari data: risk, loss, dan cerita bias-variance

Hampir setiap ujian Machine Learning and Perception dimulai dari titik yang sama. Penguji berkata: tuliskan sebuah supervised data set dan kerangka training-nya. Kalau cerita ini bisa Anda sampaikan dengan tenang, sisa ujian akan terasa lebih ringan. Jadi mari kita susun, satu bagian demi satu bagian.

## Data, model, loss, rata-rata, minimalkan

Kita punya N pasangan. Setiap pasangan terdiri dari input x n dan label y n. Kita menganggap pasangan-pasangan itu diambil secara independen dari satu distribusi yang tidak diketahui, p dari x dan y.

Sebuah model g memetakan input menjadi prediksi, dan model itu punya bobot w. Sebuah loss L mengukur seberapa salah satu prediksi. Kalau loss dirata-ratakan untuk semua pasangan training, hasilnya disebut empirical risk. Dan belajar artinya sederhana: cari bobot yang membuat empirical risk sekecil mungkin.

Ingat dalam lima kata bahasa Inggris: data, model, loss, average, minimise.

## Kenapa tidak meminimalkan galat yang sebenarnya?

Penguji akan mendesak: apa itu generalization error, dan kenapa tidak bisa diminimalkan secara langsung?

Generalization error adalah nilai harapan loss pada data baru yang diambil dari distribusi sebenarnya. Untuk menghitungnya, loss harus diintegralkan terhadap p dari x dan y. Masalahnya, p tidak diketahui. Seluruh persoalan belajar ada di situ.

Jadi yang kita minimalkan adalah empirical risk, lalu generalization error diperkirakan pada data yang tidak dipakai untuk training: sebuah test set, atau cross-validation. Menurut hukum bilangan besar, rata-rata loss pada test set yang besar akan mendekati nilai harapannya.

Satu jebakan yang harus dihindari: training loss bukan perkiraan yang adil. Bobotnya dipilih berdasarkan data itu, jadi angkanya terlihat terlalu bagus.

## Apa itu loss function?

Loss membandingkan label dengan prediksi. Nilainya tidak pernah negatif, dan nol kalau prediksinya benar. Loss dipilih sesuai tugasnya.

Untuk regresi, squared loss: setengah kali selisih label dan prediksi, dikuadratkan. Untuk dua kelas, binary cross-entropy. Untuk banyak kelas, categorical cross-entropy: minus jumlah, untuk semua kelas, dari label dikali log probabilitas prediksi. Dan untuk support vector machine, hinge loss.

Profesor Klambauer pernah menanyakan lanjutan yang menarik: apakah semua loss bisa diturunkan? Tidak. Zero-one loss, yang hanya menghitung jumlah kesalahan, tidak punya gradient yang berguna karena datar hampir di mana-mana. Jadi untuk training kita memakai cross-entropy.

## Regresi linear sebagai pemanasan

Dengan model linear dan squared loss, risk-nya berbentuk mangkuk. Fungsinya konveks, jadi hanya ada satu minimum, dan minimum itu bisa ditemukan dalam bentuk tertutup. Ambil gradient dari setengah kali norma kuadrat y dikurangi X w. Hasilnya minus X transpose dikali error. Samakan dengan nol, dan muncul normal equations. Solusinya: X transpose X, diinverskan, dikali X transpose y. Itulah pseudo-inverse.

Perhatikan satu pola di sini, karena pola ini muncul lagi di backpropagation. Untuk satu sampel, gradient-nya sama dengan error dikali input.

## Overfitting, underfitting, bias dan variance

Gambaran ini membantu. Bayangkan Anda memanah sebuah sasaran berkali-kali, dan setiap kali dengan training set yang baru. Bias adalah seberapa jauh pusat sebaran anak panah dari titik tengah sasaran. Variance adalah seberapa lebar anak panah itu tersebar.

Model yang terlalu sederhana punya bias tinggi. Ia tidak mampu mengikuti data, jadi terjadi underfitting. Model yang terlalu kompleks punya variance tinggi. Ia mengikuti noise di setiap training set, sehingga training error rendah tetapi test error tinggi. Itulah overfitting.

Rumus di balik gambaran tadi: nilai harapan galat kuadrat sama dengan noise, ditambah bias kuadrat, ditambah variance. Rumus ini diturunkan dengan menambah dan mengurangi rata-rata prediksi model. Suku silangnya punya rata-rata nol, jadi hilang.

Tambahan modern: network yang sangat besar menunjukkan double descent. Setelah melewati titik di mana network persis mencocokkan data training, test error justru turun lagi. Sebutkan dalam satu kalimat saja. Ini menunjukkan Anda tahu kurva klasik belum menceritakan semuanya.

## Maximum likelihood

Profesor Widmer beberapa kali menanyakan ini. Maximum likelihood memilih parameter yang membuat data yang teramati paling mungkin terjadi. Yang dimaksimalkan adalah log-likelihood, karena penjumlahan lebih mudah daripada perkalian.

Hubungan yang rapi: squared loss sama dengan maximum likelihood di bawah noise Gaussian. Tuliskan likelihood Gaussian, ambil minus log-nya, dan satu-satunya bagian yang bergantung pada bobot adalah jumlah galat kuadrat.

Kelemahannya: dengan data sedikit, maximum likelihood mudah overfitting. Kejadian yang belum pernah terlihat mendapat probabilitas nol. Sebuah prior, yang menghasilkan MAP estimation, atau regularisasi, bisa mengatasinya.

## Tiga hal untuk diingat

Pertama. Data, model, loss, rata-rata, minimalkan: itulah empirical risk minimization.

Kedua. Generalization error membutuhkan distribusi yang tidak diketahui, jadi diperkirakan dengan test set atau cross-validation, tidak pernah dengan data training.

Ketiga. Model sederhana punya bias, model kompleks punya variance, dan network yang sangat besar menunjukkan double descent.
