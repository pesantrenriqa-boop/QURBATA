from PIL import Image, ImageDraw, ImageFont

W,H=1240,1754
bg=(255,255,255)
green=(18,65,52)
gold=(190,123,40)
gray=(92,92,92)
border=(219,214,201)
img=Image.new('RGB',(W,H),bg)
d=ImageDraw.Draw(img)

# Production dependencies
font_ar='KFGQPC Uthman Taha Naskh Regular.ttf'
font_reg='DejaVuSans.ttf'
font_bold='DejaVuSans-Bold.ttf'
logo_path='qurbata-logo.png'

def F(path,size): return ImageFont.truetype(path,size)

def txt(x,y,text,font,fill=green,anchor='la',direction=None,lang=None):
    kw={}
    if direction: kw['direction']=direction
    if lang: kw['language']=lang
    d.text((x,y),text,font=font,fill=fill,anchor=anchor,**kw)

def rounded(box,r=36,outline=border,width=2):
    d.rounded_rectangle(box,radius=r,fill=bg,outline=outline,width=width)

logo=Image.open(logo_path).convert('RGB')
logo.thumbnail((115,115), Image.Resampling.LANCZOS)
img.paste(logo,(84,24))

txt(240,66,'BAHASA ARAB QURBATA',F(font_bold,23),green,anchor='lm')
txt(1150,66,'JILID 1  |  03',F(font_reg,17),gray,anchor='rm')
d.line((84,145,1150,145),fill=border,width=2)

txt(88,220,'UNGKAPAN',F(font_bold,17),gold)
txt(88,278,'MENYAPA TEMAN',F(font_bold,40),green)
txt(88,325,'Dengarkan - tirukan - gunakan setelah salam dan tanya kabar',F(font_reg,18),gray)

rounded((88,385,1150,615),38)
txt(619,475,'يَا صَدِيقِي',F(font_ar,90),(12,65,48),anchor='mm',direction='rtl',lang='ar')
txt(619,570,'Yā ṣadīqī - wahai temanku',F(font_reg,26),gray,anchor='mm')

rounded((88,655,1150,885),38)
txt(619,745,'يَا صَدِيقَتِي',F(font_ar,90),(12,65,48),anchor='mm',direction='rtl',lang='ar')
txt(619,840,'Yā ṣadīqatī - wahai teman perempuanku',F(font_reg,26),gray,anchor='mm')

txt(88,955,'AYO GUNAKAN',F(font_bold,27),green)
txt(88,1000,'Mulai dengan salam, sapa temanmu, lalu tanyakan kabarnya.',F(font_reg,18),gray)
rounded((88,1045,1150,1205),35)
txt(619,1112,'السَّلَامُ عَلَيْكُمْ  -  يَا صَدِيقِي، كَيْفَ حَالُكَ؟',F(font_ar,47),(12,38,31),anchor='mm',direction='rtl',lang='ar')
txt(619,1171,'بِخَيْرٍ، الْحَمْدُ لِلّٰهِ',F(font_ar,43),(12,38,31),anchor='mm',direction='rtl',lang='ar')

txt(88,1280,'LATIHAN HARI INI',F(font_bold,25),green)
boxes=[(88,1325,430,1485),(449,1325,791,1485),(810,1325,1150,1485)]
heads=[('1.','DENGARKAN','Guru mengucapkan sapaan 3x.'),('2.','TIRUKAN','Ucapkan dengan jelas.'),('3.','GUNAKAN','Sapa teman lalu tanya kabar.')]
for box,(num,head,desc) in zip(boxes,heads):
    rounded(box,28)
    x1,y1,x2,y2=box
    txt(x1+28,y1+52,num,F(font_bold,16),gold)
    txt(x1+72,y1+52,head,F(font_bold,16),green)
    txt(x1+28,y1+112,desc,F(font_reg,14),gray)

d.line((88,1518,1150,1518),fill=border,width=2)
txt(88,1560,'TARGET',F(font_bold,17),gold)
txt(190,1560,'Mampu menyapa teman dan melanjutkan percakapan pendek secara spontan.',F(font_reg,16),(85,67,40))

img.save('BAHASA-ARAB-QURBATA-J1-P003-v1.2.png',quality=95)
img.save('BAHASA-ARAB-QURBATA-J1-P003-v1.2.pdf','PDF',resolution=150.0)
