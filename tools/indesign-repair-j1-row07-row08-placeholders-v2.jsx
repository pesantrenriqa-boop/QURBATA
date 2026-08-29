#target "InDesign"

(function () {
    if (app.documents.length === 0) { alert("QURBATA: tidak ada dokumen terbuka."); return; }
    var doc = app.activeDocument;
    if (doc.pages.length !== 1) { alert("QURBATA: aktifkan template 1 halaman. Pages: " + doc.pages.length); return; }

    var page = doc.pages[0];
    var frames = page.textFrames.everyItem().getElements();

    function ctr(tf) {
        var g=tf.geometricBounds;
        return {x:(Number(g[1])+Number(g[3]))/2,y:(Number(g[0])+Number(g[2]))/2,w:Number(g[3])-Number(g[1]),h:Number(g[2])-Number(g[0])};
    }

    // Identify the repeated tartil grid by dominant frame width/height, independent of contents.
    var buckets={};
    for (var i=0;i<frames.length;i++) {
        var c=ctr(frames[i]);
        var key=Math.round(c.w)+"x"+Math.round(c.h);
        if (!buckets[key]) buckets[key]=[];
        buckets[key].push({tf:frames[i],x:c.x,y:c.y,w:c.w,h:c.h});
    }
    var best=null;
    for (var k in buckets) {
        if (!best || buckets[k].length>best.length) best=buckets[k];
    }
    if (!best || best.length<24) { alert("QURBATA: grid 4x8 tidak terdeteksi. Tidak ada perubahan."); return; }

    // Cluster dominant grid frames into rows.
    best.sort(function(a,b){return a.y-b.y;});
    var rows=[], tol=5;
    for (var j=0;j<best.length;j++) {
        var it=best[j], found=-1;
        for (var r=0;r<rows.length;r++) if (Math.abs(rows[r].y-it.y)<=tol) {found=r;break;}
        if (found<0) rows.push({y:it.y,items:[it]});
        else { rows[found].items.push(it); rows[found].y=(rows[found].y*(rows[found].items.length-1)+it.y)/rows[found].items.length; }
    }
    // Keep rows having exactly four grid cells.
    var gridRows=[];
    for (var q=0;q<rows.length;q++) if (rows[q].items.length===4) gridRows.push(rows[q]);
    gridRows.sort(function(a,b){return a.y-b.y;});
    if (gridRows.length<8) { alert("QURBATA: hanya menemukan "+gridRows.length+" row grid lengkap. Tidak ada perubahan."); return; }
    gridRows=gridRows.slice(0,8);

    var changed=[];
    for (var rr=6;rr<=7;rr++) {
        var items=gridRows[rr].items;
        items.sort(function(a,b){return b.x-a.x;}); // rightmost = Cell01
        for (var cc=0;cc<4;cc++) {
            var field="Row"+("0"+(rr+1)).slice(-2)+"Cell"+("0"+(cc+1)).slice(-2);
            var tf=items[cc].tf;
            var current="";
            try { current=String(tf.contents); } catch(_){}
            // Preserve the already-working rightmost Cell01. Repair the other three.
            if (cc>0) {
                tf.contents="<<"+field+">>";
                changed.push(field);
            }
        }
    }

    alert("QURBATA repair V2 selesai.\nDipasang: "+changed.length+"\n"+changed.join("\n")+"\n\nCentang Preview lagi.");
})();