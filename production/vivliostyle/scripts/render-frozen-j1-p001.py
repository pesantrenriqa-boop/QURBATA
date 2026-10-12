"""Frozen QURBATA J1 P001: approved A5 print layout, no rules/translations.
Arabic uses the KFGQPC Uthman Taha font from the repository.
For P002 onward, supply the approved 24-item exercise list from the page register.
"""
from pathlib import Path
from io import BytesIO
from PIL import Image,ImageDraw,ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from fontTools.ttLib import TTFont as FontToolsFont
import fitz,sys
ROOT=Path(__file__).resolve().parents[3]
FONT_DIR=ROOT/'production/vivliostyle/fonts'
FONT=FONT_DIR/'KFGQPC-Uthman-Taha-Naskh.ttf'
if not FONT.exists():
 f=FontToolsFont(str(FONT_DIR/'KFGQPC-Uthman-Taha-Naskh.woff2'));f.flavor=None;f.save(str(FONT))
OUT=ROOT/'production/vivliostyle/dist'
OUT.mkdir(parents=True,exist_ok=True)
PDF=OUT/'QURBATA-J1-P001-FROZEN.pdf'
PNG=OUT/'QURBATA-J1-P001-FROZEN.png'
W,H=419.53,595.28
c=canvas.Canvas(str(PDF),pagesize=(W,H),pageCompression=1)
c.setFillColor(HexColor('#FFFEFA'));c.rect(0,0,W,H,stroke=0,fill=1)
latin='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
latinbold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('Latin',latin))
pdfmetrics.registerFont(TTFont('LatinBold',latinbold))
ink=HexColor('#19352E');muted=HexColor('#69736C')
def text(t,x,top,sz=7,bold=False,col=ink):
 c.setFont('LatinBold' if bold else 'Latin',sz);c.setFillColor(col);c.drawString(x,H-top,t)
def arabic(s,cx,cy,size,individual=False,spacing=7):
 scale=4; font=ImageFont.truetype(str(FONT),round(size*scale))
 if individual:
  glyphs=[]
  for unit in s.split(' '):
   im=Image.new('RGBA',(int(size*scale*2.5),int(size*scale*2.5)),(0,0,0,0))
   ImageDraw.Draw(im).text((im.width/2,im.height/2),unit,font=font,anchor='mm',direction='rtl',fill='#19352E')
   glyphs.append(im.crop(im.getbbox()))
  gap=round(spacing*scale)
  total=sum(g.width for g in glyphs)+gap*(len(glyphs)-1)
  result=Image.new('RGBA',(total,max(g.height for g in glyphs)+20),(0,0,0,0));cursor=total
  for g in glyphs:
   cursor-=g.width;result.alpha_composite(g,(cursor,(result.height-g.height)//2));cursor-=gap
 else:
  bb=font.getbbox(s,direction='rtl')
  result=Image.new('RGBA',(max(1,bb[2]-bb[0]+30),max(1,bb[3]-bb[1]+30)),(0,0,0,0))
  ImageDraw.Draw(result).text((15-bb[0],15-bb[1]),s,font=font,direction='rtl',fill='#19352E')
  result=result.crop(result.getbbox())
 pw,ph=result.width/scale,result.height/scale
 c.drawImage(ImageReader(result),cx-pw/2,H-cy-ph/2,pw,ph,mask='auto')
text('QURBATA',29,27,11.5,True)
text('Quran  ·  Bahasa Arab  ·  Tahfidz  ·  Akhlak',29,39,5.7,False,muted)
text('01',382,28,9.5,True)
for x,ch in [(90,'ثَ'),(210,'تَ'),(329,'بَ')]:arabic(ch,x,91,43)
for x,t in [(24,'TAHFIDZ  ·  AN-NAS 1'),(156,'BAHASA ARAB  ·  SALAM'),(284,'AKHLAK  ·  HADIS SALAM')]:text(t,x,137,5.5,True,muted)
for x,t in [(85,'قُلْ أَعُوذُ بِرَبِّ النَّاسِ'),(210,'السَّلَامُ عَلَيْكُمْ'),(339,'أَفْشُوا السَّلَامَ بَيْنَكُمْ')]:arabic(t,x,160,12.5)
# P001 approved frozen print proof (24 groups); do not substitute older QJ1-P001 draft exercises.
D=['بَ تَ','بَ ثَ','تَ بَ','تَ ثَ','ثَ بَ','ثَ تَ','بَ تَ ثَ','بَ ثَ تَ','تَ بَ ثَ','تَ ثَ بَ','ثَ بَ تَ','ثَ تَ بَ','بَ بَ تَ','بَ بَ ثَ','تَ تَ بَ','تَ تَ ثَ','ثَ ثَ بَ','ثَ ثَ تَ','بَ تَ بَ','بَ ثَ بَ','تَ بَ تَ','تَ ثَ تَ','ثَ بَ ثَ','ثَ تَ ثَ']
assert len(D)==24
for row in range(8):
 for col in range(3):arabic(D[row*3+col],[82,210,338][col],205+row*42,29,True)
text('QJ1-P001',27,557,6,True,muted)
text('Tanggal: __________',112,557,6,False,muted)
text('Nilai: ______',255,557,6,False,muted)
text('Paraf: ______',332,557,6,False,muted)
arabic('تَعَلَّمْ  اِعْمَلْ  عَلِّمْ',210,575,12)
c.showPage();c.save()
doc=fitz.open(str(PDF))
assert len(doc)==1
doc[0].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(str(PNG))
print(PDF,PNG)
