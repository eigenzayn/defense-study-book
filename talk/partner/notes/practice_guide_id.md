# Panduan latihan talk industri (bahasa Indonesia)

Audiens: insinyur dan manajer R&D perusahaan pendana. Mereka menilai cara Anda berpikir, bukan
detail rumus. Pesan utama: *"This is how I investigate a physical problem, test a numerical method,
and decide what the evidence supports."* Jangan pernah mengklaim tesis sudah menyelesaikan masalah
proses mereka.

| Slide | Inti (ID) | Tiga kata kunci | Pertanyaan yang mungkin + jawaban singkat |
|---|---|---|---|
| 1 | aliran cepat stabil, suhu berubah lambat; CFD membayar yang cepat | two time scales · CFD pays · my start | "Which processes?" → *A general class: storage, mixing, reactors. I would not guess your processes.* |
| 2 | 569 menit, sebagian besar untuk tekanan dan kecepatan | 569 min · pressure · temperature cheap | "Hardware?" → cek log run sebelum menjawab; jangan menebak |
| 3 | rekam sekali, putar ulang 260x lebih murah, tapi umpan balik terputus | maps · 260x after recording · feedback cut | "Is this machine learning?" → *A data-based surrogate built from stored linear operators, tested against CFD.* |
| 4 | demo: aliran sama, front 4x lebih tebal | same flow · thick front · the defect | "Why so simple?" → *It isolates the effect: laminar, closed, every joule accounted for.* |
| 5 | ikuti panas: neraca tangki → outlet → satu face | budget · outlet · face | "How long did it take?" → *Weeks. The energy balance was the key tool.* |
| 6 | koreksi dalam batas fisika; front 15,7 → ~5 mm; s dipilih terhadap referensi | bounded · conservative · honest tuning | "Does speed cost accuracy?" → *Here the front and the heat come back; the strength is tuned, which I say openly.* |
| 7 | tutup dingin: panas benar, transport hilang, rekaman milik rezimnya | heat right · transport missing · one regime | "Would more data fix it?" → *More recordings per regime, yes for coverage; the transport inside one regime needs a recorded flux or a better model.* |
| 8 | tiga arah riset, semua belum diuji | learn closure · regime-aware · physics tests | "Did you train a neural network?" → *Not in this thesis. These are directions that follow from measured weaknesses.* |
| 9 | validasi di fisika proses sendiri | physics gap · coverage · measurements | "What data would you need?" → *Reference simulations or measurements per operating regime. I would not assume anything about your data.* |
| 10 | tiga kebiasaan kerja + pertanyaan berikut | budget · bounds · limits | — |

Waktu: 0:45 · 2:00 · 3:30 · 5:00 · 6:45 · 8:15 · 9:45 · 11:30 · 13:15 · 14:15. Jika terlambat,
slide 7 cukup satu kalimat.

Frasa aman untuk audiens industri: *"In my test case ..."*, *"I have not tested that on a process,
but ..."*, *"The evidence supports ..., it does not yet support ..."*.
