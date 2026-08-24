#target "InDesign"
(function(){
  if(app.documents.length===0){alert('Buka dokumen hasil Data Merge terlebih dahulu.');return;}
  var doc=app.activeDocument;
  var hidden=0, kept=0;
  for(var i=0;i<doc.textFrames.length;i++){
    var tf=doc.textFrames[i];
    try{
      var txt=tf.contents;
      var clean=(txt===undefined||txt===null)?'':String(txt).replace(/[\s\uFEFF\u200B\u200C\u200D]+/g,'');
      if(clean===''){
        tf.strokeWeight=0;
        try{tf.fillColor=doc.swatches.itemByName('None');}catch(e1){}
        hidden++;
      }else{
        kept++;
      }
    }catch(e){}
  }
  alert('QURBATA empty-frame cleanup selesai.\nFrame kosong disembunyikan: '+hidden+'\nFrame berisi dipertahankan: '+kept);
})();
