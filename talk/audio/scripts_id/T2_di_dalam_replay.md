# T2 · Di dalam replay: knob, saluran keluar, dan limiter

Episode ini membahas jantung tesis: kenapa replay standar meleset, dan bagaimana koreksi saya memperbaikinya. Kalau cerita ini bisa Anda sampaikan dengan jelas, sebagian besar pertanyaan tentang bab empat dan lima bisa Anda jawab.

## Apakah alirannya berulang?

Mulai dari pertanyaan yang mungkin diajukan Profesor Pirker: apakah aliran Anda benar-benar recurrent? Jawaban jujurnya: tidak.

Recurrence matrix membandingkan setiap pasangan keadaan yang terekam. Jarak yang kecil berarti dua keadaan mirip, sehingga replay bisa melompat dari satu ke yang lain. Di tangki saya, matriksnya terbagi dua blok: tahap pengisian dan tahap pengendapan. Tidak ada keadaan yang kembali. Metodenya meminta prominence sekitar 0,05 sampai 0,1. Tangki saya punya median 0,028. Jadi replay cukup memutar frame secara berurutan.

Apakah masih bisa disebut recurrence CFD? Ya. Penghematannya tidak datang dari lompatan antar frame, melainkan dari tidak menghitung kecepatan dan tekanan lagi.

## Face exchange dan knob-nya

Perpindahan murni tidak mencampur apa pun. Karena itu, setelah setiap langkah, library replay menukar sebagian panas lewat setiap face, dari sel hangat ke sel dingin. Kekuatan pertukaran per langkah ini disebut f s d. Besaran ini tidak bersatuan, jadi bukan koefisien difusi, tetapi bisa diterjemahkan menjadi koefisien difusi.

Sifat pentingnya begini. Pertukaran ini hanya bisa mengurangi perbedaan. Ia tidak pernah bisa membangun kembali front yang sudah melebar.

## Tidak ada satu setelan terbaik

Saya menjalankan tujuh nilai kekuatan. Kandungan panas tangki paling baik tanpa pencampuran tambahan, dengan galat suhu rata-rata 1,07 kelvin. Tinggi lapisan hangat paling baik di sekitar setengah, dengan galat hanya 0,068 milimeter. Jadi tidak ada satu nilai yang terbaik untuk keduanya. Dengan pencampuran terkuat, tangki berakhir 5,08 kelvin terlalu dingin.

Kenapa pencampuran lebih banyak membuat panas hilang? Bayangkan bak mandi yang lubang pembuangannya dipasang tepat di bawah lapisan permukaan yang hangat. Kalau lapisan itu tetap tipis, yang terbuang air dingin. Kalau lapisan itu melebar ke bawah, air hangat mencapai lubang pembuangan dan ikut keluar. Di tangki saya, outlet berada tepat di bawah front. Jadi front yang melebar berubah menjadi kebocoran panas.

Saya menunjukkannya dengan neraca energi seluruh tangki. Energi masuk dikurangi energi keluar memberi suhu outlet. Selama semburan hangat, replay standar menahan panas berlebih sekitar 2,7 kelvin. Setelah semburan berhenti, panas sebesar 4,6 kelvin terbuang lewat outlet.

Lalu siapa yang membuat front melebar? Saya periksa. Dengan peta rekaman saja, front pada detik ke-240 setebal 2,5 milimeter. Dengan exchange standar, 19,3. Referensinya 4,5. Jadi petanya baik-baik saja. Exchange-lah penyebabnya.

## Kenapa tidak pakai difusi negatif saja?

Pertanyaan klasik dari penguji. Difusi menghaluskan. Jadi kenapa tidak dijalankan mundur untuk mempertajam front?

Karena difusi negatif ill-posed. Setiap gangguan kecil akan membesar, dan riak yang paling pendek tumbuh paling cepat. Anda bisa menunjukkannya dengan satu Fourier mode. Untuk langkah difusi eksplisit, faktor pertumbuhannya satu dikurangi empat nu kali sinus kuadrat k delta x per dua. Untuk nu negatif dan mode terpendek, faktornya menjadi satu ditambah empat kali nilai mutlak nu. Nilainya lebih dari satu, jadi riak itu tumbuh di setiap langkah. Dalam uji satu dimensi saya, setelah 21 langkah, medannya sudah keluar dari rentang data.

Jadi bagian yang berguna, yaitu penajaman, saya pertahankan. Bagian yang berbahaya saya hentikan dengan limiter.

## Limiter

Untuk setiap sel, ambil nilai terkecil dan terbesar di antara sel itu dan tetangganya. Itulah batas lokalnya. Headroom sel hangat adalah seberapa jauh ia masih boleh naik. Headroom sel dingin adalah seberapa jauh ia masih boleh turun. Lewat sebuah face, panas dipindahkan ke arah atas gradien, dari sel yang lebih dingin ke sel yang lebih hangat. Jumlahnya adalah headroom yang lebih kecil, dikali kekuatan s.

Dengan begitu, tidak ada sel yang keluar dari batasnya. Nilai maksimum tidak bisa bertambah, nilai minimum tidak bisa turun. Panas yang keluar dari satu sel masuk ke sel lainnya, jadi energi tetap terjaga di setiap face. Ide ini berasal dari limiter flux-corrected transport, karya Boris dan Book, serta Zalesak.

Ada juga satu batas yang rapi. Sel heksahedral punya enam face. Kalau s paling besar satu per enam, tidak ada sel yang bisa keluar dari batasnya bahkan sebelum clamp bekerja. Rentang kerja saya, 0,40 sampai 0,50, berada di atas itu, jadi bergantung pada clamp dan conservation constraint global. Sampaikan hal ini dengan jujur kalau ditanya.

## Kenapa ada bobot vertikal?

Front-nya horizontal. Jadi koreksi seharusnya bekerja melintasi front, bukan sepanjang front. Setiap face mendapat bobot kosinus kuadrat dari sudut antara arah penghubungnya dan arah vertikal. Face yang melintasi front mendapat bobot satu, face yang sejajar front mendapat nol. Tanpa bobot ini, koreksi membuat front bergerigi ke samping. Secara matematis, bobot ini persis koefisien face dari difusi yang hanya bekerja ke satu arah.

## Recorded diffusivity tidak membantu

Satu hasil lagi yang harus bisa Anda jelaskan. Saya juga mencoba recorded diffusivity yang bersifat lokal sebagai pengganti knob konstan. Hasilnya tidak berubah, dan replay-nya identik sampai ke bit. Kenapa? Nilai yang terekam meminta pertukaran lebih besar daripada yang bisa diberikan langkah eksplisit. Setiap face mentok di batas atas, sehingga medannya berperilaku persis seperti setelan konstan. Langkah waktu yang lebih pendek atau exchange implisit akan membuatnya bisa bekerja.

## Hasilnya

Dengan koreksi, front di akhir run berubah dari 15,7 milimeter menjadi antara 5,3 dan 4,5. Referensinya 5,0. Galat suhu rata-rata sepanjang run turun dari 1,46 menjadi sekitar 0,7 kelvin. Dan ingat kalimat jujurnya: kekuatan koreksi dipilih dengan membandingkan terhadap referensi yang sama.

## Tiga hal untuk diingat

Pertama. Tidak ada setelan knob yang cocok untuk semua, karena outlet di bawah front membuang panas dari front yang melebar.

Kedua. Difusi negatif membuat riak tumbuh. Limiter mempertahankan penajaman dan tetap di dalam batas tetangga, jadi tidak ada ekstrem baru dan tidak ada panas yang hilang.

Ketiga. 15,7 milimeter menjadi sekitar 5, referensinya 5,0, dan kekuatannya dipilih dengan referensi.
