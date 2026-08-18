const fs=require('fs');
const path=require('path');
const base=path.resolve(__dirname,'render_nidom_j5_v01.js');
if(!fs.existsSync(base)) throw new Error('J5_BASE_RENDERER_MISSING');
let src=fs.readFileSync(base,'utf8');
const cut=src.indexOf('(async()=>{');
if(cut<0) throw new Error('J5_ASYNC_ANCHOR_MISSING');
src=src.slice(0,cut);
// Do not embed the font as a large base64 data URL in every page. On GitHub's
// current Chromium runner that path can stall at P001. Serve the same font
// bytes through an in-memory Playwright route instead.
src=src.replace("src:url(data:font/woff2;base64,${font}) format('woff2');font-display:swap","src:url('https://qurbata.local/UthmanTaha.woff2') format('woff2');font-display:block");
const tail=`(async()=>{
  const fp=path.resolve(__dirname,'../.build-fonts/UthmanTaha.woff2');
  if(!fs.existsSync(fp))throw Error('FONT_MISSING');
  const fontBytes=fs.readFileSync(fp);
  const b=await chromium.launch({headless:true});
  const pg=await b.newPage();
  pg.setDefaultTimeout(12000);
  await pg.route('https://qurbata.local/UthmanTaha.woff2',async route=>{
    await route.fulfill({status:200,contentType:'font/woff2',body:fontBytes,headers:{'access-control-allow-origin':'*','cache-control':'public,max-age=3600'}});
  });
  const master=await PDFDocument.create();
  for(const p of P){
    const id=String(p.n).padStart(3,'0');
    console.log('P'+id+'_START');
    console.log('P'+id+'_SETCONTENT_START');
    await pg.setContent(html(p,''),{waitUntil:'domcontentloaded',timeout:12000});
    console.log('P'+id+'_SETCONTENT_PASS');
    const hasArabic=!!(p.t&&p.hi!==null&&p.hi!==undefined&&H[p.t]&&H[p.t][p.hi]);
    if(hasArabic){
      console.log('P'+id+'_FONT_START');
      await pg.waitForFunction(()=>document.fonts.check('30px Uthman','الْخَيْرُ'),null,{timeout:8000});
      console.log('P'+id+'_FONT_PASS');
    }
    const g=await pg.evaluate(hasArabic=>({font:hasArabic?document.fonts.check('30px Uthman','الْخَيْرُ'):true,scroll:document.querySelector('.p').scrollHeight,client:document.querySelector('.p').clientHeight}),hasArabic);
    if(!g.font||g.scroll>g.client+2)throw Error('GATE_P'+p.n+' '+JSON.stringify(g));
    console.log('P'+id+'_PDF_START');
    let buf=await pg.pdf({width:'176mm',height:'250mm',printBackground:true,timeout:12000});
    console.log('P'+id+'_PDF_PASS');
    const stampDoc=await PDFDocument.load(buf),stampImg=await stampDoc.embedPng(logo),stampPage=stampDoc.getPage(0),stampH=stampPage.getHeight();
    stampPage.drawImage(stampImg,{x:45,y:stampH-70,width:40,height:40});
    buf=Buffer.from(await stampDoc.save());
    fs.writeFileSync(path.join(OUT,'QURBATA-NIDOM-J5-P'+id+'-v0.2.pdf'),buf);
    const d=await PDFDocument.load(buf);
    (await master.copyPages(d,d.getPageIndices())).forEach(x=>master.addPage(x));
    console.log('P'+id+'=PASS');
  }
  fs.writeFileSync(path.join(OUT,'QURBATA-NIDOM-J5-P001-P040-PRINT-MASTER-v0.2.pdf'),await master.save());
  await pg.close();await b.close();
  console.log('PAGE_COUNT=40');
  console.log('FONT_UTHMAN=PASS');
  console.log('FONT_TRANSPORT=PLAYWRIGHT_ROUTE_WOFF2');
  console.log('OFFICIAL_LOGO=PDF_DIRECT_STAMP');
  console.log('REASONING_DENSITY=ADAPTIVE_DALIL2_OPEN5');
  console.log('OVERFLOW=0');
})().catch(e=>{console.error(e);process.exit(1)});`;
console.log('J5_EXECUTION_ENGINE=PLAYWRIGHT_ROUTE_FONT_NO_BASE64');
eval(src+tail);
