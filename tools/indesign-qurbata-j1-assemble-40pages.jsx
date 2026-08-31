#target "InDesign"

(function () {
    if (app.documents.length === 0) {
        alert("QURBATA: tidak ada dokumen terbuka.");
        return;
    }

    var doc = app.activeDocument;

    if (doc.pages.length === 40) {
        alert("QURBATA: dokumen sudah 40 halaman. Tidak ada perubahan.");
        return;
    }

    if (doc.pages.length !== 36) {
        alert("QURBATA: assembly hanya dijalankan pada dokumen produksi Tartil 36 halaman. Pages sekarang: " + doc.pages.length);
        return;
    }

    var specials = [
        {
            page: 18,
            code: "QJ1-P018",
            title: "Hafalan 1",
            status: "Draf Terkendali — Terblokir Pemilihan Materi",
            body: "Materi peserta menunggu keputusan dan pengesahan.",
            note: "Hafalan adalah amanah yang dijaga dengan sabar, benar, dan rendah hati."
        },
        {
            page: 28,
            code: "QJ1-P028",
            title: "Bahasa Arab 1",
            status: "Draf Terkendali — Terblokir Pemilihan Materi",
            body: "Materi peserta menunggu keputusan dan pengesahan.",
            note: "Bahasa yang baik digunakan untuk memahami, menyapa, dan menghormati sesama."
        },
        {
            page: 36,
            code: "QJ1-P036",
            title: "Hafalan 2",
            status: "Draf Terkendali — Terblokir Pemilihan Materi",
            body: "Materi peserta menunggu keputusan dan pengesahan.",
            note: "Belajar dengan tenang, teliti, dan sungguh-sungguh."
        },
        {
            page: 38,
            code: "QJ1-P038",
            title: "Akhlak 1: Adab Belajar Al-Qur’an",
            status: "Draf Terkendali — Belum Siap Uji",
            body: "Materi peserta menunggu keputusan dan pengesahan.",
            note: "Belajar dengan tenang, teliti, dan sungguh-sungguh."
        }
    ];

    function addTextFrame(page, bounds, text, size, alignCenter, boldLike) {
        var tf = page.textFrames.add();
        tf.geometricBounds = bounds;
        tf.contents = text;
        try {
            tf.textFramePreferences.insetSpacing = [6, 6, 6, 6];
        } catch (_) {}
        try {
            tf.parentStory.texts[0].pointSize = size;
            tf.parentStory.texts[0].leading = size * 1.25;
            if (alignCenter) tf.parentStory.texts[0].justification = Justification.CENTER_ALIGN;
            if (boldLike) tf.parentStory.texts[0].tracking = 20;
        } catch (_) {}
        try {
            tf.strokeWeight = 0;
            tf.fillColor = doc.swatches.itemByName("None");
        } catch (_) {}
        return tf;
    }

    function addRule(page, y, x1, x2) {
        try {
            var ln = page.graphicLines.add();
            ln.geometricBounds = [y, x1, y, x2];
            ln.strokeWeight = 1;
            ln.strokeColor = doc.swatches.itemByName("Black");
        } catch (_) {}
    }

    function buildSpecialPage(page, spec) {
        var b = page.bounds; // y1 x1 y2 x2
        var y1 = Number(b[0]), x1 = Number(b[1]), y2 = Number(b[2]), x2 = Number(b[3]);
        var h = y2 - y1, w = x2 - x1;

        addTextFrame(
            page,
            [y1 + h*0.05, x1 + w*0.08, y1 + h*0.105, x2 - w*0.08],
            "QURBATA JILID 1  •  " + spec.code,
            11,
            true,
            false
        );

        addRule(page, y1 + h*0.125, x1 + w*0.08, x2 - w*0.08);

        addTextFrame(
            page,
            [y1 + h*0.18, x1 + w*0.10, y1 + h*0.31, x2 - w*0.10],
            spec.title,
            28,
            true,
            true
        );

        addTextFrame(
            page,
            [y1 + h*0.36, x1 + w*0.13, y1 + h*0.43, x2 - w*0.13],
            "HALAMAN KHUSUS",
            12,
            true,
            false
        );

        var body = addTextFrame(
            page,
            [y1 + h*0.47, x1 + w*0.12, y1 + h*0.64, x2 - w*0.12],
            spec.body + "\r\r" + spec.status,
            14,
            true,
            false
        );
        try {
            body.strokeWeight = 0.75;
            body.strokeColor = doc.swatches.itemByName("Black");
        } catch (_) {}

        addTextFrame(
            page,
            [y1 + h*0.70, x1 + w*0.12, y1 + h*0.80, x2 - w*0.12],
            spec.note,
            12,
            true,
            false
        );

        addRule(page, y1 + h*0.86, x1 + w*0.08, x2 - w*0.08);

        addTextFrame(
            page,
            [y1 + h*0.885, x1 + w*0.08, y1 + h*0.94, x2 - w*0.08],
            "QURBATA • JILID 1 • " + spec.page,
            10,
            true,
            false
        );
    }

    // Insert in ascending target-page order so positions remain the final book positions.
    for (var i = 0; i < specials.length; i++) {
        var spec = specials[i];
        var insertBeforeIndex = spec.page - 1; // zero-based
        var newPage;
        if (insertBeforeIndex < doc.pages.length) {
            newPage = doc.pages.add(LocationOptions.BEFORE, doc.pages.item(insertBeforeIndex));
        } else {
            newPage = doc.pages.add(LocationOptions.AT_END);
        }
        buildSpecialPage(newPage, spec);
    }

    // Rename page labels 1..40 for a clean final sequence.
    try {
        doc.sections.everyItem().remove();
    } catch (_) {}
    try {
        var sec = doc.sections.add(doc.pages[0]);
        sec.continueNumbering = false;
        sec.pageNumberStart = 1;
        sec.pageNumberStyle = PageNumberStyle.ARABIC;
    } catch (_) {}

    alert(
        "QURBATA Jilid 1 assembly selesai.\n\n" +
        "Pages: " + doc.pages.length + "\n" +
        "Inserted: P018, P028, P036, P038\n\n" +
        "Empat halaman khusus masih berstatus DRAFT CONTROLLED.\n" +
        "Jangan dianggap materi final sebelum mapping Tahfidz/BA/Akhlak disahkan."
    );
})();