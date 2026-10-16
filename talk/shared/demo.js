/* ============================================================================
   Demo components. Each one shows real research data or a documented model:
   FramePlayer   playback of decoded rendered frames, reference | standard replay
                 (video: 20 replay seconds per video second, frames every 2 s)
   SnapInspector stored solver snapshots at six instants (frame inspection)
   LimiterModel  the 1D model front of thesis Fig 4.1, recomputed live in the browser
   Every component listens to "slide:fallback" (key V) and swaps to its fallback.
   ========================================================================== */
(function () {
  "use strict";
  const BASE = document.body.dataset.base || "../shared/";

  /* === FRAME PLAYER === */
  window.FramePlayer = function (root, opts) {
    opts = opts || {};
    const HALF = opts.half === "left";
    const RATE = 20, TMAX = 598, INFLOW = 315;
    root.innerHTML = `
      <div class="plate noclick">
        <div class="clip" style="position:relative;overflow:hidden;${HALF ? "aspect-ratio:1/1" : ""}"><div class="inner" style="position:relative;${HALF ? "width:206.67%" : ""}">
          <video muted playsinline preload="auto" poster="${BASE}assets/demo/poster_t240.png" src="${BASE}assets/demo/ref_vs_std.mp4"></video>
          <svg class="ovl" viewBox="0 0 744 360" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%;display:none">
            <line x1="0" x2="360" y1="${360 - 37.5 / 75 * 360}" y2="${360 - 37.5 / 75 * 360}" stroke="#16191d" stroke-dasharray="8 6" stroke-width="2"/>
            <line x1="384" x2="744" y1="${360 - 37.5 / 75 * 360}" y2="${360 - 37.5 / 75 * 360}" stroke="#16191d" stroke-dasharray="8 6" stroke-width="2"/>
            <text x="737" y="${360 - 37.5 / 75 * 360 - 8}" text-anchor="end" font-size="16" font-family="Charis" fill="#16191d">outlet height</text>
          </svg>
        </div></div>
        <div class="labels">${HALF ? "<span>reference CFD</span><span></span>" : "<span>reference CFD</span><span>standard replay, f<sub>sd</sub> = 0.5</span>"}</div>
        <div class="controls">
          <button data-a="play">play</button><button data-a="reset">reset</button>
          <input type="range" min="0" max="${TMAX}" step="2" value="0">
          <span class="clock">t = 0 s</span><button data-a="outlet">outlet</button>
        </div>
        <div class="src"><span>mid-plane temperature, 293-333 K, decoded from the rendered frames (mean error ≤ 0.5 K)</span><b>thesis Ch 5</b></div>
        <div class="colorbar" style="margin-top:8px"></div><div class="cb-row"><span>293 K</span><span>313 K</span><span>333 K</span></div>
        <div class="fb" style="display:none"><video controls src="${BASE}assets/demo/ref_vs_std_fallback.mp4" style="width:100%"></video>
          <img src="${BASE}assets/demo/key_t240.png" style="width:48%;margin-top:8px"> <img src="${BASE}assets/demo/key_t598.png" style="width:48%;margin-top:8px"></div>
      </div>`;
    const v = root.querySelector("video"), r = root.querySelector("input"), c = root.querySelector(".clock");
    const play = root.querySelector('[data-a="play"]'), ovl = root.querySelector(".ovl");
    const sync = () => { const t = Math.min(TMAX, Math.round(v.currentTime * RATE / 2) * 2); r.value = t;
      c.textContent = `t = ${t} s` + (t <= INFLOW ? " · warm inflow" : " · cold inflow"); };
    v.addEventListener("timeupdate", sync);
    v.addEventListener("loadedmetadata", () => { v.currentTime = (opts.start || 240) / RATE; sync(); });
    v.addEventListener("ended", () => { play.textContent = "play"; play.classList.remove("on"); });
    r.addEventListener("input", () => { v.pause(); play.textContent = "play"; play.classList.remove("on"); v.currentTime = r.value / RATE; sync(); });
    root.querySelector('[data-a="reset"]').onclick = () => { v.pause(); v.currentTime = 0; play.textContent = "play"; play.classList.remove("on"); sync(); };
    play.onclick = () => { if (v.paused) { v.play(); play.textContent = "pause"; play.classList.add("on"); } else { v.pause(); play.textContent = "play"; play.classList.remove("on"); } };
    root.querySelector('[data-a="outlet"]').onclick = (e) => { const on = ovl.style.display === "none"; ovl.style.display = on ? "block" : "none"; e.target.classList.toggle("on", on); };
    const slide = root.closest(".slide");
    slide.addEventListener("slide:leave", () => { v.pause(); play.textContent = "play"; play.classList.remove("on"); });
    slide.addEventListener("slide:fallback", () => { const fb = root.querySelector(".fb"); const show = fb.style.display === "none";
      fb.style.display = show ? "block" : "none"; root.querySelector(".clip").style.display = show ? "none" : "block"; root.querySelector(".controls").style.display = show ? "none" : "flex"; });
  };

  /* === SNAPSHOT INSPECTOR === */
  window.SnapInspector = function (root, kind, runs, label) {
    const T = [60, 150, 240, 315, 450, 599];
    root.innerHTML = `<div class="plate noclick"><div class="snapgrid" style="grid-template-columns:repeat(${runs.length},1fr)">
      ${runs.map(([k, name, col]) => `<figure><img data-run="${k}" alt="${name}"><figcaption style="color:${col}">${name}</figcaption></figure>`).join("")}</div>
      <div class="controls">${T.map(t => `<button data-t="${t}">${t} s</button>`).join("")}</div>
      <div class="src"><span>${label}</span><b>stored solver snapshots</b></div></div>`;
    const set = (t) => { root.querySelectorAll("img").forEach(im => im.src = `${BASE}assets/snap/${kind}_${im.dataset.run}_${String(t).padStart(3, "0")}.png`);
      root.querySelectorAll("button").forEach(b => b.classList.toggle("on", +b.dataset.t === t)); };
    root.querySelectorAll("button").forEach(b => b.onclick = () => set(+b.dataset.t));
    set(+(root.dataset.t || 599));
  };

  /* === 1D LIMITER MODEL (thesis Fig 4.1, recomputed) === */
  window.LimiterModel = function (root, data) {
    const N = data.N, base = data.base, noise = data.noise, T0 = 293, DT = 40;
    root.innerHTML = `<div class="plate noclick"><canvas width="1300" height="560"></canvas>
      <div class="controls"><button data-a="play">play</button><button data-a="step">+1 step</button><button data-a="reset">reset</button>
      <span class="clock" style="min-width:420px;text-align:left"></span></div>
      <div class="src"><span>model front: 40 K across 60 cells, ν = −0.1 against limited s = 0.25 (not replay data); shaded: outside the data range</span><b>thesis Fig 4.1</b></div></div>`;
    const cv = root.querySelector("canvas"), g = cv.getContext("2d"), clk = root.querySelector(".clock");
    let un, li, k, timer = null;
    function negdiff(T) { const o = T.slice(); for (let i = 1; i < N - 1; i++) o[i] = T[i] + data.nu * (T[i + 1] - 2 * T[i] + T[i - 1]); return o; }
    function limited(T) {
      const lo = T.slice(), hi = T.slice();
      for (let i = 0; i < N - 1; i++) { lo[i] = Math.min(lo[i], T[i + 1]); hi[i] = Math.max(hi[i], T[i + 1]); }
      for (let i = 1; i < N; i++) { lo[i] = Math.min(lo[i], T[i - 1]); hi[i] = Math.max(hi[i], T[i - 1]); }
      const dE = new Array(N).fill(0);
      for (let a = 0; a < N - 1; a++) { const b = a + 1; if (T[a] === T[b]) continue;
        const [h, c] = T[a] > T[b] ? [a, b] : [b, a]; const dq = data.s * Math.min(hi[h] - T[h], T[c] - lo[c]);
        if (dq > 0) { dE[h] += dq; dE[c] -= dq; } }
      return T.map((v, i) => Math.min(hi[i], Math.max(lo[i], v + dE[i])));
    }
    function width(T) { const t = T.map(v => (v - T0) / DT); const cross = (L) => { for (let i = 0; i < N - 1; i++)
      if ((t[i] - L) * (t[i + 1] - L) <= 0 && t[i + 1] !== t[i]) return i + 0.5 + (L - t[i]) / (t[i + 1] - t[i]); return NaN; };
      return cross(0.9) - cross(0.1); }
    function panel(x0, T, col, title) {
      const W = 600, H = 470, y0 = 50, X = (v) => x0 + (v - 288) / (338 - 288) * W, Y = (i) => y0 + H - (i + 0.5) / N * H;
      g.fillStyle = "#efe9e6"; g.fillRect(X(288), y0, X(293) - X(288), H); g.fillRect(X(333), y0, X(338) - X(333), H);
      g.strokeStyle = "#cfc8bb"; g.lineWidth = 1; g.strokeRect(x0, y0, W, H);
      g.strokeStyle = "#8a9099"; g.setLineDash([6, 5]); g.beginPath(); base.forEach((v, i) => i ? g.lineTo(X(v), Y(i)) : g.moveTo(X(v), Y(i))); g.stroke(); g.setLineDash([]);
      g.strokeStyle = col; g.lineWidth = 3; g.beginPath(); T.forEach((v, i) => { const xv = X(Math.max(288, Math.min(338, v))); i ? g.lineTo(xv, Y(i)) : g.moveTo(xv, Y(i)); }); g.stroke();
      g.fillStyle = "#16191d"; g.font = "26px Charis"; g.fillText(title, x0, 34);
      g.fillStyle = "#7c838b"; g.font = "18px Charis";
      ["293", "313", "333"].forEach(s => g.fillText(s + " K", X(+s) - 20, y0 + H + 52 - 24 + 0));
    }
    function draw() {
      g.clearRect(0, 0, cv.width, cv.height);
      panel(20, un, "#55657a", "negative diffusion, ν = −0.1");
      panel(680, li, "#c4502f", "limited correction, s = 0.25");
      const out = Math.max(0, ...un.map(v => Math.max(v - 333, 293 - v)));
      clk.textContent = `step ${k}: width ${width(un).toFixed(1)} | ${width(li).toFixed(1)} cells` + (out > 1 ? ` · unlimited leaves range by ${out.toFixed(1)} K` : "");
    }
    function reset() { un = base.map((v, i) => v + noise[i]); li = base.slice(); k = 0; draw(); }
    function step() { if (k >= 60) return stop(); un = negdiff(un); li = limited(li); k++; draw(); }
    function stop() { clearInterval(timer); timer = null; const b = root.querySelector('[data-a="play"]'); b.textContent = "play"; b.classList.remove("on"); }
    root.querySelector('[data-a="play"]').onclick = (e) => { if (timer) return stop(); e.target.textContent = "pause"; e.target.classList.add("on"); timer = setInterval(step, 160); };
    root.querySelector('[data-a="step"]').onclick = () => { stop(); step(); };
    root.querySelector('[data-a="reset"]').onclick = () => { stop(); reset(); };
    root.closest(".slide").addEventListener("slide:leave", stop);
    reset();
  };
})();
