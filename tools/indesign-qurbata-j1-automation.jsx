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

    function readCommand(file) {
        var cfg = { mode: "AUDIT" };
        if (!file.exists) return cfg;
        file.encoding = "UTF-8";
        if (!file.open("r")) return cfg;
        while (!file.eof) {
            var line = file.readln();
            var p = line.indexOf("=");
            if (p > 0) {
                var k = trimText(line.substring(0, p)).toUpperCase();
                var v = trimText(line.substring(p + 1));
                cfg[k.toLowerCase()] = v;
            }
        }
        file.close();
        return cfg;
    }

    function getPageName(tf) {
        try {
            if (tf.parentPage) return tf.parentPage.name;
        } catch (_) {}
        return "";
    }

    function getBounds(tf) {
        try {
            var g = tf.geometricBounds;
            return [g[0], g[1], g[2], g[3]].join("|");
        } catch (_) {
            return "";
        }
    }

    function getTextProps(tf) {
        var out = {
            font: "",
            size: "",
            leading: "",
            paraStyle: "",
            objectStyle: ""
        };
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

    if (app.documents.length === 0) {
        alert("QURBATA: tidak ada dokumen InDesign yang terbuka.");
        return;
    }

    var scriptFile = File($.fileName);
    var toolsDir = scriptFile.parent;
    var repoRoot = toolsDir.parent;
    var distDir = Folder(repoRoot.fsName + "/dist/indesign-automation");
    ensureFolder(distDir);

    var cmdFile = File(distDir.fsName + "/QURBATA-INDESIGN-COMMAND.txt");
    var cfg = readCommand(cmdFile);
    var mode = (cfg.mode || "AUDIT").toUpperCase();

    var doc = app.activeDocument;
    var frames = doc.textFrames;
    var overset = [];
    var emptyFrames = [];
    var hiddenEmpty = 0;

    for (var i = 0; i < frames.length; i++) {
        var tf = frames[i];
        if (!tf.isValid) continue;

        var contents = "";
        try { contents = tf.contents; } catch (_) {}

        var isEmpty = trimText(contents) === "";
        if (isEmpty) {
            emptyFrames.push(tf);
            if (mode === "CLEANUP" || mode === "AUDIT_CLEANUP") {
                try {
                    tf.strokeWeight = 0;
                    tf.fillColor = doc.swatches.itemByName("None");
                    hiddenEmpty++;
                } catch (_) {}
            }
        }

        var isOverset = false;
        try { isOverset = tf.overflows === true; } catch (_) {}
        if (isOverset) {
            var p = getTextProps(tf);
            overset.push([
                getPageName(tf),
                i + 1,
                safeText(contents),
                getBounds(tf),
                safeText(p.font),
                p.size,
                p.leading,
                safeText(p.paraStyle),
                safeText(p.objectStyle)
            ]);
        }
    }

    var lines = [];
    lines.push("Page\tFrameIndex\tContents\tGeometricBounds\tFont\tPointSize\tLeading\tParagraphStyle\tObjectStyle");
    for (var j = 0; j < overset.length; j++) {
        lines.push(overset[j].join("\t"));
    }

    var report = File(distDir.fsName + "/QURBATA-J1-OVERSET-AUDIT.tsv");
    writeUtf8(report, lines.join("\r\n"));

    var summary = [];
    summary.push("Document=" + doc.name);
    summary.push("Pages=" + doc.pages.length);
    summary.push("TextFrames=" + frames.length);
    summary.push("OversetFrames=" + overset.length);
    summary.push("EmptyFrames=" + emptyFrames.length);
    summary.push("HiddenEmptyFrames=" + hiddenEmpty);
    summary.push("Mode=" + mode);
    summary.push("Report=" + report.fsName);

    var summaryFile = File(distDir.fsName + "/QURBATA-J1-AUTOMATION-SUMMARY.txt");
    writeUtf8(summaryFile, summary.join("\r\n"));

    alert(
        "QURBATA InDesign automation selesai.\n\n" +
        "Pages: " + doc.pages.length + "\n" +
        "Overset: " + overset.length + "\n" +
        "Empty frames: " + emptyFrames.length + "\n" +
        "Hidden empty: " + hiddenEmpty + "\n\n" +
        "Report:\n" + report.fsName
    );
})();
