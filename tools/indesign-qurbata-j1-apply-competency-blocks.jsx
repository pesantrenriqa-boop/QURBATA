#target "InDesign"
(function () {
    if (app.documents.length === 0) { alert("QURBATA: tidak ada dokumen terbuka."); return; }
    var doc = app.activeDocument;
    if (doc.pages.length !== 40) { alert("QURBATA: aktifkan dokumen produksi 40 halaman. Pages sekarang: " + doc.pages.length); return; }

    var docFile;
    try { docFile = doc.fullName; } catch (_) {
        alert("QURBATA: dokumen produksi belum disimpan.");
        return;
    }

    var cursor = docFile.parent, repoRoot = null;
    while (cursor && cursor.exists) {
        if (cursor.name === "QURBATA") { repoRoot = cursor; break; }
        var parent = cursor.parent;
        if (!parent || parent.fsName === cursor.fsName) break;
        cursor = parent;
    }
    if (!repoRoot) {
        var fallback = Folder("C:/Users/hp/RIQA-GITHUB/QURBATA");
        if (fallback.exists) repoRoot = fallback;
    }
    if (!repoRoot) { alert("QURBATA: root repository tidak ditemukan."); return; }

    var dataFile = File(repoRoot.fsName + "/dist/indesign-template-data/QURBATA-J1-40P-COMPETENCY.tsv");
    if (!dataFile.exists) { alert("QURBATA: competency register belum dibuat.\n" + dataFile.fsName); return; }

    dataFile.encoding = "UTF-8";
    if (!dataFile.open("r")) { alert("QURBATA: tidak dapat membuka competency register."); return; }
    var rows = [], header = dataFile.readln().split("\t");
    while (!dataFile.eof) {
        var line = dataFile.readln();
        if (!line) continue;
        var parts = line.split("\t"), o = {};
        for (var i=0; i<header.length; i++) o[header[i]] = parts[i] || "";
        rows.push(o);
    }
    dataFile.close();
    if (rows.length !== 40) { alert("QURBATA: competency register harus 40 baris. Ditemukan: " + rows.length); return; }

    function getOrCreateParagraphStyle(name, pointSize, leading, justification) {
        var ps;
        try { ps = doc.paragraphStyles.itemByName(name); ps.name; }
        catch (_) { ps = doc.paragraphStyles.add({name:name}); }
        try {
            ps.appliedFont = "Arial";
            ps.fontStyle = "Regular";
            ps.pointSize = pointSize;
            ps.leading = leading;
            ps.justification = justification;
            ps.hyphenation = false;
            ps.spaceBefore = 0;
            ps.spaceAfter = 0;
            ps.leftIndent = 0;
            ps.rightIndent = 0;
            ps.firstLineIndent = 0;
            ps.tracking = 0;
        } catch (_) {}
        return ps;
    }

    var titleStyle = getOrCreateParagraphStyle("QURBATA - Judul Kompetensi", 10.5, 12.5, Justification.CENTER_ALIGN);
    var targetStyle = getOrCreateParagraphStyle("QURBATA - Target Kompetensi", 8.5, 10.5, Justification.CENTER_ALIGN);

    function removeOld(page, labelValue) {
        var frames = page.textFrames.everyItem().getElements();
        for (var i=frames.length-1; i>=0; i--) {
            try { if (frames[i].label === labelValue) frames[i].remove(); } catch (_) {}
        }
    }

    function addFrame(page, bounds, text, labelValue, paraStyle) {
        removeOld(page, labelValue);
        var tf = page.textFrames.add();
        tf.label = labelValue;
        tf.geometricBounds = bounds;
        tf.contents = text;
        try {
            tf.textFramePreferences.insetSpacing = [0.8, 2, 0.8, 2];
            tf.textFramePreferences.verticalJustification = VerticalJustification.CENTER_ALIGN;
            tf.strokeWeight = 0;
            tf.fillColor = doc.swatches.itemByName("None");
            tf.ignoreWrap = true;
        } catch (_) {}
        try {
            var para = tf.parentStory.paragraphs[0];
            para.appliedParagraphStyle = paraStyle;
            para.appliedFont = "Arial";
            para.fontStyle = "Regular";
            para.fillColor = doc.swatches.itemByName("Black");
        } catch (_) {}
        return tf;
    }

    var titleCount=0, targetCount=0, oversetCount=0;

    for (var p=0; p<40; p++) {
        var page=doc.pages[p], r=rows[p], b=page.bounds;
        var y1=Number(b[0]), x1=Number(b[1]), y2=Number(b[2]), x2=Number(b[3]);
        var h=y2-y1, w=x2-x1;

        var titleText=r.CompetencyCode+"  •  "+r.CompetencyTitle;
        var targetText="Target: "+r.CompetencyTarget;

        // Keep both blocks inside the existing blank band above the Tartil grid.
        var titleFrame=addFrame(
            page,
            [y1+h*0.118, x1+w*0.09, y1+h*0.151, x2-w*0.09],
            titleText,
            "QURBATA_COMPETENCY_TITLE",
            titleStyle
        );
        var targetFrame=addFrame(
            page,
            [y1+h*0.151, x1+w*0.09, y1+h*0.198, x2-w*0.09],
            targetText,
            "QURBATA_COMPETENCY_TARGET",
            targetStyle
        );
        titleCount++; targetCount++;
        try { if (titleFrame.overflows) oversetCount++; } catch (_) {}
        try { if (targetFrame.overflows) oversetCount++; } catch (_) {}
    }

    alert(
        "QURBATA competency block diperbaiki.\n\n"+
        "Pages: 40\n"+
        "Title blocks: "+titleCount+"\n"+
        "Target blocks: "+targetCount+"\n"+
        "Overset blocks: "+oversetCount+"\n\n"+
        "Style: QURBATA - Judul Kompetensi / Target Kompetensi\n"+
        "Font: Arial (Latin, independen dari style Tartil Arab)"
    );
})();