import fs from "node:fs/promises";

const file = new URL("./build-pagedjs-p001-p010.mjs", import.meta.url);
let src = await fs.readFile(file, "utf8");

const re = /const checkpoint40=\[[^;]+\];/u;
const replacement = 'const checkpoint40=["بَحَثَ","دَرَسَ","صَبَرَ","ضَرَبَ","عَبَدَ","فَتَحَ","قَرَأَ","كَتَبَ","تَبِعَ","فَرِحَ","شَرِبَ","خَسِرَ","عَلِمَ","عَمِلَ","سَمِعَ","حَفِظَ","كَبُرَ","حَسُنَ","ضَعُفَ","غَفَرَ","نَصَرَ","وَجَدَ","شَهِدَ","وَرِثَ"];';

if (!re.test(src)) throw new Error("checkpoint40 allocation not found");
src = src.replace(re, replacement);
await fs.writeFile(file, src, "utf8");
console.log("P040_ZERO_DUPLICATE_PREPARED=24/24");
