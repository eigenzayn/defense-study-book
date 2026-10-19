# M4 · Arsitektur: CNN, ResNet, RNN, LSTM, dan Transformer

Di kebanyakan ujian, setelah bagian inti, penguji memilih satu arsitektur dan meminta Anda menjelaskannya. Jadi untuk setiap arsitektur, siapkan tiga hal: idenya dalam satu kalimat, kenapa arsitektur itu bekerja, dan satu rumus yang menunjukkannya.

## Convolutional network

Idenya: filter kecil dengan bobot yang dipakai bersama digeser di atas gambar, sehingga sebuah pola bisa ditemukan di mana pun letaknya.

Kenapa cocok untuk gambar? Gambar punya struktur lokal, piksel yang berdekatan saling berkaitan. Dan pola yang sama, misalnya tepi atau mata, bisa muncul di mana saja. Bobot yang dipakai bersama membuat jumlah parameter sedikit dan menghasilkan translation equivariance: geser gambarnya, feature map ikut bergeser. Pooling memperkecil ukuran map dan menambah sedikit invariansi. Layer yang lebih dalam melihat bagian gambar yang lebih luas.

Angka yang perlu diingat: ukuran output sama dengan pembulatan ke bawah dari n ditambah dua p dikurangi k, dibagi s, lalu ditambah satu. Di sini n adalah ukuran input, k ukuran kernel, p padding, dan s stride.

## ResNet dan U-Net

ResNet menambahkan input sebuah blok ke output-nya. Activation berikutnya sama dengan activation sekarang ditambah F dari activation sekarang. Kenapa membantu? Jacobian sebuah residual block adalah identitas ditambah bagian kecil. Jadi delta tidak menyusut, dan gradient bisa melewati network yang sangat dalam. Mirip lift ekspres di samping tangga.

U-Net dipakai untuk segmentasi. Isinya encoder dan decoder dengan skip connection di antara keduanya. U-Net memprediksi satu kelas per piksel, dan skip connection menyalin detail halus dari encoder ke decoder. Profesor Klambauer pernah menanyakan U-Net.

## Recurrent network

Idenya: RNN membaca sebuah urutan langkah demi langkah dan menyimpan hidden state yang membawa informasi masa lalu.

Forward pass-nya: s dari t sama dengan W dikali x dari t, ditambah R dikali a dari t dikurangi satu. Lalu a dari t sama dengan f dari s dari t. Bobot yang sama dipakai di setiap langkah, jadi jumlah parameter tidak bertambah seiring panjang urutan.

Bagaimana cara melatihnya? Dengan backpropagation through time. Bentangkan network sepanjang urutan, lalu lakukan backpropagation seperti pada network dalam dengan bobot yang dipakai bersama. Delta di setiap langkah mendapat dua sumbangan: satu dari output di langkah itu, dan satu dari langkah berikutnya. Karena bobotnya dipakai bersama, gradient-nya dijumlahkan sepanjang waktu.

## Kenapa RNN biasa gagal, dan bagaimana LSTM memperbaikinya

Di setiap langkah mundur dalam waktu, delta dikalikan dengan recurrent Jacobian. Untuk urutan yang panjang, hasil perkaliannya menghilang. Jadi RNN biasa melupakan ketergantungan jarak jauh. Masalah vanishing gradient yang sama, kini terjadi dalam waktu.

LSTM, dari Hochreiter dan Schmidhuber tahun 1997, memperbaikinya dengan memory cell yang diperbarui lewat penjumlahan. Cell c dari t sama dengan forget gate dikali cell lama, ditambah input gate dikali input baru. Output gate menentukan apa yang dibaca dari cell.

Baris kuncinya: turunan c dari t terhadap c dari t dikurangi satu hanyalah forget gate. Ketika forget gate mendekati satu, turunan itu mendekati identitas. Jadi error mengalir mundur sepanjang waktu tanpa menyusut. Inilah constant error carousel. Bayangkan ban berjalan yang membawa ingatan ke depan, dan gate-gate adalah pekerja yang memutuskan apa yang diletakkan di ban, apa yang tetap, dan apa yang diangkat.

## Bidirectional RNN dan label untuk satu urutan

Profesor Schlüter pernah bertanya tentang "RNN dari masa depan". Bidirectional RNN menjalankan satu RNN maju dan satu RNN mundur, lalu menggabungkan state keduanya. Jadi setiap langkah melihat masa lalu dan masa depan. Batasnya: butuh seluruh urutan, jadi tidak cocok untuk penggunaan real-time.

Untuk satu label per urutan, pakai hidden state terakhir, atau gabungkan semua hidden state dengan pooling, lalu pasang classifier di atasnya.

## Attention dan Transformer

Idenya: setiap token mengambil rata-rata berbobot dari semua token, dan bobotnya berasal dari query dikali key.

Setiap token membentuk tiga vektor lewat pemetaan linear: query, key, dan value. Bobot attention adalah softmax dari query dikali key, dibagi akar kuadrat d k. Output-nya mencampur value dengan bobot tersebut.

Kenapa dibagi akar d k? Kalau entri query dan key independen dengan variansi satu, perkalian titiknya bervariansi d k. Membaginya dengan akarnya mengembalikan variansi ke satu, sehingga softmax tidak mengalami saturasi.

Satu blok Transformer berisi multi-head self-attention ditambah MLP, masing-masing dengan residual connection dan layer normalization.

## Dua pertanyaan lanjutan

Profesor Lehner pernah bertanya: Transformer bersifat permutation-equivariant, kenapa itu masalah? Karena self-attention melihat token sebagai sebuah himpunan. Kalau token diacak, output-nya teracak dengan cara yang sama. Urutan kata hilang. Jadi informasi posisi ditambahkan: sinusoid tetap, vektor yang dipelajari, atau relative encoding seperti RoPE.

Dan: bandingkan biaya RNN dan Transformer. RNN linear terhadap panjang urutan, orde N, tetapi berurutan. Transformer kuadratik, orde N kuadrat, karena setiap token memperhatikan setiap token, tetapi semua token diproses paralel, dan jalur jarak jauh hanya satu langkah. Karena itu juga model bergaya LSTM seperti xLSTM kembali menarik: inferensinya linear dalam N.

## Tiga hal untuk diingat

Pertama. CNN: filter lokal, bobot bersama, pooling. ResNet: identitas ditambah residual, jadi Jacobian tetap dekat identitas.

Kedua. RNN: bobot sama di setiap langkah, dilatih dengan backpropagation through time. LSTM: pembaruan cell lewat penjumlahan, jadi dengan forget gate mendekati satu, error terbawa tanpa berubah.

Ketiga. Attention: softmax dari query kali key dibagi akar d k, dikali value. Transformer butuh informasi posisi, berbiaya N kuadrat tetapi berjalan paralel.
