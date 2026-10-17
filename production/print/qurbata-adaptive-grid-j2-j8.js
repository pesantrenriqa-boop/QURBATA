/* QURBATA J2-J8 — adaptive A5 exercise renderer, review-only.
 * Requires verified text supplied by the caller; never invents Qur'anic tokens.
 * Usage: QurbataAdaptiveGrid.render(container, {jilid:6, rows:[
 *  {phase:'introduction',columns:2,content_type:'word',items:['...', '...']},
 *  {phase:'fluency',columns:1,content_type:'full_ayah',source_ref:'...',items:['...']}
 * ]});
 */
(function(root){
"use strict";
const phases=new Set(["introduction","transition","fluency","evaluation"]);
const types=new Set(["letter","word","phrase","ayah_excerpt","full_ayah"]);
function validate(data){
 if(!data||!Number.isInteger(data.jilid)||data.jilid<2||data.jilid>8)throw Error("Jilid must be 2–8");
 if(!Array.isArray(data.rows)||!data.rows.length)throw Error("Missing exercise rows");
 data.rows.forEach((row,i)=>{
  if(!phases.has(row.phase))throw Error("Invalid phase at row "+i);
  if(![1,2,3].includes(row.columns))throw Error("Invalid column count at row "+i);
  if(!types.has(row.content_type))throw Error("Invalid content type at row "+i);
  if(!Array.isArray(row.items)||row.items.length!==row.columns||row.items.some(v=>typeof v!=="string"||!v.trim()))throw Error("Each column needs exactly one nonempty item at row "+i);
  if(["ayah_excerpt","full_ayah"].includes(row.content_type)&&(!row.source_ref||typeof row.source_ref!=="string"))throw Error("Qur'an reference required at row "+i);
  if(row.phase==="fluency"&&row.columns!==1)throw Error("Fluency exercises must use one full-width box at row "+i);
  if(row.phase==="introduction"&&row.columns===1&&!row.allow_long_introduction)throw Error("New competency introduction requires 2–3 boxes, unless explicitly justified at row "+i);
 });
 return true;
}
function render(container,data){
 validate(data);
 if(!container||typeof container.appendChild!=="function")throw Error("Container element required");
 const doc=container.ownerDocument;
 const fragment=doc.createDocumentFragment();
 data.rows.forEach(row=>{
  const line=doc.createElement("div");line.className="exercise-row";line.dataset.columns=String(row.columns);line.dataset.phase=row.phase;line.setAttribute("dir","rtl");
  row.items.forEach(value=>{const cell=doc.createElement("div");cell.className="exercise-cell ar";cell.lang="ar";cell.setAttribute("dir","rtl");cell.textContent=value;line.appendChild(cell)});
  fragment.appendChild(line);
 });
 container.replaceChildren(fragment);
 return {rows:data.rows.length,boxes:data.rows.reduce((n,row)=>n+row.columns,0),status:"STAGING_NOT_TASHIH"};
}
root.QurbataAdaptiveGrid=Object.freeze({validate,render});
})(typeof window!=="undefined"?window:this);
