from pathlib import Path
from hb_svg import paths
base=Path('/mnt/data')
phrases=[
('trace1','السَّلَامُ عَلَيْكُمْ'),
('trace2','وَعَلَيْكُمُ السَّلَامُ'),
('trace3','يَا صَدِيقِي، كَيْفَ حَالُكَ؟'),
('trace4','بِخَيْرٍ، الْحَمْدُ لِلّٰهِ')]
for name,text in phrases:
    ps,total=paths(text)
    s=600/total
    parts=[f"<svg xmlns='http://www.w3.org/2000/svg' width='640' height='72' viewBox='0 0 640 72'>",f"<g transform='translate(620,62) scale({-s},{-s})'>"]
    for d in ps:
        parts.append(f"<path d='{d}' fill='none' stroke='#686868' stroke-width='30' stroke-dasharray='30 85' stroke-linecap='round' stroke-linejoin='round'/>")
    parts.append('</g></svg>')
    (base/f'{name}_v.svg').write_text(''.join(parts),encoding='utf-8')

html=f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><style>
@font-face{{font-family:Uthman;src:url('file:///home/oai/.local/share/fonts/KFGQPC%20Uthman%20Taha%20Naskh%20Regular.ttf')}}
@page{{size:A4;margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;font-family:Arial,sans-serif;color:#222}}.page{{width:210mm;height:297mm;padding:14mm 15mm 11mm;position:relative}}.green{{color:#2d6a4f}}.head{{display:flex;justify-content:space-between;font-weight:700;font-size:10pt;border-bottom:1px solid #ddd;padding-bottom:4mm}}.label{{font-size:9pt;font-weight:700;margin-top:7mm}}.title{{font-size:20pt;font-weight:700;margin-top:1mm}}.sub{{font-size:9pt;color:#666;margin-top:1.5mm}}.card{{border:1px solid #ddd;border-radius:4mm;margin-top:7mm;height:42mm;display:flex;flex-direction:column;justify-content:center;align-items:center}}.arab-main{{font-family:Uthman;font-size:48pt;line-height:1;direction:rtl;color:#2d6a4f}}.indo-main{{font-size:17pt;font-weight:700;color:#555;margin-top:3mm}}.section{{margin-top:8mm}}.section h3{{margin:0 0 3mm;font-size:9pt;color:#2d6a4f}}.rows{{font-size:11pt;line-height:1.9}}.inline{{display:inline-block;font-family:Uthman;font-size:28pt;direction:rtl;vertical-align:-6px;margin:0 2mm}}.practice{{display:grid;grid-template-columns:1fr 1fr;gap:12mm;font-size:10pt}}.practice b{{font-size:10pt}}.inline2{{display:inline-block;font-family:Uthman;font-size:32pt;direction:rtl;vertical-align:-8px;margin-left:2mm}}.write-title{{display:flex;align-items:center;gap:5mm;margin-top:8mm;color:#2d6a4f;font-weight:700;font-size:10pt}}.write-title:before,.write-title:after{{content:'';height:1px;background:#2d6a4f;flex:1}}.hint{{font-size:8.5pt;color:#666;margin-top:2mm}}.trace{{height:16mm;border-bottom:1px solid #ddd;display:flex;align-items:center}}.trace img{{width:100%;height:15mm;object-fit:contain}}.footer{{position:absolute;left:15mm;right:15mm;bottom:7mm;border-top:1px solid #ddd;padding-top:2mm;font-size:7.5pt;color:#666}}
</style></head><body><div class="page"><div class="head"><span>BAHASA ARAB QURBATA JILID 1</span><span class="green">04</span></div><div class="label green">UNGKAPAN</div><div class="title">DENGARKAN</div><div class="sub">Dengarkan - tirukan - lakukan saat guru memberi instruksi</div><div class="card"><div class="arab-main">اِسْمَعْ</div><div class="indo-main">Dengarkan</div></div><div class="section"><h3>AYO GUNAKAN</h3><div class="rows"><div>1. Mulai dengan salam.</div><div>2. Tanyakan kabar teman.</div><div>3. Sapa teman dengan sopan.</div><div>4. Saat guru berkata <span class="inline">اِسْمَعْ</span>, dengarkan dengan baik.</div></div></div><div class="section"><h3>LATIHAN HARI INI</h3><div class="practice"><div><b>1. DENGARKAN</b><br><span>Guru mengucapkan 3x.</span></div><div><b>2. TIRUKAN</b><br><span>Ucapkan <span class="inline2">اِسْمَعْ</span></span></div></div></div><div class="write-title">AYO MENULIS</div><div class="hint">Tebalkan titik-titik dari kanan ke kiri.</div><div class="trace"><img src="file:///mnt/data/trace1_v.svg"></div><div class="trace"><img src="file:///mnt/data/trace2_v.svg"></div><div class="trace"><img src="file:///mnt/data/trace3_v.svg"></div><div class="trace"><img src="file:///mnt/data/trace4_v.svg"></div><div class="footer">QURBATA - Bahasa Arab komunikatif, ringan, dan kumulatif</div></div></body></html>'''
(base/'p004_v13.html').write_text(html,encoding='utf-8')
