# Panduan latihan sidang (bahasa Indonesia)


## Pelafalan (latih dulu, cek di https://youglish.com)
| Kata | Cara ucap (kira-kira) | Arti |
|---|---|---|
| buoyancy / buoyant | BOY-un-see / BOY-unt | gaya apung / mengapung |
| heterogeneity | het-uh-ruh-juh-NEE-uh-tee | ketidakmerataan suhu |
| adiabatic | ay-dee-uh-BAT-ik | tanpa pertukaran panas dengan dinding |
| recurrence | ri-KUR-uns | pengulangan |
| thermocline | THUR-muh-klyn | lapisan transisi suhu (front) |
| conservative | kun-SUR-vuh-tiv | menjaga jumlah total (panas tidak hilang) |
| diffusion / anti-diffusion | di-FYOO-zhun / AN-tee di-FYOO-zhun | penyebaran / kebalikannya |
| laminar | LAM-in-ar | aliran teratur, tidak turbulen |
| millimetres | MIL-ih-mee-terz | milimeter |
| kelvin | KEL-vin | satuan suhu |
| reservoir, regime | REZ-er-vwar, ray-ZHEEM | wadah, rezim/jenis aliran |

Simbol tidak dibaca sebagai huruf. Katakan "the mixing strength", bukan "f s d"; "the correction
strength", bukan "s".

Untuk latihan, bukan untuk dibaca di depan penguji. Naskah Inggris ada di `speaker_notes_en.md`;
di sini ada logikanya. Cara pakai: baca satu slide, tutup berkas, jelaskan dalam bahasa Inggris
dengan tiga kata kunci saja. Rekam, dengar ulang.

Alur besar yang harus Anda pegang (satu kalimat per langkah):
1. rCFD memutar ulang aliran yang direkam; dibuat untuk skalar pasif. 2. Suhu tidak pasif.
3. Replay standar punya satu kenop campur, tidak ada nilai terbaik. 4. Penyebabnya: front yang tebal
menguras panas lewat outlet. 5. Koreksi anti-difusi yang dibatasi membangun front lagi.
6. Di tangki adiabatik lebarnya kembali. 7. Di tutup dingin panasnya benar, tapi lapisan terlambat
memisah: itu transport yang hilang. 8. Rekaman milik rezim alirannya.

---

### Slide 1 · pertanyaan
- **Inti:** apakah rekaman aliran bisa membawa suhu yang ikut mendorong aliran?
- **Kata kunci:** record & replay · temperature drives the flow · where it breaks
- **Istilah:** *passive scalar* = besaran yang dibawa aliran tapi tidak mengubahnya (pewarna); *non-passive* = ikut mengubah aliran (suhu lewat gaya apung).
- **Pertanyaan:** "Why is temperature harder than a dye?" → *Because warm fluid rises. The temperature changes the velocity, and the replay cannot recompute the velocity.*

### Slide 2 · fenomena (demo)
- **Inti:** jet hangat 315 s, lapisan hangat di atas, front sekitar 5 mm, outlet tepat di bawah front.
- **Kata kunci:** jet for 315 s · 5 mm front · outlet under the front
- **Cara demo:** tekan *play*, biarkan jalan sampai sekitar 320 s, tekan *outlet* untuk garis tinggi outlet. Kalau macet: tekan **V** (video cadangan).
- **Istilah:** *filling box* = kotak yang terisi dari sumber apung (Baines & Turner 1969); *front/thermocline* = zona transisi hangat-dingin.
- **Pertanyaan:** "Why laminar, why this fluid?" → *Re about 100 at the inlet, so no turbulence model adds a second source of error. The fluid is the one defined in the case files; both stages simulate the same fluid.*

### Slide 3 · metode
- **Inti:** preparation menghitung CFD penuh sekali dan menyimpan peta perpindahan sel; replay hanya mengangkut suhu.
- **Kata kunci:** maps · no pressure solve · 260x, recording excluded
- **Cara membaca gambar:** kiri = rekaman, tengah = database 600 frame, kanan = satu langkah replay: peta M, pertukaran S, koreksi C (kontribusi saya), kendala konservasi B.
- **Angka wajib:** 569 menit vs 2,16 menit rata-rata; 120–700x; rekaman = satu run penuh.
- **Pertanyaan:** "Is 260x fair?" → *Solver time against solver time, without image output, same machine. The recording costs one full run; the saving starts with the second replay.*

### Slide 4 · Q1
- **Inti:** satu kenop f_sd tidak bisa membenarkan isi panas dan tinggi lapisan sekaligus.
- **Kata kunci:** f_sd is free · heat vs height · more mixing, more loss
- **Cara membaca grafik:** (a) suhu rata-rata; garis hitam referensi; warna = tujuh kekuatan. Setelah 315 s yang dicampur kuat jatuh lebih cepat. (b) ketinggian pusat panas.
- **Angka wajib:** 1,07 K (f_sd = 0); 0,068 mm (dekat 0,5); 5,08 K terlalu dingin pada f_sd = 3.
- **Pertanyaan:** "How did earlier work choose f_sd?" → *I found no procedure in the published work; it is set by hand.*

### Slide 5 · mekanisme (demo dua panel)
- **Inti:** peta rekaman tidak mengoleskan front; langkah pertukaran yang mengoleskan; outlet di bawah front lalu menguras panas.
- **Kata kunci:** maps keep it thin · exchange smears · outlet drains
- **Angka wajib:** 4,5 mm vs 19,3 mm pada 240 s; 2,5 mm dengan peta saja; 4,6 K terkuras setelah inflow.
- **Istilah:** *bulk balance* = neraca energi tangki: perubahan suhu rata-rata = laju massa x (T_in − T_out); dari situ T_out dihitung.
- **Pertanyaan:** "Is the drain real?" → *I recovered the outlet temperature from the energy balance and checked it against the stored solver fields, within 0.5 K.*

### Slide 6 · koreksi (demo model 1D)
- **Inti:** difusi negatif menajamkan tapi meledak; versi dibatasi menajamkan tanpa nilai baru di luar rentang.
- **Kata kunci:** backward diffusion explodes · local bounds · vertical weight
- **Cara demo:** tekan *play*. Kiri (abu): riak tumbuh, keluar dari rentang setelah sekitar 21 langkah. Kanan (merah): front menajam dari 8,8 ke 4,4 sel setelah 30 langkah.
- **Penjelasan rumus:** Δq = s·min(Q⁺ₕ, Q⁻꜀): sel hangat boleh naik paling banyak sampai maksimum tetangganya (Q⁺), sel dingin turun paling banyak sampai minimum tetangganya (Q⁻); ambil yang lebih kecil, kalikan s.
- **Istilah:** *flux-corrected transport* (Boris & Book 1973, Zalesak 1979); *local extremum*.
- **Pertanyaan:** "Why s ≤ 1/6?" → *A cell has six faces. If each moves at most s times the headroom, the total stays inside the bounds when six times s is at most one. Above that the clamp may act.* (backup B3)

### Slide 7 · hasil adiabatik
- **Inti:** front kembali ke lebar referensi, galat suhu rata-rata kira-kira setengah.
- **Kata kunci:** 15.7 to about 5 · error halves · s chosen against the reference
- **Angka wajib:** 15,7 → 5,3–4,5 mm (ref 5,0); 1,46 → 0,70–0,64 K.
- **Kejujuran wajib:** s dipilih dengan membandingkan ke referensi yang sama.
- **Pertanyaan:** "How would you pick s without the reference?" → *That is the open problem. One idea is to tie it to the recorded diffusivity or to a stability measure of the front; I have not tested it.*

### Slide 8 · tutup didinginkan
- **Inti:** isi panas benar; lapisan terlambat memisah saat tangki terisi; fluks rekaman mengurangi keterlambatan tapi tangki jadi terlalu dingin.
- **Kata kunci:** heat right · layers too slow · flux helps, overcools
- **Cara membaca grafik:** (b) heterogenitas; pita merah = keterlambatan koreksi lokal; ungu = dengan fluks rekaman.
- **Angka wajib:** −0,66 → +0,06 K pada pendinginan 9,62 K; 2,25 → 0,45 K; −0,86 K.
- **Pertanyaan:** "Why does the flux overcool?" → *With the global conservation constraint switched off, the flux moves the end temperature by only 0.07 K. So the surplus appears where the flux meets the single-compartment constraint. Splitting the constraint into compartments is the next fix.*

### Slide 9 · rezim
- **Inti:** tutup dingin membuat konveksinya sendiri; aliran itu berganti sekitar 10x lebih cepat; rekaman tanpa pendinginan tidak bisa melayaninya.
- **Kata kunci:** own convection · ten times faster · one database per regime
- **Pertanyaan:** "Would multiple databases solve Q4?" → *They would supply the right motion for each regime; the lag while filling is a transport problem inside one regime, so I would expect partial help. Not tested.*

### Slide 10 · bukti dan batas
- **Inti:** empat hal terbukti, empat masih terbuka (termasuk Q5 vessel).
- **Pertanyaan:** "What would you do differently?" → *Record the flux without the temperature of the reference, so it can transfer, and plan the strength selection from the start.*

### Slide 11 · kontribusi
- **Kata kunci:** trade-off and cause · bounded correction · limit of local fixes

---

## Rencana waktu 15 menit
0:45 · 2:00 · 3:30 · 5:00 · 6:30 · 8:15 · 9:45 · 11:30 · 12:15 · 13:30 · 14:15. Jika pada akhir
slide 7 jam sudah lewat 10:30, lompati slide 9 (gabungkan satu kalimatnya ke slide 10).

## Tombol saat presentasi
→ / spasi: maju · ←: mundur · F: layar penuh · P: jendela presenter (layar kedua) · R: kartu latihan ·
V: video cadangan demo · B: slide cadangan · G: lompat ke nomor slide.
