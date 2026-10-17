/* QURBATA J2-J8 adaptive grid: dependency-free test runner.
 * Browser: include after qurbata-adaptive-grid-j2-j8.js; Node:
 *   node -e "global.window=global;require('./qurbata-adaptive-grid-j2-j8.js');require('./qurbata-adaptive-grid-j2-j8-tests.js')"
 * Exit/fail if any assertion fails. No Quranic source is fabricated.
 */
(function(root){
"use strict";
const api=root.QurbataAdaptiveGrid;
if(!api||typeof api.validate!=="function")throw Error("Load adaptive renderer first");
let passed=0;
function ok(name,record){api.validate(record);passed++;return name}
function fail(name,record){let threw=false;try{api.validate(record)}catch(e){threw=true}if(!threw)throw Error("Expected rejection: "+name);passed++}
const intro={phase:"introduction",columns:3,content_type:"word",items:["بَ","تَ","ثَ"]};
const phrase={phase:"transition",columns:2,content_type:"phrase",items:["قَرَأَ","كَتَبَ"]};
const fluency={phase:"fluency",columns:1,content_type:"phrase",items:["قَرَأَ الطَّالِبُ"]};
const ayah={phase:"fluency",columns:1,content_type:"full_ayah",items:["[SOURCE VERIFIED TEXT REQUIRED]"],source_ref:"[SOURCE REF REQUIRED]"};
ok("J2 mixed introduction transition fluency",{jilid:2,rows:[intro,phrase,fluency]});
ok("J6 all full-width fluency",{jilid:6,rows:[fluency,ayah]});
ok("J8 documented long introduction",{jilid:8,rows:[{phase:"introduction",columns:1,content_type:"phrase",items:["قَرَأَ الطَّالِبُ"],introduction_rationale:"Latihan lanjutan memerlukan konteks utuh"}]});
fail("J2 cannot use one-column introduction without exception",{jilid:2,rows:[{...fluency,phase:"introduction"}]});
fail("J6 introduction exception needs rationale",{jilid:6,rows:[{...fluency,phase:"introduction"}]});
fail("Full ayah cannot be split into 2 columns",{jilid:6,rows:[{...ayah,columns:2,items:["a","b"]}]});
fail("Quranic excerpt requires source reference",{jilid:3,rows:[{...fluency,content_type:"ayah_excerpt"}]});
fail("Fluency cannot use 3 boxes",{jilid:3,rows:[{...intro,phase:"fluency"}]});
fail("Evaluation cannot use 2 boxes",{jilid:5,rows:[{...phrase,phase:"evaluation"}]});
fail("Unsupported jilid",{jilid:1,rows:[intro]});
fail("Wrong box count",{jilid:3,rows:[{...intro,items:["بَ"]}]});
root.QURBATA_GRID_TEST_RESULT={passed,failed:0,status:"PASS",note:"Structural tests only; no Quranic tashih or PDF render verification"};
if(typeof console!=="undefined"&&console.log)console.log("QURBATA adaptive grid tests PASS: "+passed);
})(typeof window!=="undefined"?window:this);
