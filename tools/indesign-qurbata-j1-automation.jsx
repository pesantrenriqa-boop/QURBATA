#target "InDesign"

(function () {
    function trimText(s) {
        if (s === null || s === undefined) return "";
        return String(s).replace(/^\s+|\s+$/g, "");
    }
    function safeText(s) {
        if (s === null || s === undefined) return "";
        return String(s).replace(/\t/g, " ").replace(/\r/g, " ").replace(/\n/g, " ");
    }
    function ensureFolder(folder) {
        if (!folder.exists) folder.create();
    }
    function getPageName(tf) {
        try { if (tf.parentPage) return tf.parentPage.name; } catch (_) {}
        return "";
    }
    function getBounds(tf) {
        try {
            var g = tf.geometricBounds;
            return [g[0], g[1], g[2], g[3]].join("|");
        } catch (_) { return ""; }
    }
    function getTextProps(tf) {
        var out = { font:"", size:"", leading:"", paraStyle:"", objectStyle:"" };
        try {
            if (tf.parentStory && tf.parentStory.texts.length > 0) {
                var t = tf.parentStory.texts[0];
                try { out.font = t.appliedFont.name; } catch (_) {}
                try { out.size = t.pointSize; } catch (_) {}
                try { out.leading = t.leading; } catch (_) {}
                try { out.paraStyle = t.appliedParagraphStyle.name; } catch (_) {}
            }
        } catch (_) {}
        try { out.objectStyle = tf.appliedObjectStyle.name; } catch (_) {}
        return out;
    }
    function writeUtf8(file, text) {
        file.encoding = "UTF-8";
        file.lineFeed = "Windows";
        if (!file.open("w")) throw new Error("Cannot write: " + file.fsName);
        file.write(text);
        file.close();
    }
    function recompose(tf) {
        try { if (tf.parentStory) tf.parentStory.recompose(); }
        catch (_) { try { app.activeDocument.recompose(); } catch (__) {} }
    }
    function isOverset(tf) {
        try { return tf.overflows === true; } catch (_) { return false; }
    }
    function fitOversetFrame(tf, minPt, stepPt) {
        var result = { changed:false, fixed:false, originalSize:"", finalSize:"", originalLeading:"", finalLeading:"" };
        if (!isOverset(tf)) return result;

        var t = null;
        try {
            if (!tf.parentStory || tf.parentStory.texts.length < 1) return result;
            t = tf.parentStory.texts[0];
        } catch (_) { return result; }

        var originalSize = 0;
        try { originalSize = Number(t.pointSize); } catch (_) {}
        if (!originalSize || isNaN(originalSize)) originalSize = 36;

        var originalLeading = "";
        try { originalLeading = t.leading; } catch (_) {}

        result.originalSize = originalSize;
        result.originalLeading = originalLeading;

        var size = originalSize;
        if (size < minPt) minPt = size;

        while (isOverset(tf) && size - stepPt >= minPt - 0.001) {
            size = Math.max(minPt, size - stepPt);
            try {
                t.pointSize = size;
                t.leading = size;
                result.changed = true;
            } catch (_) { break; }
            recompose(tf);
        }

        result.fixed = !isOverset(tf);
        try { result.finalSize = t.pointSize; } catch (_) { result.finalSize = size; }
        try { result.finalLeading = t.leading; } catch (_) { result.finalLeading = size; }
        return result;
    }

    if (app.documents.length === 0) {
        alert("QURBATA: tidak ada dokumen InDesign yang terbuka.");
        return;
    }

    var mode = (typeof QURBATA_MODE !== "undefined") ? String(QURBATA_MODE).toUpperCase() : "AUDIT";
    var outputDir = (typeof QURBATA_OUTPUT_DIR !== "undefined") ? String(QURBATA_OUTPUT_DIR) : "";
    var minPt = (typeof QURBATA_MIN_PT !== "undefined") ? Number(QURBATA_MIN_PT) : 28;
    var stepPt = (typeof QURBATA_STEP_PT !== "undefined") ? Number(QURBATA_STEP_PT) : 0.5;

    if (!minPt || minPt < 20) minPt = 28;
    if (!stepPt || stepPt <= 0) stepPt = 0.5;

    var scriptFile = File($.fileName);
    var toolsDir = scriptFile.parent;
    var repoRoot = toolsDir.parent;
    var distDir = outputDir ? Folder(outputDir) : Folder(repoRoot.fsName + "/dist/indesign-automation");
    ensureFolder(distDir);

    var doAutoFix = (mode === "AUTOFIX" || mode === "AUTOFIX_CLEANUP");
    var doCleanup = (mode === "CLEANUP" || mode === "AUDIT_CLEANUP" || mode === "AUTOFIX_CLEANUP");

    var doc = app.activeDocument;
    var frames = doc.textFrames;
    var oversetBefore = 0;
    var oversetAfter = [];
    var emptyFrames = [];
    var hiddenEmpty = 0;
    var fixedCount = 0;
    var unresolvedCount = 0;
    var fitRows = [];

    for (var i = 0; i < frames.length; i++) {
        var tf = frames[i];
        if (!tf.isValid) continue;

        var contents = "";
        try { contents = tf.contents; } catch (_) {}

        var isEmpty = trimText(contents) === "";
        if (isEmpty) {
            emptyFrames.push(tf);
            if (doCleanup) {
                try {
                    tf.strokeWeight = 0;
                    tf.fillColor = doc.swatches.itemByName("None");
                    hiddenEmpty++;
                } catch (_) {}
            }
        }

        var wasOverset = isOverset(tf);
        if (wasOverset) oversetBefore++;

        if (wasOverset && doAutoFix) {
            var beforeProps = getTextProps(tf);
            var fit = fitOversetFrame(tf, minPt, stepPt);
            if (fit.fixed) fixedCount++; else unresolvedCount++;
            fitRows.push([
                getPageName(tf), i + 1, safeText(contents),
                fit.originalSize, fit.finalSize,
                fit.originalLeading, fit.finalLeading,
                fit.fixed ? "FIXED" : "UNRESOLVED",
                safeText(beforeProps.paraStyle), safeText(beforeProps.objectStyle)
            ]);
        }

        if (isOverset(tf)) {
            var p = getTextProps(tf);
            oversetAfter.push([
                getPageName(tf), i + 1, safeText(contents), getBounds(tf),
                safeText(p.font), p.size, p.leading,
                safeText(p.paraStyle), safeText(p.objectStyle)
            ]);
        }
    }

    var auditLines = [];
    auditLines.push("Page\tFrameIndex\tContents\tGeometricBounds\tFont\tPointSize\tLeading\tParagraphStyle\tObjectStyle");
    for (var j = 0; j < oversetAfter.length; j++) auditLines.push(oversetAfter[j].join("\t"));

    var report = File(distDir.fsName + "/QURBATA-J1-OVERSET-AUDIT.tsv");
    writeUtf8(report, auditLines.join("\r\n"));

    var fitReport = File(distDir.fsName + "/QURBATA-J1-AUTOFIX-REPORT.tsv");
    if (doAutoFix) {
        var fitLines = [];
        fitLines.push("Page\tFrameIndex\tContents\tOriginalSize\tFinalSize\tOriginalLeading\tFinalLeading\tResult\tParagraphStyle\tObjectStyle");
        for (var k = 0; k < fitRows.length; k++) fitLines.push(fitRows[k].join("\t"));
        writeUtf8(fitReport, fitLines.join("\r\n"));
    }

    var summary = [];
    summary.push("Document=" + doc.name);
    summary.push("Pages=" + doc.pages.length);
    summary.push("TextFrames=" + frames.length);
    summary.push("OversetBefore=" + oversetBefore);
    summary.push("FixedOversetFrames=" + fixedCount);
    summary.push("UnresolvedOversetFrames=" + unresolvedCount);
    summary.push("OversetAfter=" + oversetAfter.length);
    summary.push("EmptyFrames=" + emptyFrames.length);
    summary.push("HiddenEmptyFrames=" + hiddenEmpty);
    summary.push("Mode=" + mode);
    summary.push("MinPointSize=" + minPt);
    summary.push("StepPointSize=" + stepPt);
    summary.push("AuditReport=" + report.fsName);
    if (doAutoFix) summary.push("AutoFixReport=" + fitReport.fsName);

    var summaryFile = File(distDir.fsName + "/QURBATA-J1-AUTOMATION-SUMMARY.txt");
    writeUtf8(summaryFile, summary.join("\r\n"));

    alert(
        "QURBATA InDesign automation selesai.\n\n" +
        "Pages: " + doc.pages.length + "\n" +
        "Overset before: " + oversetBefore + "\n" +
        "Fixed: " + fixedCount + "\n" +
        "Overset after: " + oversetAfter.length + "\n" +
        "Empty frames: " + emptyFrames.length + "\n" +
        "Hidden empty: " + hiddenEmpty + "\n" +
        "Mode: " + mode + "\n\n" +
        "Summary:\n" + summaryFile.fsName
    );
})();