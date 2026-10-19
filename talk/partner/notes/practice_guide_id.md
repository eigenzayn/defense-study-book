# Panduan latihan talk industri (bahasa Indonesia)


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

Audiens: insinyur dan manajer R&D perusahaan pendana. Mereka menilai cara Anda berpikir, bukan
detail rumus. Pesan utama: *"This is how I investigate a physical problem, test a numerical method,
and decide what the evidence supports."* Jangan pernah mengklaim tesis sudah menyelesaikan masalah
proses mereka.

| Slide | Inti (ID) | Tiga kata kunci | Pertanyaan yang mungkin + jawaban singkat |
|---|---|---|---|
| 1 | aliran cepat stabil, suhu berubah lambat; CFD membayar yang cepat | two time scales · CFD pays · my start | "Which processes?" → *A general class: storage, mixing, reactors. I would not guess your processes.* |
| 2 | 569 menit, sebagian besar untuk tekanan dan kecepatan | 569 min · pressure · temperature cheap | "Hardware?" → cek log run sebelum menjawab; jangan menebak |
| 3 | tiga langkah: simulasi sekali → rekam gerak (600 frame) → putar ulang panas (≈2 menit, 260x); umpan balik terputus | simulate · record · replay | "Is this machine learning?" → *A data-based surrogate built from stored linear operators, tested against CFD.* |
| 4 | demo: aliran sama, front 5 mm vs 4x lebih tebal | same flow · 5 mm · four times | "Why so simple?" → *It isolates the effect: laminar, closed, every joule accounted for.* |
| 5 | outlet tepat di bawah front, front tebal = bocor panas 4,6 K | follow the heat · outlet · leak | "How did you find it?" → *By following the energy: tank budget, then outlet, then one face.* (detail: cadangan B2) |
| 6 | koreksi dalam batas fisika; front 15,7 → ~5 mm; s dipilih terhadap referensi | bounded · energy kept · honest tuning | "Does speed cost accuracy?" → *Here the front and the heat come back; the strength is tuned, which I say openly.* |
| 7 | tutup dingin: panas benar (0,06 K), transport hilang, rekaman milik rezimnya (Minggu ≠ badai salju) | cold plumes · transport · one regime | "Would more data fix it?" → *More recordings per regime, yes for coverage; the transport inside one regime needs a recorded flux or a better model.* (angka: cadangan B3) |
| 8 | tiga arah riset (belum diuji) + syarat sebelum dipakai industri | learn · switch · test | "Did you train a neural network?" → *Not in this thesis. These are directions that follow from measured weaknesses.* "What data would you need?" → *Reference data per operating regime. I would not assume anything about your data.* |
| 9 | tiga kebiasaan kerja + pertanyaan berikut | energy · bounds · limits | — |

Versi ramping 18 Okt 2026: 9 slide inti, detail di slide cadangan (tekan B). Cadangan: B1 metode
lengkap, B2 tiga langkah investigasi, B3 angka tutup dingin, B4 POD, B5 dasar biaya, B6 limiter,
B7 snapshot, B8 yang saya bangun sendiri, B9 daftar validasi lengkap.

Waktu: 0:45 · 2:00 · 3:30 · 5:00 · 6:45 · 8:15 · 10:00 · 12:00 · 13:00. Jika terlambat,
slide 8 cukup tiga judul arah riset. Tekan A saat latihan untuk mendengar contoh pembawaan slide itu.

Frasa aman untuk audiens industri: *"In my test case ..."*, *"I have not tested that on a process,
but ..."*, *"The evidence supports ..., it does not yet support ..."*.
