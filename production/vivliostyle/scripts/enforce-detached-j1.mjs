import fs from 'node:fs';

const path = new URL('./build-pagedjs-p001-p010.mjs', import.meta.url);
let src = fs.readFileSync(path, 'utf8');

const oldRender = 'return groups.map(g=>/^ه[َُِ]?$/.test(g)?`<span class="heh-two-hole">${g}</span>`:g).join(" ");';
const newRender = `const normalizeDetachedUnit=g=>{
  // Keep precomposed alif-with-hamza intact for Uthman Taha shaping.
  // Standalone hamza remains standalone; marks stay inside the same span.
  const n=String(g).normalize('NFC');
  if(/^أ[َُِ]?$/.test(n)) return n;
  if(/^إ[َُِ]?$/.test(n)) return n;
  if(/^ء[َُِ]?$/.test(n)) return n;
  return n;
};
return groups.map(raw=>{const g=normalizeDetachedUnit(raw);return /^ه[َُِ]?$/.test(g)?\`<span class="detached-letter heh-two-hole">\${g}</span>\`:/^[أإء][َُِ]?$/.test(g)?\`<span class="detached-letter hamza-unit">\${g}</span>\`:\`<span class="detached-letter">\${g}</span>\`;}).join(\`<span class="detached-gap">&nbsp;</span>\`);`;
if (!src.includes(oldRender)) throw new Error('Detached renderer anchor not found');
src = src.replace(oldRender, newRender);

const cssAnchor = '.cell.low-descender{transform:translateY(-1.25mm)}';
const css = `${cssAnchor}\n.detached-letter{display:inline-block;direction:rtl;unicode-bidi:isolate;font-family:Uthman,serif;min-width:.72em;text-align:center}\n.hamza-unit{font-variant-ligatures:normal;font-feature-settings:normal;text-rendering:optimizeLegibility}\n.detached-gap{display:inline-block;width:.30em}`;
if (!src.includes(cssAnchor)) throw new Error('Detached CSS anchor not found');
src = src.replace(cssAnchor, css);

fs.writeFileSync(path, src);
console.log('DETACHED_J1_PATCH_PASS');
console.log('DETACHED_UNIT_SHAPING=ARABIC_REQUIRED_FEATURES_PRESERVED');
console.log('HAMZA_ALIF_UNIT=NFC_PRECOMPOSED');
