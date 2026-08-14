import ctypes
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform
FONT='/home/oai/.local/share/fonts/KFGQPC Uthman Taha Naskh Regular.ttf'
lib=ctypes.CDLL('/lib/x86_64-linux-gnu/libharfbuzz.so.0')
hb_blob_p=ctypes.c_void_p; hb_face_p=ctypes.c_void_p; hb_font_p=ctypes.c_void_p; hb_buffer_p=ctypes.c_void_p
lib.hb_blob_create.argtypes=[ctypes.c_char_p,ctypes.c_uint,ctypes.c_int,ctypes.c_void_p,ctypes.c_void_p]; lib.hb_blob_create.restype=hb_blob_p
lib.hb_face_create.argtypes=[hb_blob_p,ctypes.c_uint]; lib.hb_face_create.restype=hb_face_p
lib.hb_font_create.argtypes=[hb_face_p]; lib.hb_font_create.restype=hb_font_p
lib.hb_ot_font_set_funcs.argtypes=[hb_font_p]
lib.hb_face_get_upem.argtypes=[hb_face_p]; lib.hb_face_get_upem.restype=ctypes.c_uint
lib.hb_font_set_scale.argtypes=[hb_font_p,ctypes.c_int,ctypes.c_int]
lib.hb_buffer_create.restype=hb_buffer_p
lib.hb_buffer_add_utf8.argtypes=[hb_buffer_p,ctypes.c_char_p,ctypes.c_int,ctypes.c_uint,ctypes.c_int]
lib.hb_buffer_guess_segment_properties.argtypes=[hb_buffer_p]
lib.hb_shape.argtypes=[hb_font_p,hb_buffer_p,ctypes.c_void_p,ctypes.c_uint]
class Info(ctypes.Structure): _fields_=[('codepoint',ctypes.c_uint32),('mask',ctypes.c_uint32),('cluster',ctypes.c_uint32),('var1',ctypes.c_uint32),('var2',ctypes.c_uint32)]
class Pos(ctypes.Structure): _fields_=[('x_advance',ctypes.c_int32),('y_advance',ctypes.c_int32),('x_offset',ctypes.c_int32),('y_offset',ctypes.c_int32),('var',ctypes.c_uint32)]
lib.hb_buffer_get_length.argtypes=[hb_buffer_p]; lib.hb_buffer_get_length.restype=ctypes.c_uint
lib.hb_buffer_get_glyph_infos.argtypes=[hb_buffer_p,ctypes.POINTER(ctypes.c_uint)]; lib.hb_buffer_get_glyph_infos.restype=ctypes.POINTER(Info)
lib.hb_buffer_get_glyph_positions.argtypes=[hb_buffer_p,ctypes.POINTER(ctypes.c_uint)]; lib.hb_buffer_get_glyph_positions.restype=ctypes.POINTER(Pos)
_data=open(FONT,'rb').read(); _mem=ctypes.create_string_buffer(_data); blob=lib.hb_blob_create(_mem,len(_data),2,None,None); face=lib.hb_face_create(blob,0); hbfont=lib.hb_font_create(face); lib.hb_ot_font_set_funcs(hbfont); upem=lib.hb_face_get_upem(face); lib.hb_font_set_scale(hbfont,upem,upem)
ttf=TTFont(FONT); glyphset=ttf.getGlyphSet(); order=ttf.getGlyphOrder()
def paths(text):
 b=lib.hb_buffer_create(); raw=text.encode(); lib.hb_buffer_add_utf8(b,raw,len(raw),0,len(raw)); lib.hb_buffer_guess_segment_properties(b); lib.hb_shape(hbfont,b,None,0)
 n=lib.hb_buffer_get_length(b); infos=lib.hb_buffer_get_glyph_infos(b,None); pos=lib.hb_buffer_get_glyph_positions(b,None)
 total=sum(pos[i].x_advance for i in range(n)); cum=0; out=[]
 for i in range(n):
  gid=infos[i].codepoint; adv=pos[i].x_advance; x=total-cum-adv+pos[i].x_offset; y=pos[i].y_offset
  pen=SVGPathPen(glyphset); tpen=TransformPen(pen,Transform(1,0,0,1,x,y)); glyphset[order[gid]].draw(tpen); d=pen.getCommands()
  if d: out.append(d)
  cum+=adv
 return out,total
