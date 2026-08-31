#target "InDesign"
(function () {
    if (app.documents.length === 0) { alert("QURBATA: tidak ada dokumen terbuka."); return; }
    var doc = app.activeDocument;
    if (doc.pages.length !== 40) { alert("QURBATA: aktifkan dokumen produksi 40 halaman. Pages sekarang: " + doc.pages.length); return; }
    var scriptFile = File($.fileName);
    var repoRoot = scriptFile.parent.parent;
    var dataFile = File(repoRoot.fsName + "/dist/indesign-template-data/QURBATA-J1-40P-COMPETENCY.tsv");
    if (!dataFile.exists) { alert("QURBATA: competency register belum dibuat.\n" + dataFile.fsName); return; }
    dataFile.encoding = "UTF-8";
    if (!dataFile.open("r")) { alert("QURBATA: tidak dapat membuka competency register."); return; }
    var rows = [];
    var header = dataFile.readln().split("\t");
    while (!dataFile.eof) {
        var line = dataFile.readln();
        if (!line) continue;
        var parts = line.split("\t");
        var o = {};
        for (var i = 0; i < header.length; i++) o[header[i]] = parts[i] || "";
        rows.push(o);
    }
    dataFile.close();
    if (rows.length !== 40) { alert("QURBATA: competency register harus 40 baris. Ditemukan: " + rows.length); return; }
    function removeOld(page, labelValue) {
        var frames = page.textFrames.everyItem().getElements();
        for (var i = frames.length - 1; i >= 0; i--) { try { if (frames[i].label === labelValue) frames[i].remove(); } catch (_) {} }
    }
    function addFrame(page, bounds, text, size, labelValue, align) {
        removeOld(page, labelValue);
        var tf = page.textFrames.add();
        tf.label = labelValue;
        tf.geometricBounds = bounds;
        tf.contents = text;
        try { tf.textFramePreferences.insetSpacing = [1.5,2,1.5,2]; tf.strokeWeight = 0; tf.fillColor = doc.swatches.itemByName("None"); } catch (_) {}
        try { var t=tf.parentStory.texts[0]; t.pointSize=size; t.leading=size*1.15; t.justification=align; } catch (_) {}
        return tf;
    }
    for (var p=0; p<40; p++) {
        var page=doc.pages[p], r=rows[p], b=page.bounds;
        var y1=Number(b[0]), x1=Number(b[1]), y2=Number(b[2]), x2=Number(b[3]);
        var h=y2-y1, w=x2-x1;
        var titleText=r.CompetencyCode+"  •  "+r.CompetencyTitle;
        var targetText="Target: "+r.CompetencyTarget;
        addFrame(page,[y1+h*0.115,x1+w*0.09,y1+h*0.147,x2-w*0.09],titleText,10.5,"QURBATA_COMPETENCY_TITLE",Justification.CENTER_ALIGN);
        addFrame(page,[y1+h*0.148,x1+w*0.10,y1+h*0.183,x2-w*0.10],targetText,8.5,"QURBATA_COMPETENCY_TARGET",Justification.CENTER_ALIGN);
    }
    alert("QURBATA competency block selesai.\n\nPages: 40\nTitle blocks: 40\nTarget blocks: 40\n\nEmpat halaman khusus tetap menunggu mapping/pengesahan final.");
})();