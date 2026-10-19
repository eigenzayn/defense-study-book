# M5 · Machine learning klasik, REINFORCE, dan evaluasi model

Episode ML&P terakhir membahas pertanyaan yang berada di samping deep learning: support vector machine, kernel, VC dimension, loss REINFORCE, serta cara mengevaluasi dan menguji ketahanan sebuah classifier. Sebagian pernah ditanyakan Profesor Kofler dan Profesor Hochreiter, jadi layak diperhatikan.

## Support vector machine

Idenya dalam satu kalimat: SVM mencari hyperplane pemisah dengan margin terbesar.

Bayangkan sebuah jalan di antara dua kelompok rumah. SVM membangun jalan yang selebar mungkin, dan rumah-rumah yang menyentuh tepi jalan disebut support vector. Hanya merekalah yang menentukan letak jalan.

Margin-nya sama dengan dua dibagi norma w. Jadi memaksimalkan margin berarti meminimalkan norma w kuadrat. Pada versi soft-margin, sebagian titik boleh berada di dalam margin. Hal itu diizinkan lewat slack variable, dan dibayar dengan penalti C. Jadi yang diminimalkan adalah setengah norma w kuadrat, ditambah C dikali jumlah slack, dengan syarat setiap titik berada di sisi yang benar, sejauh slack-nya.

Pada dual problem, yang muncul hanyalah perkalian titik antar data. Titik-titik dengan alpha n lebih besar dari nol adalah support vector.

## Kernel dan kernel trick

Kernel adalah perkalian titik di sebuah feature space, yang dihitung tanpa membangun feature-nya.

Contoh klasiknya begini. Ambil polynomial kernel di dua dimensi: x transpose x aksen, dikuadratkan. Kalikan semuanya, dan hasilnya persis perkalian titik dua vektor feature, dengan feature x satu kuadrat, akar dua kali x satu x dua, dan x dua kuadrat. Jadi kernel menghitung perkalian titik di feature space tiga dimensi itu, tanpa pernah membangunnya.

Karena dual SVM hanya membutuhkan perkalian titik, perkalian itu bisa diganti dengan kernel. Hasilnya classifier non-linear dengan biaya classifier linear. Contohnya polynomial kernel dan Gaussian kernel.

## VC dimension

VC dimension adalah jumlah titik terbanyak yang bisa diberi label oleh sebuah kelas model dengan semua kemungkinan cara. Kelas model itu dikatakan mampu shatter himpunan tersebut. VC dimension mengukur kapasitas. Untuk classifier linear di d dimensi, VC dimension-nya d ditambah satu. Dalam generalization bound, jarak antara training error dan test error membesar seiring VC dimension dan mengecil seiring jumlah sampel.

## REINFORCE, ditanyakan Profesor Hochreiter

Kita ingin policy dengan expected return terbesar. Expected return J dari theta adalah integral, untuk semua trajectory, dari probabilitas trajectory dikali return-nya.

Triknya adalah log-derivative trick: gradient dari p sama dengan p dikali gradient log p. Trik ini memindahkan gradient ke dalam nilai harapan, sehingga gradient bisa diperkirakan dari episode yang diambil sampelnya.

Sekarang tulis log-probabilitas sebuah trajectory. Isinya log keadaan awal, ditambah jumlah sepanjang waktu dari log-policy, ditambah log dinamika lingkungan. Lingkungan tidak bergantung pada parameter policy. Jadi saat gradient diambil, hanya suku policy yang tersisa.

Hasilnya: gradient J sama dengan nilai harapan dari jumlah sepanjang waktu, gradient log pi dari a t diberi s t, dikali return G t. Sebagai loss yang diminimalkan, kita tulis minus jumlah log pi dari aksi, dikali return dikurangi sebuah baseline. Baseline tidak mengubah nilai harapan gradient, tetapi mengurangi variansinya.

## Bagaimana mengevaluasi sebuah classifier?

Dengan confusion matrix, precision, recall, dan area di bawah kurva ROC.

Precision: dari semua yang saya sebut positif, berapa yang benar? True positive dibagi true positive ditambah false positive. Recall: dari semua yang benar-benar positif, berapa yang saya temukan? True positive dibagi true positive ditambah false negative. Cara mudah mengingat: precision itu seberapa bersih, recall itu seberapa lengkap.

Kurva ROC menggambarkan true-positive rate terhadap false-positive rate, untuk semua threshold. AUC adalah probabilitas bahwa sebuah sampel positif acak mendapat skor lebih tinggi daripada sampel negatif acak. AUC 0,5 berarti seperti menebak. AUC satu berarti sempurna.

## Bagaimana lagi mengukur robustness?

Profesor Klambauer pernah bertanya: selain adversarial attack, bagaimana lagi mengukur robustness? Uji di bawah distribution shift: input yang rusak, domain baru, data dari waktu yang berbeda. Periksa kalibrasi dan ketidakpastian, dengan ensemble atau Monte Carlo dropout. Dan periksa seberapa sensitif output terhadap perubahan kecil pada input.

Di sini Anda bisa membawa tesis sendiri. Rekaman yang dibuat di bawah satu kondisi batas gagal di kondisi batas lain, karena regime-nya berubah. Itu distribution shift, dalam sebuah simulasi fisika. Jawaban yang kuat dan personal.

## Tiga hal untuk diingat

Pertama. SVM: margin maksimum; dual-nya hanya berisi perkalian titik, jadi kernel memberi classifier non-linear dengan biaya linear. Classifier linear di d dimensi punya VC dimension d ditambah satu.

Kedua. REINFORCE: log-derivative trick, dinamika lingkungan hilang, dan loss-nya minus log pi dikali return dikurangi baseline.

Ketiga. Precision itu seberapa bersih, recall seberapa lengkap, AUC kualitas pemeringkatan. Robustness: distribution shift, kalibrasi, sensitivitas, dan contoh regime dari tesis Anda.
