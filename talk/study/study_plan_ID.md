# Rencana belajar satu bulan (17 Okt – 15 Nov 2026, cadangan sampai sidang)

Sidang terdiri dari: presentasi tesis 15 menit, tanya tesis 5 menit, Machine Learning & Perception
20 menit, track AI for Simulation 20 menit (format dari pengalaman mahasiswa sebelumnya). Bahan:
deck sidang (`talk/defense`), buku ujian lisan v2 (`oral_exam_v2`), bank soal (`notes/`).

## Prinsip belajar (agar mudah diingat)
1. **Retrieval dulu, baca belakangan.** Jawab pertanyaan tanpa melihat, baru periksa. Ini cara paling
   efektif untuk mengingat (bukan membaca ulang).
2. **Satu topik, tiga kalimat.** Apa itu, mengapa, apa artinya. Jika bisa diucapkan dalam bahasa
   Inggris tanpa jeda panjang, topik itu siap.
3. **Turunan rumus ditulis tangan** dari kertas kosong (backprop, delta error, s ≤ 1/6, neraca energi).
4. **Jarak waktu.** Ulang topik pada hari ke-1, 3, 7, 14 (kartu yang salah kembali lebih cepat).
5. **Rekam diri sendiri.** Dengar ulang sekali; catat tiga hal yang diperbaiki, bukan semua.

## Pola harian (sekitar 2,5 jam pada hari kerja)
| Blok | Menit | Isi |
|---|---|---|
| A | 60 | satu topik ML&P atau AI for Simulation: retrieval + turunan tangan |
| B | 40 | presentasi: satu bagian deck, ucapkan keras dengan tiga kata kunci (tombol R) |
| C | 25 | bahasa Inggris lisan (lihat di bawah) |
| D | 15 | kartu hafalan: pertanyaan tesis dan angka wajib |
Minggu: simulasi ujian 60–90 menit (talk + tanya), lalu istirahat.

## Empat minggu
| Minggu | Presentasi & tesis | ML & Perception | AI for Simulation | Bahasa Inggris |
|---|---|---|---|---|
| 1 · 17–23 Okt | alur 11 slide sidang; slide 1–5 lancar | ERM, loss, generalisasi; neuron → MLP | rCFD kuliah: ide, database, recurrence | shadowing 10 menit/hari; rekam slide 1–3 |
| 2 · 24–30 Okt | slide 6–11; talk penuh pertama (rekam, ukur waktu); roster ke PAS bila komite pasti | backprop + delta error; GD, momentum, Adam | gambar tesis Bab 5; dasar CFD (NS, FVM, Boussinesq) | 3 jawaban "why" per hari, masing-masing 3 kalimat |
| 3 · 31 Okt–6 Nov | talk partner; 2 talk penuh sidang; tanya-jawab dari `examiner_questions.md` | aktivasi, regularisasi, init; CNN; RNN/LSTM | gambar tesis Bab 6 + Bab 2; limiter, s ≤ 1/6 | mock Q&A 2x dengan rekaman |
| 4 · 7–13 Nov | 3 simulasi ujian penuh; versi darurat 12 menit | attention, Transformer; ML klasik | pertanyaan lanjutan Pirker (rezim, fluks, biaya) | latihan tanpa catatan; frasa jembatan otomatis |
| cadangan | kartu hafalan, tidur cukup, tes laptop + proyektor | topik terlemah | topik terlemah | pemanasan 10 menit sebelum ujian |

## Bahasa Inggris lisan: 25 menit per hari
- 10 menit **shadowing**: putar 1 menit bicara (BBC 6 Minute English atau TED), ulangi kalimatnya
  bersamaan dengan pembicara, fokus pada ritme, bukan aksen.
- 10 menit **jelaskan satu slide** tanpa naskah, rekam, dengar ulang sekali.
- 5 menit **pelafalan istilah**: cek di YouGlish atau Cambridge Dictionary (contoh: *buoyancy,
  heterogeneity, anti-diffusive, recurrence, thermocline*).

Frasa jembatan (hafalkan sampai otomatis):
- *"Let me think about that for a second."*
- *"There are two parts to that. First ... Second ..."*
- *"The short answer is ..., and the reason is ..."*
- *"I have not tested that, but I would expect ... because ..."*
- *"Could you repeat the question? I want to make sure I answer the right thing."*

## Tautan (diperiksa aktif 16 Okt 2026)
Bahasa Inggris dan presentasi:
- BBC Learning English, 6 Minute English: https://www.bbc.co.uk/learningenglish/english/features/6-minute-english
- BBC Learning English, The English We Speak: https://www.bbc.co.uk/learningenglish/english/features/the-english-we-speak
- YouGlish (pelafalan dalam kalimat nyata): https://youglish.com/
- Cambridge Dictionary (audio UK/US): https://dictionary.cambridge.org/
- Academic Phrasebank, University of Manchester: https://www.phrasebank.manchester.ac.uk/
- TED Talks (shadowing): https://www.ted.com/talks
- Penn State, struktur assertion–evidence untuk slide: https://writing.engr.psu.edu/research.html

Machine learning (intuisi visual):
- 3Blue1Brown, Neural networks: https://www.3blue1brown.com/topics/neural-networks
- StatQuest: https://statquest.org/
- Karpathy, micrograd (backprop dari nol): https://github.com/karpathy/micrograd
- Colah, Understanding LSTM Networks: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
- Jay Alammar, The Illustrated Transformer: https://jalammar.github.io/illustrated-transformer/

## Angka wajib (kartu hafalan)
260x (569 vs 2,16 min; rekaman tidak termasuk) · f_sd: 1,07 K / 0,068 mm / 5,08 K · front 4,5 vs 19,3 mm
(240 s), 2,5 mm peta saja · terkuras 4,6 K · 15,7 → 5,3–4,5 mm (ref 5,0) · 1,46 → 0,70–0,64 K ·
s ≤ 1/6 · −0,66 → +0,06 K pada 9,62 K · 2,25 → 0,45 K, −0,86 K · prominence 0,028 / 0,027 (perlu 0,05–0,1).
