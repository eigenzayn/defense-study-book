# M2 · Dari satu neuron sampai backpropagation

Topik ini paling sering ditanyakan di seluruh ujian. Profesor Hochreiter, Profesor Klambauer, dan penguji lain menanyakannya berulang kali: jelaskan backpropagation dan definisikan delta error. Targetnya sederhana. Anda harus bisa menuliskannya di papan dalam dua menit, sambil menjelaskan setiap baris yang ditulis. Mari kita ke sana.

## Satu neuron

Sebuah neuron mengambil jumlah berbobot dari input-nya, menambahkan bias, lalu memasukkan hasilnya ke fungsi non-linear. Jumlah berbobot itu disebut pre-activation, s. Hasilnya, a sama dengan f dari s, disebut activation. Satu layer melakukan hal ini untuk banyak neuron sekaligus. Dalam bentuk matriks, activation layer l sama dengan f dari W dikali activation layer di bawahnya, ditambah b. Forward pass berjalan layer demi layer, dari input ke output.

## Kenapa butuh non-linearitas?

Profesor Schlüter pernah bertanya: apa yang terjadi tanpa activation function? Seluruh network runtuh menjadi satu model linear. Kalikan dua pemetaan linear, hasilnya tetap pemetaan linear. Jadi kedalaman tidak menambah apa-apa, dan network bahkan tidak bisa menyelesaikan XOR. Non-linearitaslah yang membuat kedalaman berguna.

## Universal approximation theorem

Satu hidden layer, dengan cukup banyak unit dan activation yang bukan polinomial, misalnya sigmoid, bisa mendekati fungsi kontinu apa pun pada himpunan kompak. Sekarang bagian pentingnya, yaitu batasnya. Teorema ini mengatakan network mampu merepresentasikan fungsinya. Teorema ini tidak mengatakan berapa unit yang dibutuhkan. Dan tidak mengatakan bahwa gradient descent akan menemukan bobotnya. Keberadaan, bukan kemampuan dipelajari.

## Backpropagation: idenya

Masalahnya begini. Sebuah network bisa punya jutaan bobot, dan kita butuh gradient loss untuk setiap bobot. Menghitungnya satu per satu jelas tidak mungkin.

Backpropagation mendapatkan semuanya dengan satu forward pass dan satu backward pass. Bayangkan seperti menelusuri siapa yang bertanggung jawab dalam sebuah tim. Output-nya salah sebesar sekian. Setiap unit menanggung bagian kesalahan, sesuai seberapa besar kontribusinya. Dan bagian kesalahan itu mengalir mundur, layer demi layer. Bagian kesalahan itulah yang disebut delta.

## Definisi delta

Tulis ini lebih dulu: delta i didefinisikan sebagai turunan loss terhadap pre-activation s i.

Sekarang gradient dari bobot w i j. Bobot ini mempengaruhi loss hanya lewat s i. Jadi dengan chain rule, turunan loss terhadap w i j sama dengan delta i, dikali turunan s i terhadap w i j. Karena s i adalah jumlah berbobot, turunan itu tidak lain adalah a j.

Jadi gradient-nya adalah delta i dikali a j. Dengan kata-kata: delta dari unit di atas, dikali activation dari unit di bawah. Kalimat inilah yang ingin didengar penguji.

Dan update-nya: w i j menjadi w i j dikurangi eta, dikali delta i, dikali a j.

## Rekursinya

Pertanyaan berikutnya: bagaimana mendapatkan delta untuk hidden unit? Hidden unit j mempengaruhi loss hanya lewat unit-unit i di layer berikutnya. Jadi kita jumlahkan semua jalur itu.

Delta j sama dengan jumlah, untuk semua i, dari delta i dikali w i j, dikali f aksen dari s j.

Dalam bentuk matriks: ambil delta layer di atas, kalikan dengan transpose matriks bobot, lalu kalikan elemen demi elemen dengan kemiringan activation-nya. Delta mengalir ke bawah: kalikan W transpose, lalu kalikan f aksen.

Gradient untuk satu matriks bobot utuh adalah outer product: vektor delta layer l dikali transpose vektor activation layer di bawahnya. Biayanya linear terhadap jumlah bobot. Itulah sebabnya backprop efisien.

## Delta di output

Profesor Hochreiter menyukai pertanyaan ini: berapa delta di output dengan softmax dan cross-entropy? Jawabannya sederhana sekali. Prediksi dikurangi label.

Anda bisa menurunkannya. Turunan output softmax a k terhadap s i sama dengan a k dikali, satu jika k sama dengan i, dikurangi a i. Masukkan ke turunan cross-entropy, gunakan fakta bahwa label one-hot berjumlah satu, dan semuanya menyusut menjadi a i dikurangi y i.

Hasil yang sama rapinya berlaku untuk output linear dengan squared loss, dan untuk sigmoid dengan binary cross-entropy. Karena itulah pasangan-pasangan ini selalu dipakai bersama.

## Vanishing dan exploding gradient

Lihat lagi rekursinya. Untuk mendapatkan delta layer pertama, kita mengalikan satu Jacobian per layer. Jadi melewati banyak layer, delta mengecil atau membesar secara eksponensial. Dengan sigmoid, kemiringannya paling besar seperempat. Kalau seperempat dikali norma bobot lebih kecil dari satu, delta menghilang ketika network makin dalam.

Dan ada kaitannya dengan Linz: Sepp Hochreiter menganalisis masalah ini dalam tesis diplomanya tahun 1991, di Linz. Kalau penguji bertanya siapa yang menemukannya, itulah jawabannya, dan saat yang tepat untuk tersenyum.

Solusinya: activation ReLU atau SELU, inisialisasi yang baik, normalisasi, residual connection, dan untuk data berurutan, LSTM.

## Tiga hal untuk diingat

Pertama. Delta adalah turunan loss terhadap pre-activation. Gradient sama dengan delta di atas dikali activation di bawah.

Kedua. Delta mengalir ke bawah: kalikan W transpose, lalu f aksen. Di output, softmax dengan cross-entropy memberi prediksi dikurangi label.

Ketiga. Perkalian Jacobian bisa menghilang atau meledak. Hochreiter, 1991, Linz. Solusinya: ReLU atau SELU, inisialisasi, ResNet, LSTM.
