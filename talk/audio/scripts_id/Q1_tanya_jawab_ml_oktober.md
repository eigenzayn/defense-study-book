# Q1 · Tanya jawab: Machine Learning, Oktober 2026

Ini soal-soal machine learning dari sidang bulan Oktober 2026, bersama Profesor Hochreiter dan Profesor Schlüter. Setelah setiap soal ada jeda singkat. Jawab dulu dengan suara keras. Lalu dengarkan jawaban contohnya. Kalimat pertama adalah bagian yang dihafal. Sesudahnya kita turunkan rumusnya langkah demi langkah, supaya Anda bisa menurunkannya di papan tulis, bukan sekadar menghafal.

## 1 · Bagaimana nilai satu neuron dihitung?

Soal 1. How is the value of a single neuron computed?

Neuron menjumlahkan input yang sudah diberi bobot, menambahkan bias, lalu melewatkan hasilnya ke fungsi aktivasi yang non-linear.

Mari kita bangun. Neuron menerima input a satu sampai a n dari layer di bawahnya. Setiap input punya bobotnya sendiri, w j. Kita kalikan, kita jumlahkan, lalu kita tambah bias b. Angka ini disebut pre-activation, s, yaitu jumlah dari w j kali a j, ditambah b. Kemudian kita terapkan fungsi aktivasi, sehingga outputnya a sama dengan f dari s. Dua langkah yang perlu diingat: jumlahkan dulu, lalu bengkokkan.

## 2 · Apa itu deep learning, dan apa yang terjadi di dalam layer?

Soal 2. What is deep learning? What is a layer, and what happens in a layer?

Deep learning melatih jaringan dengan banyak layer secara end to end, dan setiap layer mengubah representasi dari layer di bawahnya menjadi representasi yang lebih berguna.

Sekarang dari satu neuron ke satu layer. Layer adalah banyak neuron yang membaca input yang sama. Setiap neuron punya satu baris bobot. Kalau baris-baris ini kita tumpuk, kita dapat matriks bobot W, dan bias-biasnya membentuk vektor b. Jadi seluruh layer menghitung s sama dengan W kali a, ditambah b, lalu a baru sama dengan f dari s, elemen demi elemen. Jaringan mengulang ini dari layer ke layer. Layer awal menemukan fitur sederhana, misalnya tepi. Layer berikutnya menggabungkannya menjadi bagian dan objek. Fitur ini tidak kita rancang dengan tangan. Jaringan mempelajarinya dari data. Jadi layer itu linear, lalu dibengkokkan. Dan deep artinya fitur yang dibangun dari fitur.

## 3 · Apa bedanya jaringan dengan dan tanpa fungsi aktivasi?

Soal 3. What is the difference between a deep network with and without activation functions?

Tanpa fungsi aktivasi, seluruh jaringan runtuh menjadi satu pemetaan linear, sehingga kedalaman tidak menambah apa-apa.

Buktinya cukup dua baris. Ambil dua layer tanpa f. Layer pertama menghasilkan W satu x ditambah b satu. Layer kedua menghasilkan W dua dikali hasil tadi, ditambah b dua. Kita kalikan keluar: W dua W satu x, ditambah W dua b satu ditambah b dua. Sekarang sebut W dua W satu sebagai matriks baru, W aksen, dan sisanya sebagai bias baru, b aksen. Hasilnya W aksen x ditambah b aksen, yaitu lagi-lagi satu layer linear. Ini berlaku untuk berapa pun jumlah layernya. Model linear bahkan tidak bisa menyelesaikan XOR. Non-linearitaslah yang membuat kedalaman berguna.

## 4 · Bolehkah fungsi aktivasi linear?

Soal 4. Can an activation function be linear?

Di output, boleh, untuk regresi. Di hidden layer, tidak, karena linear kali linear tetap linear.

Jawaban sebelumnya adalah alasan untuk hidden layer. Untuk output, lihat targetnya. Pada regresi, target bisa berupa bilangan real berapa saja, jadi tidak boleh kita tekan ke dalam rentang tertentu. Output linear, yaitu fungsi identitas, adalah pilihan yang tepat. Dengan squared loss, deltanya juga bersih, prediksi dikurangi target. Aturannya sederhana. Linear di output untuk regresi. Non-linear di setiap hidden layer.

## 5 · Supervised atau unsupervised?

Soal 5. Supervised or unsupervised learning: what is the difference, and why choose one?

Supervised learning punya label untuk setiap input dan mempelajari pemetaan dari input ke label, sedangkan unsupervised learning tidak punya label dan mencari struktur di dalam input.

Pada supervised learning, datanya berupa pasangan x dan y, dan model belajar memprediksi y dari x. Klasifikasi dan regresi termasuk supervised. Pada unsupervised learning, kita hanya punya x. Kita mencari cluster, densitas data, atau beberapa arah utama seperti pada PCA. Self-supervised learning ada di tengah. Ia membuat labelnya sendiri dari data, misalnya dengan memprediksi kata berikutnya. Bagaimana memilih? Kalau saya punya target yang jelas dan data berlabel, saya pilih supervised. Kalau tidak ada label, atau saya ingin menjelajahi data dulu, saya pilih unsupervised.

## 6 · Tuliskan empirical risk minimization

Soal 6. Write down empirical risk minimization.

True risk tidak bisa kita hitung, jadi ekspektasi loss kita ganti dengan rata-ratanya pada data training, lalu rata-rata itu kita minimalkan.

Mari kita turunkan. Kita punya N pasangan data, x n dan y n, yang diambil secara independen dari distribusi p dari x dan y yang tidak diketahui. Model g memetakan x ke prediksi, y topi, dan punya parameter w. Loss L dari y dan y topi menyatakan seberapa salah satu prediksi. Yang sebenarnya kita inginkan adalah true risk yang kecil. Itu adalah ekspektasi loss, R dari g, sama dengan ekspektasi terhadap p dari L dari y dan g dari x. Tetapi p tidak diketahui, jadi ekspektasi ini tidak bisa dihitung. Hukum bilangan besar menolong kita. Rata-rata sampel mendekati ekspektasi. Jadi ekspektasi kita ganti dengan rata-rata atas data kita. Hasilnya empirical risk, R topi, sama dengan satu per N, kali jumlah atas n dari L dari y n dan g dari x n. Training berarti meminimalkan R topi terhadap w.

Contoh sederhananya regresi linear. Modelnya w transpose x, dan lossnya squared error. Jadi R topi adalah satu per N kali jumlah dari y n dikurangi w transpose x n, dikuadratkan. Kita samakan gradiennya dengan nol. Hasilnya X transpose X kali w sama dengan X transpose y. Jadi w sama dengan invers dari X transpose X, dikali X transpose y. Inilah normal equations, solusi least squares.

## 7 · Empirical error dan generalization error

Soal 7. What is the difference between the empirical error and the generalization error?

Empirical error adalah rata-rata loss pada data training, sedangkan generalization error adalah ekspektasi loss pada data baru dari distribusi yang sama.

Keduanya berbeda karena satu alasan. Bobot kita pilih dengan melihat data training. Jadi training error adalah perkiraan yang terlalu optimis, bias ke bawah. Generalization error adalah true risk dari jawaban sebelumnya, dan kita memperkirakannya pada data yang belum pernah dilihat model, yaitu test set atau cross-validation. Selisih keduanya disebut generalization gap. Gap yang besar berarti overfitting. Menurut teori, gap ini membesar seiring kapasitas model, misalnya VC dimension, dan mengecil seiring bertambahnya jumlah sampel N. Jadi lebih banyak data atau model yang lebih sederhana memperkecil gap.

## 8 · Jelaskan gradient descent dan weight update

Soal 8. Explain gradient descent and the weight update.

Gradient descent menggeser bobot satu langkah kecil melawan arah gradien, w menjadi w dikurangi eta kali gradien empirical risk.

Mengapa tanda minus? Pakai ekspansi Taylor orde pertama. Kalau bobot kita ubah sebesar delta w yang kecil, risk berubah kira-kira sebesar gradien, ditranspose, dikali delta w. Sekarang pilih delta w sama dengan minus eta kali gradien. Maka perubahan risk adalah minus eta kali kuadrat norma gradien. Kuadrat norma tidak pernah negatif. Jadi untuk eta yang cukup kecil, risk pasti turun. Itulah seluruh idenya. Gradien menunjuk ke atas bukit, jadi kita melangkah ke arah sebaliknya. Eta, learning rate, menentukan besar langkahnya.

## 9 · Mengapa memakai mini-batch?

Soal 9. Why do we use mini-batches?

Mini-batch memberi perkiraan gradien penuh yang unbiased dan murah, bisa dihitung paralel di GPU, dan noise kecilnya membantu generalisasi.

Alasannya dalam simbol. Empirical risk adalah rata-rata atas N sampel. Jadi gradiennya juga rata-rata, yaitu rata-rata gradien per sampel. Sekarang ambil B sampel secara acak dan rata-ratakan hanya gradien mereka. Nilai harapan dari rata-rata ini adalah gradien penuh, jadi perkiraannya unbiased. Variansnya adalah varians per sampel dibagi B. Jadi standar deviasinya turun seperti satu per akar B, sedangkan biayanya naik seperti B. Menggandakan batch berarti biaya dua kali lipat, tetapi noise hanya berkurang sekitar tiga puluh persen. Karena itu batch yang sedang adalah kompromi terbaik. Sisa noise-nya justru berguna, karena membantu keluar dari minimum yang tajam.

## 10 · Turunkan backpropagation dan delta error

Soal 10. Derive backpropagation and the recursive formula for the delta errors.

Delta sebuah unit adalah turunan loss terhadap pre-activation-nya, gradien bobot adalah delta di atas dikali aktivasi di bawah, dan delta dihitung mundur dengan chain rule.

Langkah satu, definisi. Delta i sama dengan turunan parsial L terhadap s i.

Langkah dua, gradien bobot. Bobot w i j memengaruhi loss hanya lewat s i. Jadi menurut chain rule, turunan L terhadap w i j adalah delta i kali turunan s i terhadap w i j. Dan s i adalah jumlah berbobot, jumlah atas j dari w i j kali a j. Turunannya terhadap w i j cukup a j. Jadi gradiennya delta i kali a j.

Langkah tiga, rekursi. Unit tersembunyi j memengaruhi loss hanya lewat unit-unit k di layer berikutnya. Jadi kita jumlahkan semua jalur itu. Turunan L terhadap s j adalah jumlah atas k dari tiga faktor. Pertama, turunan L terhadap s k, yaitu delta k. Kedua, turunan s k terhadap a j, yaitu bobot w k j. Ketiga, turunan a j terhadap s j, yaitu f aksen dari s j. Jadi delta j sama dengan f aksen dari s j, dikali jumlah atas k dari w k j kali delta k.

Langkah empat, titik awal. Di output, untuk squared loss setengah kali a dikurangi y, dikuadratkan, deltanya adalah a dikurangi y, dikali f aksen dari s. Lalu kita bergerak mundur, layer demi layer. Dalam bentuk matriks: kalikan delta di atas dengan W transpose, lalu kalikan elemen demi elemen dengan f aksen. Satu forward pass dan satu backward pass memberi semua gradien, dengan biaya yang linear terhadap jumlah bobot.

## 11 · Delta output untuk softmax dengan cross-entropy

Soal 11. What is the output delta for softmax with cross-entropy?

Hasilnya sederhana: prediksi dikurangi label, a i dikurangi y i.

Mari kita turunkan. Output softmax adalah a k sama dengan e pangkat s k, dibagi jumlah atas semua kelas dari e pangkat s. Loss cross-entropy dengan label one-hot adalah L sama dengan minus jumlah atas k dari y k kali log a k. Pertama kita butuh turunan softmax. Dengan aturan hasil bagi, turunan a k terhadap s i adalah a k kali, satu jika k sama dengan i, dikurangi a i. Sekarang pakai chain rule. Turunan L terhadap s i adalah minus jumlah atas k dari y k per a k, dikali turunan softmax tadi. Faktor a k saling menghapus. Kita dapat minus y i, ditambah a i kali jumlah atas k dari y k. Label one-hot jumlahnya satu. Jadi deltanya a i dikurangi y i. Hasil bersih yang sama juga berlaku untuk sigmoid dengan binary cross-entropy, dan untuk output linear dengan squared loss.

## 12 · Klasifikasi biner: mengapa sigmoid, dan mengapa bukan step function?

Soal 12. Binary classification with labels 0 and 1: what is the output, why a sigmoid, and could we use a step function instead?

Outputnya adalah probabilitas kelas satu, sigmoid memberi nilai halus antara nol dan satu, dan step function tidak bisa dilatih dengan backpropagation karena turunannya nol hampir di mana-mana.

Pertama sigmoid. Sigma dari s sama dengan satu per satu ditambah e pangkat minus s. Turunannya adalah e pangkat minus s, dibagi satu ditambah e pangkat minus s, dikuadratkan. Ini bisa ditulis sebagai sigma kali, satu dikurangi sigma. Jadi kemiringannya paling besar di s sama dengan nol, yaitu setengah kali setengah, seperempat.

Sekarang lossnya. Binary cross-entropy adalah L sama dengan minus, y log a, ditambah satu dikurangi y, kali log dari satu dikurangi a. Turunannya terhadap a adalah a dikurangi y, dibagi a kali satu dikurangi a. Kalikan dengan kemiringan sigmoid, a kali satu dikurangi a. Faktor-faktor ini saling menghapus, dan deltanya a dikurangi y. Bersih, dan tidak pernah macet.

Sekarang step function. Untuk keputusan akhir, hasilnya sama dengan threshold di setengah. Tetapi turunannya nol di mana-mana kecuali di nol, dan di nol turunannya tidak terdefinisi. Jadi semua delta bernilai nol, dan tidak ada bobot yang berubah. Perceptron zaman dulu memang memakai step, tetapi dengan aturan update-nya sendiri, bukan backpropagation. Tangga yang datar berarti gradien nol, dan gradien nol berarti tidak belajar.

## 13 · Fungsi aktivasi apa saja, dan mana yang dari Linz?

Soal 13. Which activation functions do you know, and which one is from Linz?

Sigmoid, tanh, ReLU, leaky ReLU dan GELU, dan dari Linz ada ELU dan SELU, yang membuat jaringan self-normalizing.

Sigmoid dan tanh halus, tetapi mengalami saturasi. Tadi kita turunkan bahwa kemiringan sigmoid paling besar seperempat, sehingga jaringan dalam dengan sigmoid kehilangan gradiennya. ReLU, yaitu maksimum dari nol dan s, punya kemiringan satu untuk input positif, jadi tidak saturasi di sana. Tetapi unit yang inputnya selalu negatif tidak akan pernah belajar lagi, disebut dead unit. ELU, dari Clevert, Unterthiner dan Hochreiter, mengganti bagian negatif dengan alpha kali, e pangkat s, dikurangi satu. Fungsinya halus dan mendorong rata-rata aktivasi ke nol. SELU, dari Klambauer dan kawan-kawan tahun 2017, mengalikan ELU dengan konstanta lambda. Dengan lambda sekitar 1,0507 dan alpha sekitar 1,6733, rata-rata dan varians aktivasi ditarik ke nol dan satu, layer demi layer, tanpa batch normalization.

## 14 · Learning rate: mengapa kecil, mengapa besar?

Soal 14. How does the learning rate influence training? Why small, why large?

Learning rate adalah ukuran langkah, terlalu kecil membuat training lambat, terlalu besar membuat loss berosilasi atau divergen.

Batasnya bisa kita lihat dengan model sederhana. Di dekat minimum, loss sepanjang satu arah berbentuk parabola, setengah kali h kali w kuadrat, dengan h adalah kelengkungan. Gradiennya h kali w. Jadi satu langkah memberi w baru sama dengan w dikurangi eta h w, yaitu satu dikurangi eta h, dikali w. Setiap langkah mengalikan jarak ke minimum dengan faktor satu dikurangi eta h. Kalau faktor ini di antara minus satu dan satu, kita konvergen. Artinya eta harus lebih kecil dari dua per h. Kalau eta sangat kecil, faktornya hampir satu, jadi kita merayap. Kalau eta lebih besar dari dua per h, besar faktornya lebih dari satu, dan kita makin menjauh setiap langkah. Itulah divergensi. Dalam praktik kita pakai learning rate sedang, warm-up singkat, lalu decay, misalnya cosine schedule.

## 15 · Learning rate dan batch size

Soal 15. Learning rate versus batch size: how are they related?

Batch yang lebih besar memberi gradien yang lebih sedikit noise-nya, jadi boleh melangkah lebih besar, dan aturan yang umum menskalakan learning rate secara linear dengan batch size.

Inilah argumen linear scaling rule, dari Goyal dan kawan-kawan tahun 2017. Ambil k langkah kecil, masing-masing dengan batch size B dan learning rate eta. Kalau gradien hanya sedikit berubah selama langkah-langkah ini, total pergeserannya kira-kira eta dikali jumlah k perkiraan gradien. Sekarang ambil satu langkah besar dengan batch size k kali B. Gradiennya adalah rata-rata dari k kali B sampel yang sama. Supaya bergeser sejauh yang sama, langkah ini butuh learning rate k kali eta. Jadi kalikan batch dengan k, dan kalikan learning rate dengan k. Noise juga bercerita hal yang sama: noise langkah naik bersama eta dan turun bersama B, jadi rasio eta per B menentukan tingkat noise. Aturan ini gagal di awal training, karena itu kita pakai warm-up, dan pada batch yang sangat besar, karena gradiennya sudah hampir tepat.

## 16 · Gradient descent dan Adam pada mini-batch

Soal 16. Gradient descent versus Adam on mini-batches: how does each one use the data?

Keduanya melangkah sekali per mini-batch, tetapi SGD hanya memakai gradien saat ini dengan satu learning rate global, sedangkan Adam menyimpan rata-rata berjalan dari gradien sebelumnya dan memberi setiap bobot ukuran langkahnya sendiri.

Pertama datanya. Kita acak training set, memotongnya menjadi mini-batch, dan melangkah sekali per batch. Satu putaran atas semua batch disebut satu epoch. Kedua optimizer bekerja seperti ini.

Sekarang Adam. Misalkan g adalah gradien batch saat ini. Adam menyimpan momen pertama, m sama dengan beta satu kali m, ditambah satu dikurangi beta satu, kali g. Ini momentum, rata-rata atas batch-batch sebelumnya. Adam juga menyimpan momen kedua, v, rata-rata yang sama tetapi dari g kuadrat. Keduanya mulai dari nol, jadi di langkah-langkah awal nilainya terlalu kecil. Kalau m kita uraikan, nilai harapannya adalah rata-rata sebenarnya dikali satu dikurangi beta satu pangkat t. Jadi kita bagi dengan faktor itu. Inilah bias correction, m topi dan v topi. Langkahnya eta kali m topi, dibagi akar v topi ditambah epsilon.

Mengapa ini membantu? Misalkan semua gradien sebuah bobot dikalikan konstanta c. Maka m topi naik c kali dan akar v topi juga naik c kali. Langkahnya tetap sama. Jadi Adam tidak peduli skala setiap gradien, dan setiap bobot mendapat langkah yang wajar. SGD biasa melupakan batch-batch sebelumnya. Adam mengingatnya.

## 17 · Optimizer apa saja? AdamW dan Adam dengan L2

Soal 17. Which optimizers do you know? What is the difference between AdamW and Adam with L2?

SGD, momentum, Nesterov, AdaGrad, RMSprop, Adam dan AdamW, dan AdamW menerapkan weight decay langsung pada bobot, bukan lewat pembagian adaptif.

Mari kita bandingkan. Dengan L2 kita menambahkan lambda per dua kali kuadrat norma w ke loss. Gradiennya lambda kali w. Untuk SGD biasa, update-nya menjadi w dikurangi eta, kali g ditambah lambda w. Ini bisa ditulis sebagai satu dikurangi eta lambda, kali w, dikurangi eta g. Jadi bobot menyusut dengan faktor tetap setiap langkah. Untuk SGD, L2 dan weight decay sama saja.

Untuk Adam tidak. Suku lambda w masuk ke momen-momen, lalu dibagi akar v topi. Bobot dengan gradien besar punya v topi yang besar, jadi decay-nya menjadi kecil. Regularisasinya paling lemah justru di bobot yang paling banyak bergerak. AdamW, dari Loshchilov dan Hutter, memisahkan keduanya. Update-nya w dikurangi eta, kali m topi per akar v topi, ditambah lambda w. Sekarang decay ada di luar pembagian, dan setiap bobot menyusut dengan laju yang sama. Ingat: AdamW menaruh decay di luar pembagian.

## 18 · Apa itu vanishing dan exploding gradient?

Soal 18. What are vanishing and exploding gradients?

Delta di layer awal adalah hasil kali satu faktor per layer, sehingga ia menyusut ke nol atau membesar tanpa batas kalau faktor-faktor ini di bawah atau di atas satu.

Kembali ke rekursi. Delta sebuah layer adalah f aksen kali W transpose kali delta layer di atasnya. Terapkan berulang kali. Delta layer pertama adalah hasil kali atas semua layer dari f aksen dan W transpose. Sekarang ambil normanya. Besar hasil kali ini paling banyak hasil kali spectral norm semua W, dikali kemiringan terbesar f, untuk setiap layer. Dengan sigmoid, kemiringan terbesarnya seperempat. Jadi kalau seperempat kali norma W di bawah satu, delta menyusut seperti bilangan itu dipangkatkan kedalaman. Itu peluruhan eksponensial. Kalau faktornya di atas satu, delta tumbuh secara eksponensial. Sepp Hochreiter menganalisis masalah ini dalam tesis diplomanya tahun 1991, di Linz.

## 19 · Cara mengatasi vanishing gradient, dan struktur W yang diinginkan

Soal 19. How can we mitigate vanishing gradients, and which structure do we want for W during learning?

Kita jaga setiap faktor dalam hasil kali mundur tetap dekat dengan satu, dan idealnya W dekat dengan isometri, dengan singular value mendekati satu.

Dari jawaban tadi, semua solusi punya tujuan yang sama. Inisialisasi yang cermat mengatur skala yang benar sejak awal. Aktivasi seperti ReLU, ELU atau SELU punya kemiringan satu, atau mendekati satu, bukan seperempat. Layer normalisasi menjaga aktivasi pada skala tetap. Residual connection mengubah layer menjadi a baru sama dengan a ditambah F dari a. Maka Jacobian-nya adalah identitas ditambah Jacobian dari F. Hasil kali suku-suku berbentuk satu ditambah sesuatu yang kecil tidak menghilang. Untuk sekuens, LSTM menyimpan memory cell dengan aliran error yang konstan. Dan gradient clipping membatasi ledakan.

Struktur apa untuk W? Kalau semua singular value W sama dengan satu, W ortogonal. Ia memutar vektor tetapi tidak meregangkannya, jadi sinyal dan delta tetap berukuran sama. Itulah ide orthogonal initialization. Selama training, bobot mempelajari struktur dan normanya cenderung membesar. Kita ingin spectral norm tetap terbatas, misalnya lewat weight decay atau spectral normalization.

## 20 · Inisialisasi bobot, dan mengapa varians ini

Soal 20. Which initialization techniques do you know, and why do we use this variance?

Inisialisasi LeCun, Glorot dan He memilih varians bobot sehingga varians sinyal tetap sama dari layer ke layer.

Mari kita turunkan. Pre-activation adalah s sama dengan jumlah atas n in suku dari w j kali a j. Anggap bobot independen dari input dan rata-ratanya nol. Varians dari jumlah suku-suku independen adalah jumlah variansnya. Setiap suku punya varians sama dengan varians w kali rata-rata kuadrat a. Jadi varians s adalah n in, kali varians w, kali rata-rata kuadrat a. Kita ingin ini tetap konstan dari layer ke layer. Jadi kita pilih varians w sama dengan satu per n in. Itulah inisialisasi LeCun, yang dipakai bersama SELU.

Untuk ReLU, separuh input menjadi nol, jadi rata-rata kuadrat a hanya separuh varians s. Untuk mengimbanginya, varians bobot kita gandakan: dua per n in. Itulah inisialisasi He.

Backward pass punya masalah yang sama, tetapi delta dijumlahkan atas n out unit. Di sana kita butuh satu per n out. Glorot, yang juga disebut Xavier, mengambil kompromi: dua per jumlah n in dan n out. Lalu mengapa tidak nol semua? Karena semua unit dalam satu layer akan menghitung hal yang sama dan mendapat update yang sama, sehingga tidak pernah berbeda. Bobot acak memecah simetri ini.

## 21 · Spectral norm dan mengapa penting

Soal 21. What is the spectral norm of a weight matrix, and why does it matter?

Spectral norm adalah singular value terbesar dari W, yaitu faktor terbesar yang dapat dipakai layer untuk meregangkan sebuah vektor.

Definisinya adalah maksimum, atas semua x bukan nol, dari norma W x dibagi norma x. Kalau dikuadratkan, kita dapat x transpose W transpose W x per x transpose x. Rasio itu paling besar untuk eigenvector teratas dari W transpose W. Jadi spectral norm adalah akar dari eigenvalue terbesar W transpose W, yaitu singular value terbesar.

Mengapa penting? Ambil dua input, x dan x aksen. Satu layer meregangkan selisih keduanya paling banyak sebesar spectral norm W. Aktivasi seperti ReLU atau tanh punya kemiringan paling besar satu, jadi tidak meregangkan lebih jauh. Rangkaikan semua layer. Selisih output paling besar hasil kali semua spectral norm, dikali selisih input. Jadi hasil kali ini membatasi konstanta Lipschitz jaringan. Hasil kali yang besar berarti sinyal meledak dan jaringan sensitif terhadap perubahan kecil pada input. Spectral normalization membagi W dengan spectral norm-nya, dipakai untuk robustness dan pada GAN.

## 22 · Batch norm, layer norm dan RMSNorm

Soal 22. Which normalizations do you know, and which one is popular now?

Batch norm menormalkan setiap fitur atas mini-batch, layer norm menormalkan atas fitur-fitur satu sampel, dan RMSNorm, yang populer sekarang, hanya membagi dengan root mean square tanpa mengurangi rata-rata.

Mari kita tulis sebagai satu resep. Ambil sekumpulan angka. Kurangi dengan rata-ratanya, mu. Bagi dengan standar deviasinya, akar dari varians ditambah epsilon kecil. Lalu skalakan dengan gain yang dipelajari, gamma, dan geser dengan beta yang dipelajari. Pertanyaannya hanya kumpulan angka mana yang dipakai. Batch norm memakai satu fitur di semua sampel dalam batch. Jadi ia bergantung pada batch, butuh running statistics saat testing, dan kesulitan dengan batch kecil. Layer norm memakai semua fitur dari satu sampel. Ia bekerja sama saat training dan testing, jadi cocok untuk transformer dan recurrent network. RMSNorm, dari Zhang dan Sennrich, membuang rata-rata. Ia membagi x dengan akar dari satu per d kali jumlah x kuadrat, ditambah epsilon, lalu mengalikan dengan gain. Idenya, yang menstabilkan training adalah penskalaan ulang, bukan pemusatan ulang. Lebih murah dan sama bagusnya, sehingga large language model seperti LLaMA memakainya.

## 23 · Teknik regularisasi apa saja?

Soal 23. Which regularization techniques do you know?

Weight decay, dropout, early stopping, data augmentation dan noise, dan semuanya memperkecil jarak antara training error dan test error.

Mari kita turunkan nama weight decay. Kita tambahkan lambda per dua kali kuadrat norma w ke empirical risk. Gradiennya bertambah lambda kali w. Jadi update-nya w dikurangi eta, kali gradien risk ditambah lambda w. Kalau disusun ulang, itu satu dikurangi eta lambda, kali w, dikurangi eta kali gradien risk. Sebelum setiap langkah biasa, bobot menyusut dengan faktor satu dikurangi eta lambda. Bobotnya meluruh. L1 sebaliknya menambahkan jumlah nilai mutlak dan mendorong bobot tepat ke nol, jadi modelnya menjadi sparse.

Dropout mematikan setiap unit dengan peluang tertentu selama training. Kita pertahankan unit dengan peluang p dan membagi outputnya dengan p. Maka output yang diharapkan tetap sama, sehingga tidak ada yang berubah saat testing. Jaringan tidak bisa bergantung pada satu unit saja. Early stopping menghentikan training ketika validation error mulai naik. Data augmentation menambahkan salinan input yang ditransformasi, misalnya dibalik atau dipotong.

## 24 · Primal SVM, dan angka satu yang terkenal

Soal 24. Write down the SVM primal. What do we optimize, where does the 1 in the constraints come from, and could we use another value?

Kita memaksimalkan margin, dan angka satu hanya menetapkan skala w dan b, sehingga nilai positif berapa pun memberi hyperplane yang sama.

Mulai dari geometri. Jarak titik x i ke hyperplane w transpose x ditambah b sama dengan nol adalah nilai mutlak dari w transpose x i ditambah b, dibagi norma w. Sekarang perhatikan ada skala bebas. Kalau w dan b dikalikan konstanta positif berapa pun, hyperplane-nya tetap sama. Jadi skalanya boleh kita tetapkan. Kita pilih supaya titik-titik terdekat memberi y i kali, w transpose x i ditambah b, tepat sama dengan satu. Inilah canonical form, atau canonical hyperplane. Maka titik terdekat berjarak satu per norma w, di setiap sisi. Marginnya dua per norma w.

Memaksimalkan dua per norma w sama dengan meminimalkan normanya. Kita meminimalkan setengah kuadrat norma, karena halus dan konveks, dan setengahnya membuat turunannya bersih. Jadi primalnya: minimalkan setengah kuadrat norma w, dengan syarat y i kali, w transpose x i ditambah b, minimal satu, untuk setiap i. Dengan slack variable xi i dan penalti C, kita dapat soft margin.

Bolehkah memakai c sebagai pengganti satu? Boleh. Ambil w aksen sama dengan w per c, dan b aksen sama dengan b per c. Syarat dengan c berubah menjadi syarat dengan satu untuk w aksen. Solusinya hanya diskalakan, hyperplane yang sama dan classifier yang sama. Satu hanyalah pilihan yang paling alami.

## 25 · Receptive field pada CNN

Soal 25. What is the receptive field of a CNN, how can we increase it, and what does pooling do?

Receptive field adalah bagian input yang dapat memengaruhi satu unit, dan ia membesar dengan kedalaman, ukuran kernel, stride atau pooling, dan dilation.

Mari kita turunkan pertumbuhannya. Mulai dari satu piksel input, receptive field-nya satu. Konvolusi dengan ukuran kernel k melihat k tetangga, jadi menambah k dikurangi satu ke receptive field. Tetapi di layer yang lebih dalam, tetangga tidak berjarak satu piksel input. Jaraknya sebesar hasil kali semua stride sebelumnya. Sebut ini jump, j. Jadi aturannya: r baru sama dengan r lama, ditambah k dikurangi satu, kali j. Contoh: tiga layer tiga kali tiga, stride satu. Masing-masing menambah dua, jadi receptive field-nya satu ditambah dua ditambah dua ditambah dua, yaitu tujuh. Kalau ada layer pooling dengan stride dua sebelumnya, jump-nya berlipat dua, dan setiap layer sesudahnya menambah dua kali lebih banyak. Dilated convolution dengan dilation d meregangkan kernel, sehingga mencakup d kali k dikurangi satu, ditambah satu posisi input, dengan jumlah bobot yang sama.

Pooling mengambil maksimum atau rata-rata dalam jendela kecil. Ia tidak punya bobot, memperkecil peta, memperbesar receptive field layer berikutnya, dan menambah sedikit invariansi terhadap pergeseran kecil. Global average pooling memberi satu vektor untuk seluruh gambar atau seluruh sekuens.
