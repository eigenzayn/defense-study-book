# A2 · Membaca gambar-gambar di tesis saya

Profesor Pirker sering menunjuk sebuah gambar lalu bertanya: apa yang ditunjukkan gambar ini, dan kenapa? Jadi untuk setiap gambar penting, siapkan tiga kalimat. Apa yang digambarkan. Apa yang terlihat. Dan kenapa itu penting. Di episode ini kita latih persis hal itu. Setiap gambar saya sebut berdasarkan isinya, bukan nomornya, karena penomoran gambar masih bisa berubah.

## Passive scalar dan non-passive scalar

Gambar pembuka punya tiga panel. Pertama, zat pewarna di dalam kecepatan tersimpan dari tangki terisolasi: zat itu hanya teregang oleh aliran. Kedua, tangki yang didinginkan, di mana plume dingin dari tutup menciptakan gerakan. Ketiga, replay, yang memindahkan suhu dengan peta rekaman dan tidak pernah menghitung kecepatan.

Kenapa penting: seluruh pertanyaan tesis ada dalam satu gambar. Zat pewarna hanya menumpang aliran, sedangkan suhu menciptakan aliran, dan replay memutus umpan balik itu.

## Recurrence dari database

Gambar ini menunjukkan distance matrix dari rekaman. Ada dua blok, terbelah di akhir semburan: tahap pengisian dan tahap pengendapan. Baris-barisnya naik ke sebuah plateau, dan tidak ada yang kembali mendekati nol.

Kenapa penting: prominence, dengan median 0,028, tetap di bawah kebutuhan metode. Jadi tidak ada keadaan yang kembali, dan replay memutar frame secara berurutan.

## Transport panas vertikal di bawah tutup dingin

Gambar ini membagi vertical heat flux rata-rata bidang menjadi dua bagian: bagian yang dibawa aliran, dan bagian yang dibawa konduksi. Di bawah tutup dingin, aliran membawa panas jauh lebih banyak daripada konduksi, dan simpangan suhunya seukuran plume utuh.

Kenapa penting: pendinginan adalah proses transport. Langkah difusif tidak bisa menirunya.

## Dua regime

Geometri sama, semburan sama, dua aliran berbeda. Dengan tutup terisolasi, semburan naik, menyebar di bawah tutup, lalu lapisan hangatnya diam. Dengan tutup dingin, lapisan di atas front berputar dalam deretan sel, digerakkan oleh plume dingin.

Kenapa penting: satu kondisi batas memindahkan aliran dari satu regime ke regime lain.

## Replay standar pada sapuan pencampuran

Dua panel: suhu rata-rata dan tinggi panas, untuk tujuh kekuatan pencampuran. Pencampuran yang lebih kuat memanaskan tangki lebih cepat selama semburan, dan mengurasnya lebih cepat sesudahnya. Tinggi panas paling baik pada kekuatan menengah, kandungan panas paling baik dengan pencampuran kecil.

Kenapa penting: tidak ada satu setelan terbaik.

## Tangki terisolasi sepanjang run

Suhu bidang tengah pada empat waktu, dengan lebar front tertulis di setiap panel. Replay yang hanya memakai peta rekaman menjaga front setipis referensi. Replay standar membuatnya melebar. Replay terkoreksi menipiskannya lagi.

Kenapa penting: pelebaran datang dari face exchange, bukan dari peta rekaman.

## Diagram ruang-waktu

Suhu rata-rata horizontal digambar terhadap ketinggian dan waktu. Terlihat lapisan hangat yang tumbuh ke bawah. Panel selisih menunjukkan di mana replay standar terlalu hangat atau terlalu dingin, dan panel ketebalan menunjukkan front-nya tetap terlalu tebal. Replay terkoreksi mengikuti referensi.

## Semua run koreksi dalam satu peta

Setiap penanda adalah satu replay: galat trace dan galat profil akhir, digambar terhadap lebar front. Hanya bentuk yang diberi bobot vertikal yang menurunkan kedua galat sekaligus sambil membawa front ke lebar referensi, 5,0 milimeter. Rentang kerjanya s dari 0,40 sampai 0,50.

Kenapa penting: arah lebih menentukan daripada kekuatan.

## Buoyancy frequency di sepanjang front

Buoyancy frequency menunjukkan seberapa kuat pelapisan menahan gerakan vertikal. N kuadrat sama dengan g dikali beta dikali gradien suhu vertikal. Replay standar hanya punya penghalang kira-kira setengah sekuat referensi. Replay terkoreksi mencapai nilai referensi setelah semburan.

Kenapa penting: front yang lebih tajam adalah penghalang yang lebih kuat. Koreksi memulihkan kestabilan front, tidak hanya lebarnya.

## Profil akhir melintasi front

Tanpa koreksi, front lebar dan terlalu tinggi. Koreksi tanpa bobot membuatnya tipis, tetapi meletakkannya di tempat yang salah. Bobot vertikal mengikuti referensi.

Kenapa penting: front yang bergerigi bisa punya lebar yang benar tetapi bentuk yang salah. Baca lebar selalu bersama profilnya.

## Suhu outlet dari neraca energi

Suhu outlet diperoleh dari neraca energi seluruh tangki: massa dikali laju perubahan suhu rata-rata sama dengan laju aliran massa dikali selisih suhu inlet dan outlet. Selama semburan hangat, replay standar menahan panas berlebih sekitar 2,7 kelvin. Setelah itu, 4,6 kelvin terbuang.

Kenapa penting: outlet berada tepat di bawah front, jadi galat numerik di front berubah menjadi galat dalam neraca energi.

## State space

Dua mode POD utama dari medan referensi, dan jarak setiap run dari ruang sepuluh mode pertama. Replay standar keluar dari ruang ini dan tidak kembali. Replay terkoreksi kembali setelah semburan.

Kenapa penting: koreksi menjaga replay tetap dekat dengan keadaan-keadaan yang dicakup rekaman.

## Tutup dingin: profil, trace, dan plume

Profil akhir: replay standar menyimpan jumlah panas yang hampir benar, tetapi di tempat yang salah, dengan galat profil 2,79 kelvin. Bagian tengah terlalu hangat, lapisan atas terlalu dingin. Koreksi memindahkan panasnya kembali.

Trace: sebuah pita berarsir menunjukkan seberapa jauh koreksi lokal tertinggal dalam heterogenitas selama semburan hangat. Hanya recorded flux yang ikut mengikuti heterogenitas. Keterlambatan pelapisan berarti kekurangan transport, bukan kekurangan ketajaman.

Dan dalam tiga dimensi: plume pada replay standar berhenti di tengah jalan. Dengan koreksi, plume itu mencapai front lagi. Replay tidak mengarang gerakan apa pun. Plume itu sudah ada di peta rekaman sejak awal.

## Recurrence dari dua rekaman

Setelah semburan berhenti, aliran dengan tutup dingin terus memperbarui dirinya, kira-kira sepuluh kali lebih cepat pada selang waktu pendek, sedangkan aliran tutup terisolasi hampir tidak berubah.

Kenapa penting: kasus yang didinginkan adalah regime yang berbeda, jadi database yang direkam tanpa pendinginan tidak bisa berisi gerakannya.

## Tiga hal untuk diingat

Pertama. Untuk setiap gambar: apa yang digambarkan, apa yang terlihat, kenapa penting.

Kedua. Rangkaian gambar kuncinya: tidak ada satu setelan pencampuran terbaik, peta rekaman menjaga front tipis, outlet membuang panas, dan koreksi vertikal memulihkan lebar serta kestabilan front.

Ketiga. Dengan tutup dingin: panasnya benar tetapi tempatnya salah tanpa koreksi, keterlambatan adalah kekurangan transport, dan regime yang berbeda butuh database yang berbeda.
