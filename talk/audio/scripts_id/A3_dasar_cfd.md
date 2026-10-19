# A3 · Dasar-dasar CFD di balik recurrence CFD

Episode terakhir membahas dasar CFD dari kuliah Profesor Pirker. Pertanyaan-pertanyaan ini menguji apakah Anda benar-benar paham landasan tempat recurrence CFD berdiri. Triknya sama untuk setiap pertanyaan: sampaikan idenya, berikan satu rumus, lalu kaitkan dengan tesis Anda. Kaitan itulah yang mengubah jawaban buku teks menjadi jawaban Anda sendiri.

## Bilangan tak berdimensi

Bilangan Reynolds membandingkan inersia dengan gaya viskos: U dikali L dibagi nu. Aliran dalam pipa laminar di bawah sekitar 2300, dan turbulen di atas sekitar 4000.

Beberapa yang lain. Bilangan Péclet membandingkan konveksi dengan difusi. Bilangan Prandtl membandingkan difusi momentum dengan difusi panas. Bilangan Froude membandingkan inersia dengan gravitasi. Bilangan Richardson membandingkan gaya apung dengan inersia.

Kasus Anda: bilangan Reynolds sekitar 99, jadi laminar, dan bilangan Richardson 1,84, jadi gaya apung sedikit lebih kuat daripada inersia.

## Persamaan pengatur dan material derivative

Massa, momentum, dan energi bersifat kekal. Ada dua cara melihat aliran. Sudut pandang Lagrangian mengikuti satu parsel fluida. Sudut pandang Eulerian mengamati satu titik tetap.

Material derivative menghubungkan keduanya. Turunan ini adalah laju perubahan yang dialami parsel yang bergerak: perubahan lokal terhadap waktu, ditambah kecepatan dikali gradien. Rumusnya didapat dari chain rule sepanjang lintasan, karena parsel bergerak mengikuti kecepatan.

Persamaan momentum dengan kata-kata: perubahan terhadap waktu ditambah konveksi sama dengan gaya tekanan, ditambah gaya viskos, ditambah gaya badan.

## Metode volume hingga

Integralkan persamaannya pada setiap sel. Teorema divergensi mengubah setiap divergensi menjadi flux yang melewati face. Apa yang keluar dari satu sel masuk ke sel tetangganya, jadi metodenya konservatif.

Setiap nilai sel lalu terhubung dengan tetangganya lewat satu persamaan linear: a P dikali c P sama dengan jumlah koefisien tetangga dikali nilai tetangga, ditambah sumber. Bentuk ini disebut computational molecule.

Kaitannya dengan tesis Anda: kalau semua koefisiennya positif, nilai baru merupakan rata-rata berbobot dari tetangganya, jadi tidak ada ekstrem baru yang muncul. Aturan itulah yang melindungi face exchange di recurrence CFD, dan ide yang sama ada di balik limiter Anda.

## Skema diskretisasi dan difusi numerik

First-order upwind mengambil nilai dari arah hulu. Skema ini stabil, tetapi menambahkan difusi palsu. Central differencing lebih akurat, tetapi bisa berosilasi ketika cell Péclet number lebih dari dua.

Kenapa upwind menimbulkan difusi? Ekspansikan nilai hulu dengan deret Taylor. Selisih upwind sama dengan turunan sebenarnya dikurangi setengah delta x dikali turunan kedua. Jadi persamaan yang sebenarnya diselesaikan upwind punya suku difusi tambahan, dengan difusivitas numerik setengah dikali u dikali delta x.

Dan tesis Anda dalam satu kalimat: sebuah cerita tentang difusi numerik. Face exchange melebarkan front, dan koreksi mengembalikannya.

## Time stepping eksplisit dan implisit

Langkah eksplisit murah tetapi dibatasi kestabilan. Langkah implisit menyelesaikan sistem persamaan, tetapi stabil tanpa syarat.

Untuk konveksi eksplisit, bilangan Courant harus di bawah satu: informasi tidak boleh berpindah lebih dari satu sel per langkah. Untuk difusi eksplisit, diffusion number, Gamma delta t dibagi delta x kuadrat, harus di bawah setengah.

Batas difusi ini bisa Anda tunjukkan di papan. Masukkan satu Fourier mode ke langkah difusi eksplisit. Faktor pertumbuhannya satu dikurangi empat d dikali sinus kuadrat k delta x per dua. Nilainya tetap di antara minus satu dan satu untuk setiap mode hanya jika empat d paling besar dua, jadi d paling besar setengah.

Kaitannya lagi: batas difusi eksplisit inilah yang menahan recorded diffusivity dalam replay Anda.

## Algoritma SIMPLE

SIMPLE singkatan dari Semi-Implicit Method for Pressure-Linked Equations, dari Patankar. Empat langkah. Satu: tebak tekanan, lalu selesaikan persamaan momentum untuk mendapat kecepatan. Dua: tuliskan koreksi kecepatan sebagai fungsi koreksi tekanan. Tiga: masukkan ke persamaan kontinuitas, sehingga muncul persamaan untuk koreksi tekanan. Empat: koreksi kedua medan, dengan under-relaxation, dan ulangi sampai residual-nya kecil.

Tebak, hitung, koreksi, ulangi. Ingat dari episode pertama: recurrence CFD bekerja dengan semangat yang sama.

## Turbulensi

Turbulensi bersifat kacau dan mencampur dengan kuat. Energi masuk di eddy besar lalu mengalir turun ke skala Kolmogorov, tempat viskositas menghabiskannya.

Panjang Kolmogorov bisa diturunkan dari analisis dimensi. Besaran itu hanya boleh bergantung pada viskositas nu dan laju disipasi epsilon. Cocokkan satuan meter dan detik, dan hasilnya eta sama dengan nu pangkat tiga dibagi epsilon, dipangkatkan seperempat.

RANS memisahkan kecepatan menjadi rata-rata dan fluktuasi, lalu memodelkan semua eddy, biasanya dengan eddy viscosity, misalnya C mu dikali k kuadrat dibagi epsilon pada model k-epsilon. LES hanya memodelkan eddy kecil. DNS tidak memodelkan sama sekali. Kasus Anda tidak membutuhkan semua ini, karena alirannya laminar.

## Lapisan batas dinding

Di dekat dinding, kecepatan turun menjadi nol. y plus menunjukkan seberapa jauh sel pertama dari dinding, dalam satuan viskos: friction velocity dikali jarak ke dinding, dibagi nu. Viscous sublayer berada di bawah y plus sekitar lima, log layer di atas sekitar tiga puluh. Wall function menempatkan sel pertama di log layer dan memodelkan sisanya, jadi murah. Simulasi yang meresolusi dinding butuh y plus sekitar satu.

## Transport panas dan Boussinesq

Suhu dan spesies mengikuti persamaan transport yang sama: perubahan terhadap waktu ditambah konveksi sama dengan difusi ditambah sumber. Kalau densitas bergantung pada suhu, aliran dan suhu saling terikat.

Untuk perubahan densitas yang kecil, Boussinesq approximation menganggap densitas konstan di mana-mana, kecuali pada suku gravitasi. Dan suku gaya apung itulah tepatnya hubungan yang diputus oleh replay.

## Aliran multifase

Euler-Euler memperlakukan setiap fase sebagai kontinum, dengan volume fraction. Cocok untuk sistem yang padat dengan biaya lebih rendah. Euler-Lagrange melacak setiap partikel, dan jika tumbukan partikel ikut dihitung, menjadi CFD-DEM: akurat, tetapi mahal. Recurrence CFD pertama kali dipakai untuk bubble column dan fluidized bed.

## Tiga hal untuk diingat

Pertama. Volume hingga bersifat konservatif, dan koefisien positif berarti tidak ada ekstrem baru: aturan yang sama melindungi limiter Anda.

Kedua. Upwind menambahkan difusivitas numerik setengah u delta x. Tesis Anda adalah cerita tentang difusi numerik.

Ketiga. Batas eksplisit: Courant di bawah satu, diffusion number di bawah setengah. Batas difusi itulah yang menahan recorded diffusivity.
