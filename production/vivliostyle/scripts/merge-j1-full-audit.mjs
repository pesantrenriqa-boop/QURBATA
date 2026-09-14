import fs from "node:fs/promises";
import path from "node:path";
import { PDFDocument } from "pdf-lib";

const root=path.resolve(import.meta.dirname,"..");
const inputs=[
  "QURBATA-J1-P001-P010-AUDIT.pdf",
  "QURBATA-J1-P011-P020-AUDIT.pdf",
  "QURBATA-J1-P021-P030-AUDIT.pdf",
  "QURBATA-J1-P031-P040-AUDIT.pdf"
].map(name=>path.join(root,"dist",name));
const out=await PDFDocument.create();
for(const file of inputs){
  const bytes=await fs.readFile(file);
  const src=await PDFDocument.load(bytes);
  if(src.getPageCount()!==10)throw new Error(`${path.basename(file)} must contain 10 pages`);
  const pages=await out.copyPages(src,src.getPageIndices());
  pages.forEach(p=>out.addPage(p));
}
if(out.getPageCount()!==40)throw new Error(`Full J1 expected 40 pages, got ${out.getPageCount()}`);
out.setTitle("QURBATA JILID 1 — P001-P040 AUDIT");
out.setSubject("Frozen curriculum audit build");
out.setProducer("QURBATA Vivliostyle block pipeline + pdf-lib merge");
const bytes=await out.save({useObjectStreams:false});
await fs.writeFile(path.join(root,"dist/QURBATA-J1-P001-P040-AUDIT.pdf"),bytes);
console.log("Merged QURBATA J1 P001-P040: 40 pages.");
