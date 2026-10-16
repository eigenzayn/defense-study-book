/* ============================================================================
   Deck engine (no dependencies, works from file:// and offline).
   Keys: Right/Space/PageDown next, Left/PageUp back, Home/End, F fullscreen,
   P presenter window, R rehearsal card, V demo fallback, B backups, G go to slide,
   H help. The presenter window is an about:blank popup driven from this page,
   so it works from file:// as well; the audience screen never shows notes.
   ========================================================================== */
(function () {
  "use strict";
  const stage = document.querySelector(".deck-stage");
  const slides = Array.from(document.querySelectorAll(".slide"));
  const notes = JSON.parse((document.getElementById("notes") || { textContent: "{}" }).textContent || "{}");
  const deckName = document.body.dataset.deck || "deck";
  let idx = 0, presenter = null, t0 = null, rehearse = false;

  /* === SCALE THE 1920x1080 STAGE TO THE WINDOW === */
  function fit() {
    const s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
    const x = (window.innerWidth - 1920 * s) / 2, y = (window.innerHeight - 1080 * s) / 2;
    stage.style.transform = `translate(${x}px, ${y}px) scale(${s})`;
  }
  window.addEventListener("resize", fit); fit();

  /* === TOAST === */
  const toast = document.createElement("div"); toast.className = "toast"; stage.appendChild(toast);
  function say(msg) { toast.textContent = msg; toast.classList.add("show"); clearTimeout(say.t); say.t = setTimeout(() => toast.classList.remove("show"), 1400); }

  /* === REHEARSAL CARD === */
  const card = document.createElement("div"); card.className = "overlay"; stage.appendChild(card);
  function renderCard() {
    const s = slides[idx], n = notes[s.id] || {};
    const cues = (s.dataset.cues || "").split("|").filter(Boolean);
    card.innerHTML = `<div class="kicker">Rehearsal · slide ${idx + 1} of ${slides.length} · planned ${fmt(+s.dataset.time || 0)}</div>
      <h2>${s.dataset.title || ""}</h2>
      <div class="cues">${cues.map(c => `<div>${c}</div>`).join("")}</div>
      <p class="small"><b>Key message.</b> ${n.key || ""}</p>
      <p class="small"><b>Transition.</b> ${n.next || ""}</p>
      <ul class="plain small"><li>☐ I said the key message in my own words</li><li>☐ every number I said is on the slide or in the notes</li>
      <li>☐ I pointed at the evidence, not at the title</li><li>☐ I stayed within the planned time</li></ul>`;
  }

  /* === NAVIGATION === */
  function go(i) {
    i = Math.max(0, Math.min(slides.length - 1, i));
    slides[idx].classList.remove("active");
    slides[idx].dispatchEvent(new CustomEvent("slide:leave"));
    idx = i;
    slides[idx].classList.add("active");
    slides[idx].dispatchEvent(new CustomEvent("slide:enter"));
    history.replaceState(null, "", "#" + (idx + 1));
    if (rehearse) renderCard();
    if (window.deckProgress) window.deckProgress(idx, slides);
    updatePresenter();
  }
  window.deck = { go: (i) => go(i), next: () => go(idx + 1), prev: () => go(idx - 1), get index() { return idx; } };

  /* === PRESENTER WINDOW === */
  function fmt(sec) { sec = Math.max(0, Math.round(sec)); return Math.floor(sec / 60) + ":" + String(sec % 60).padStart(2, "0"); }
  function planned(upto) { return slides.slice(0, upto).reduce((a, s) => a + (+s.dataset.time || 0), 0); }
  function openPresenter() {
    presenter = window.open("", deckName + "-presenter", "width=1100,height=760");
    if (!presenter) { say("Allow pop-ups for the presenter window"); return; }
    presenter.document.title = "Presenter · " + document.title;
    presenter.document.body.innerHTML = "";
    const st = presenter.document.createElement("style");
    st.textContent = `body{font-family:Georgia,serif;background:#16191d;color:#ece7dd;margin:0;padding:26px 34px;font-size:22px;line-height:1.4}
      .row{display:flex;justify-content:space-between;align-items:baseline;gap:20px} .big{font-size:56px;font-weight:700}
      .t{color:#d98a63} h2{font-size:32px;margin:8px 0 6px} .cues{display:flex;gap:16px;margin:10px 0 14px}
      .cues div{flex:1;border-top:3px solid #c4502f;padding-top:6px;font-weight:700} .notes{font-size:24px;white-space:pre-wrap;background:#1f2329;padding:14px 18px;border-radius:4px}
      .next{color:#9aa3ad;margin-top:12px} .short{color:#c9d3dc;font-style:italic;margin-top:8px} button{font:inherit;font-size:18px;margin-right:8px}`;
    presenter.document.head.appendChild(st);
    presenter.document.body.innerHTML = `<div class="row"><div class="big" id="clock">0:00</div><div id="plan"></div><div><button id="b">◀</button><button id="n">▶</button><button id="r">reset timer</button></div></div>
      <h2 id="title"></h2><div class="cues" id="cues"></div><div class="notes" id="notes"></div><div class="short" id="short"></div><div class="next" id="next"></div>`;
    const pd = presenter.document;
    pd.getElementById("n").onclick = () => go(idx + 1);
    pd.getElementById("b").onclick = () => go(idx - 1);
    pd.getElementById("r").onclick = () => { t0 = Date.now(); };
    pd.addEventListener("keydown", key);
    if (!t0) t0 = Date.now();
    updatePresenter();
  }
  function updatePresenter() {
    if (!presenter || presenter.closed) return;
    const d = presenter.document, s = slides[idx], n = notes[s.id] || {};
    d.getElementById("title").textContent = `${idx + 1}/${slides.length}  ${s.dataset.title || ""}`;
    d.getElementById("cues").innerHTML = (s.dataset.cues || "").split("|").filter(Boolean).map(c => `<div>${c}</div>`).join("");
    d.getElementById("notes").textContent = n.say || "(no notes)";
    d.getElementById("short").textContent = n.short ? "If lost: " + n.short : "";
    const nx = slides[idx + 1];
    d.getElementById("next").textContent = nx ? "Next: " + (nx.dataset.title || "") : "Last slide";
    d.getElementById("plan").innerHTML = `slide ${fmt(+s.dataset.time || 0)} · plan at end of slide <span class="t">${fmt(planned(idx + 1))}</span>`;
  }
  setInterval(() => { if (presenter && !presenter.closed && t0) presenter.document.getElementById("clock").textContent = fmt((Date.now() - t0) / 1000); }, 500);

  /* === KEYS === */
  function key(e) {
    const k = e.key;
    if (["ArrowRight", "PageDown", " "].includes(k)) { e.preventDefault(); go(idx + 1); }
    else if (["ArrowLeft", "PageUp"].includes(k)) { e.preventDefault(); go(idx - 1); }
    else if (k === "Home") go(0);
    else if (k === "End") go(slides.length - 1);
    else if (k === "f" || k === "F") { if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {}); else document.exitFullscreen(); }
    else if (k === "p" || k === "P") openPresenter();
    else if (k === "r" || k === "R") { rehearse = !rehearse; card.classList.toggle("show", rehearse); if (rehearse) renderCard(); }
    else if (k === "v" || k === "V") { slides[idx].dispatchEvent(new CustomEvent("slide:fallback")); say("Demo fallback"); }
    else if (k === "b" || k === "B") { const j = slides.findIndex(s => s.classList.contains("backup")); if (j >= 0) go(j); }
    else if (k === "g" || k === "G") { const n = parseInt(prompt("Go to slide", idx + 1), 10); if (n) go(n - 1); }
    else if (k === "h" || k === "H" || k === "?") say("→ next · ← back · F full screen · P presenter · R rehearse · V demo fallback · B backups · G go to");
  }
  document.addEventListener("keydown", key);
  stage.addEventListener("click", (e) => { if (!e.target.closest("button, input, video, a, .noclick")) go(idx + 1); });
  document.addEventListener("fullscreenchange", fit);

  const start = parseInt((location.hash || "#1").slice(1), 10) - 1;
  slides.forEach(s => s.classList.remove("active"));
  idx = 0; slides[0].classList.add("active");
  go(isNaN(start) ? 0 : start);
})();
