// Zía · componente oficial de Intezia (fuente única) · v4 · 10-oct-2026
// Uso: Zia.svg({v:"D"|"N", eyes:"normal|happy|surp|tired|worried|wink|closed", aL, aR, limbs, feet, look:[x,y], tilt, mouth, sweat, view:"front|34|side|back"})
// Coordenadas locales: base del cuerpo en y=0, centro en x=0, alto 232, base 260. viewBox -175 -275 350 315.
// Brazos: 0 = reposo (colgando hacia afuera). aL positivo sube el izquierdo; aR negativo sube el derecho.
// Clases para animar con GSAP: .zaL .zaR (svgOrigin "-78 -92" / "78 -92"), .zfL .zfR, .zbody, .zeyes y una por cada ojo:
// .ze-normal .ze-happy .ze-surp .ze-tired .ze-worried .ze-wink .ze-closed, mas .zmouth y .zsweat.
(function (root) {
  function roundedTri(P, r) {
    let d = "";
    P.forEach((p, i) => {
      const a = P[(i + P.length - 1) % P.length], b = P[(i + 1) % P.length];
      const la = Math.hypot(a[0] - p[0], a[1] - p[1]), lb = Math.hypot(b[0] - p[0], b[1] - p[1]);
      const s = [p[0] + (a[0] - p[0]) * r / la, p[1] + (a[1] - p[1]) * r / la];
      const e = [p[0] + (b[0] - p[0]) * r / lb, p[1] + (b[1] - p[1]) * r / lb];
      d += (i ? "L" : "M") + s[0].toFixed(1) + " " + s[1].toFixed(1) + " Q" + p[0] + " " + p[1] + " " + e[0].toFixed(1) + " " + e[1].toFixed(1);
    });
    return d + "Z";
  }
  const BODY = roundedTri([[0, -232], [130, 0], [-130, 0]], 34);
  const BODY_SIDE = roundedTri([[0, -232], [86, 0], [-86, 0]], 30);

  const PAL = {
    D: { body: ["#FFF27E", "#FFCB1F", "#F7941D", "#E0621A", "#B53F10"], stops: [0, .28, .58, .84, 1], limb: ["#FFB431", "#D25A18"], foot: ["#E8741E", "#9E3510"],
         eye: "#1b0d03", glint: "#fff", blush: "#FF5A36", blushO: .3, hiO: .75, ao: .7 },
    N: { body: ["#4a4a4a", "#1c1c1c", "#030303"], stops: [0, .45, 1], limb: ["#3a3a3a", "#080808"], foot: ["#2a2a2a", "#000"],
         eye: "#FFD300", glint: "#fff", blush: "#FFD300", blushO: .16, hiO: .4, ao: 0 }
  };

  function defs() {
    if (typeof document === "undefined" || document.getElementById("zia-defs")) return;
    let g = "";
    for (const k of ["D", "N"]) {
      const P = PAL[k];
      g += `<linearGradient id="zia${k}b" x1="0" y1="-235" x2="0" y2="5" gradientUnits="userSpaceOnUse">${P.body.map((c, i) => `<stop offset="${P.stops[i]}" stop-color="${c}"/>`).join("")}</linearGradient>`;
      g += `<linearGradient id="zia${k}l" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${P.limb[0]}"/><stop offset="1" stop-color="${P.limb[1]}"/></linearGradient>`;
      g += `<linearGradient id="zia${k}f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${P.foot[0]}"/><stop offset="1" stop-color="${P.foot[1]}"/></linearGradient>`;
    }
    g += `<radialGradient id="ziaHi" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>`;
    g += `<radialGradient id="ziaAO" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#5a1a00" stop-opacity="1"/><stop offset="1" stop-color="#5a1a00" stop-opacity="0"/></radialGradient>`;
    g += `<radialGradient id="ziaSh" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#000" stop-opacity=".45"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>`;
    g += `<clipPath id="ziaClipF"><path d="${BODY}"/></clipPath><clipPath id="ziaClipS"><path d="${BODY_SIDE}"/></clipPath>`;
    const s = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    s.setAttribute("id", "zia-defs"); s.setAttribute("width", "0"); s.setAttribute("height", "0");
    s.setAttribute("style", "position:absolute;width:0;height:0;overflow:hidden");
    s.innerHTML = `<defs>${g}</defs>`;
    document.body.insertBefore(s, document.body.firstChild);
  }

  // Brazo "nub": un ovalo que nace detras del cuerpo. Sin bola, sin dedos.
  function arm(side, k, rot, sc) {
    const sx = side < 0 ? -78 : 78, sy = -92, rest = side < 0 ? -42 : 42;
    return `<g class="${side < 0 ? "zaL" : "zaR"}" transform="rotate(${rot} ${sx} ${sy}) translate(${sx} ${sy}) scale(${sc}) translate(${-sx} ${-sy})">` +
      `<g transform="rotate(${rest} ${sx} ${sy})"><ellipse cx="${sx + side * 30}" cy="${sy}" rx="38" ry="16" fill="url(#zia${k}l)"/>` +
      `<ellipse cx="${sx + side * 44}" cy="${sy - 5}" rx="13" ry="4.5" fill="#fff" opacity="${k === "N" ? .1 : .22}"/></g></g>`;
  }
  function foot(side, k, sc) {
    const x = side * 56;
    return `<g class="${side < 0 ? "zfL" : "zfR"}" transform="translate(${x} 6) scale(${sc}) translate(${-x} -6)"><ellipse cx="${x}" cy="6" rx="36" ry="18" fill="url(#zia${k}f)"/><ellipse cx="${x - 8}" cy="0" rx="14" ry="5" fill="#fff" opacity="${k === "N" ? .08 : .18}"/></g>`;
  }
  function eyes(P, active, look) {
    const E = P.eye, G = P.glint, on = (n) => (n === active ? 1 : 0);
    const half = (cx) => `<path d="M${cx - 12} -98 A12 24 0 0 0 ${cx + 12} -98 Z" fill="${E}"/>`;
    return `<g class="zeyes" transform="translate(${look[0]} ${look[1]})">` +
      `<g class="ze-normal" opacity="${on("normal")}"><ellipse cx="-30" cy="-98" rx="12" ry="24" fill="${E}"/><ellipse cx="30" cy="-98" rx="12" ry="24" fill="${E}"/><ellipse cx="-26" cy="-108" rx="4.5" ry="6" fill="${G}"/><ellipse cx="34" cy="-108" rx="4.5" ry="6" fill="${G}"/></g>` +
      `<g class="ze-happy" opacity="${on("happy")}"><path d="M-44 -94 q14 -20 28 0 M16 -94 q14 -20 28 0" stroke="${E}" stroke-width="7.5" stroke-linecap="round" fill="none"/></g>` +
      `<g class="ze-surp" opacity="${on("surp")}"><circle cx="-30" cy="-100" r="17" fill="${E}"/><circle cx="30" cy="-100" r="17" fill="${E}"/><circle cx="-25" cy="-106" r="5" fill="${G}"/><circle cx="35" cy="-106" r="5" fill="${G}"/></g>` +
      `<g class="ze-tired" opacity="${on("tired")}">${half(-30)}${half(30)}</g>` +
      `<g class="ze-worried" opacity="${on("worried")}"><g transform="rotate(-16 -30 -98)">${half(-30)}</g><g transform="rotate(16 30 -98)">${half(30)}</g></g>` +
      `<g class="ze-wink" opacity="${on("wink")}"><ellipse cx="-30" cy="-98" rx="12" ry="24" fill="${E}"/><ellipse cx="-26" cy="-108" rx="4.5" ry="6" fill="${G}"/><path d="M17 -96 h26" stroke="${E}" stroke-width="7.5" stroke-linecap="round"/></g>` +
      `<g class="ze-closed" opacity="${on("closed")}"><path d="M-43 -96 h26 M17 -96 h26" stroke="${E}" stroke-width="7.5" stroke-linecap="round"/></g>` +
      `</g>`;
  }

  function svg(o) {
    o = Object.assign({ v: "D", eyes: "normal", aL: 0, aR: 0, limbs: 1, feet: 1, look: [0, 0], tilt: 0, mouth: 0, sweat: 0, view: "front", shadow: 1 }, o || {});
    defs();
    const k = o.v === "N" ? "N" : "D", P = PAL[k];
    const side = o.view === "side", back = o.view === "back", tq = o.view === "34";
    const B = side ? BODY_SIDE : BODY, clip = side ? "ziaClipS" : "ziaClipF", hw = side ? 86 : 130;
    let s = `<svg viewBox="-175 -275 350 315" xmlns="http://www.w3.org/2000/svg" class="zia-svg">`;
    if (o.shadow) s += `<ellipse cx="0" cy="16" rx="${hw + 10}" ry="14" fill="url(#ziaSh)"/>`;
    // pies fuera de la inclinacion: se quedan en el piso
    if (side) s += `<g class="zfR"><ellipse cx="14" cy="6" rx="44" ry="18" fill="url(#zia${k}f)" opacity="${o.feet * o.limbs}"/></g>`;
    else s += foot(-1, k, o.feet * o.limbs) + foot(1, k, o.feet * o.limbs);
    s += `<g transform="rotate(${o.tilt} 0 -10)">`;
    if (side) s += arm(1, k, o.aR, o.limbs);
    else s += arm(-1, k, o.aL, o.limbs) + arm(1, k, o.aR, o.limbs);
    // cuerpo
    s += `<g class="zbody"><path d="${B}" fill="url(#zia${k}b)"/><g clip-path="url(#${clip})">`;
    if (P.ao) s += `<ellipse cx="0" cy="22" rx="175" ry="70" fill="url(#ziaAO)" opacity="${P.ao}"/>`;
    if (back) s += `<ellipse cx="40" cy="-160" rx="60" ry="50" fill="url(#ziaHi)" opacity="${P.hiO * .85}"/>`;
    else s += `<ellipse cx="-40" cy="-160" rx="62" ry="52" fill="url(#ziaHi)" opacity="${P.hiO}"/><ellipse cx="-78" cy="-70" rx="22" ry="60" fill="url(#ziaHi)" opacity="${P.hiO * .45}" transform="rotate(28 -78 -70)"/>`;
    if (tq) s += `<path d="M28 -232 L135 4 L40 4 Z" fill="#000" opacity="${k === "N" ? .28 : .16}"/>`;
    s += `</g></g>`;
    // cara
    if (!back) {
      if (side) {
        s += `<ellipse cx="-50" cy="-98" rx="7" ry="22" fill="${P.eye}"/><ellipse cx="-48" cy="-108" rx="2.5" ry="5" fill="${P.glint}"/>`;
      } else {
        const lx = o.look[0] + (tq ? -22 : 0);
        s += `<ellipse cx="${-56 + (tq ? -10 : 0)}" cy="-62" rx="16" ry="8" fill="${P.blush}" opacity="${P.blushO}"/>`;
        if (!tq) s += `<ellipse cx="56" cy="-62" rx="16" ry="8" fill="${P.blush}" opacity="${P.blushO}"/>`;
        let ey = eyes(P, o.eyes, [lx, o.look[1]]);
        if (tq) ey = ey.replace(/<ellipse cx="30" cy="-98" rx="12"/g, '<ellipse cx="30" cy="-98" rx="8.5"');
        s += ey;
        s += `<path class="zmouth" opacity="${o.mouth ? 1 : 0}" d="M-12 -58 q12 12 24 0" stroke="${P.eye}" stroke-width="5" stroke-linecap="round" fill="none"/>`;
        s += `<path class="zsweat" opacity="${o.sweat ? 1 : 0}" d="M82 -170 q-12 18 0 26 q12 -8 0 -26z" fill="#fff"/>`;
      }
    }
    return s + `</g></svg>`;
  }

  // Firma: bloque de la A. Devuelve la geometria del triangulo del logo para escalar a Zía.
  const TRI_IN_LOGO = { note: "triangulo del logo: base 60 px de 1353 en intezia-white.png; Zía visible mide 245 de base" };

  root.Zia = { svg, BODY, BODY_SIDE, PAL, defs, TRI_IN_LOGO, version: "4" };
})(typeof window !== "undefined" ? window : globalThis);
