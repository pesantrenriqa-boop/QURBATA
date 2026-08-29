#target "InDesign"

(function () {
    if (app.documents.length === 0) {
        alert("QURBATA: buka template 1 halaman terlebih dahulu.");
        return;
    }

    var doc = app.activeDocument;
    if (doc.pages.length !== 1) {
        alert("QURBATA: aktifkan TEMPLATE 1 HALAMAN, bukan dokumen merged. Pages sekarang: " + doc.pages.length);
        return;
    }

    function isEmptyFrame(tf) {
        try {
            var s = String(tf.contents).replace(/[\s\r\n]+/g, "");
            return s === "";
        } catch (_) { return false; }
    }

    function center(tf) {
        var g = tf.geometricBounds; // y1,x1,y2,x2
        return { x:(Number(g[1])+Number(g[3]))/2, y:(Number(g[0])+Number(g[2]))/2 };
    }

    // Find empty grid text frames only. Restrict to the main 4x8 grid by geometry:
    // derive candidates from empty frames and group by their y center.
    var frames = doc.pages[0].textFrames.everyItem().getElements();
    var empty = [];
    for (var i=0; i<frames.length; i++) {
        if (isEmptyFrame(frames[i])) {
            var c = center(frames[i]);
            // Exclude header/footer: grid is the middle of the page.
            var pg = doc.pages[0].bounds;
            var ph = Number(pg[2]) - Number(pg[0]);
            var py = Number(pg[0]);
            if (c.y > py + ph*0.15 && c.y < py + ph*0.88) {
                empty.push({tf:frames[i], x:c.x, y:c.y});
            }
        }
    }

    // Cluster into visual rows using y centers.
    empty.sort(function(a,b){ return a.y-b.y; });
    var rows = [];
    var tol = 4; // points
    for (var e=0; e<empty.length; e++) {
        var placed = false;
        for (var r=0; r<rows.length; r++) {
            if (Math.abs(rows[r].y-empty[e].y) <= tol) {
                rows[r].items.push(empty[e]);
                rows[r].y = (rows[r].y*(rows[r].items.length-1)+empty[e].y)/rows[r].items.length;
                placed=true; break;
            }
        }
        if (!placed) rows.push({y:empty[e].y,items:[empty[e]]});
    }

    // We only repair the two bottom grid rows that contain 3 empty frames each.
    var targets = [];
    for (var rr=0; rr<rows.length; rr++) {
        if (rows[rr].items.length === 3) targets.push(rows[rr]);
    }
    targets.sort(function(a,b){ return a.y-b.y; });

    if (targets.length < 2) {
        alert("QURBATA: tidak menemukan dua row dengan masing-masing 3 frame kosong. Tidak ada perubahan.");
        return;
    }

    // Use the last two such rows: Row07 and Row08.
    targets = targets.slice(targets.length-2);

    // In the template, Cell01 is the rightmost column; Cell04 is the leftmost.
    // The rightmost frame is already populated, so the three empty visual frames
    // from left->right correspond to Cell04, Cell03, Cell02.
    var names = [
        ["Row07Cell04","Row07Cell03","Row07Cell02"],
        ["Row08Cell04","Row08Cell03","Row08Cell02"]
    ];

    var changed = [];
    for (var tr=0; tr<2; tr++) {
        var items = targets[tr].items;
        items.sort(function(a,b){ return a.x-b.x; }); // left -> right
        if (items.length !== 3) continue;
        for (var j=0; j<3; j++) {
            var tf = items[j].tf;
            tf.contents = "<<" + names[tr][j] + ">>";
            changed.push(names[tr][j]);
        }
    }

    alert("QURBATA placeholder repair selesai.\n\nDipasang: " + changed.length +
          "\n" + changed.join("\n") +
          "\n\nSekarang Data Merge > Preview record 1.");
})();