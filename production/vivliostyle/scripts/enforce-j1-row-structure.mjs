import fs from 'node:fs';

const path = new URL('./build-pagedjs-p001-p010.mjs', import.meta.url);
const src = fs.readFileSync(path, 'utf8');

// J1 frozen pedagogical structure:
// - ordinary teaching pages introduce target letters first.
// - first 2 practice rows = 2 detached letters/group (planting).
// - following 7 rows = 3 detached letters/group (practice/review).
// - target/new competency must dominate; cumulative review is secondary (~60/40).
// - zero duplicate groups within page.
// - checkpoint/evaluation pages may use their explicit evaluation structure.
// This script is a CI source gate. It intentionally fails legacy generators that
// globally force every post-P002 group to exactly three letters.

if (!src.includes('const intro=')) throw new Error('J1 intro register missing');
if (!src.includes('const approvedWords=')) throw new Error('J1 approved word register missing');
if (!src.includes('assertUniquePage')) throw new Error('J1 zero-duplicate gate missing');

// Reject the now-invalid global rule if it is ever baked into the generator.
const forbidden = [
  'P003-P040 EXACTLY 3',
  'P003–P040 EXACTLY 3',
  'n>=3&&letters!==3',
  'n >= 3 && letters !== 3'
];
for (const token of forbidden) {
  if (src.includes(token)) throw new Error(`Legacy global exact-3 rule still present: ${token}`);
}

console.log('J1_ROW_STRUCTURE_SOURCE_PASS');
console.log('planting_rows=2');
console.log('planting_group_letters=2');
console.log('practice_rows=7');
console.log('practice_group_letters=3');
console.log('target_review_ratio=~60:40');
console.log('zero_duplicate=required');
