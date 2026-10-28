from PIL import Image, ImageDraw, ImageFont
import math, random
random.seed(10)
w,h=1200,630
im=Image.new('RGB',(w,h)); pix=im.load()
for y in range(h):
 for x in range(w):
  d=max(0,1-math.sqrt(((x-600)/800)**2+((y-280)/500)**2)); pix[x,y]=(int(29+65*d),int(6+15*d),int(12+23*d))
d=ImageDraw.Draw(im); gold='#e5c982'; muted='#c8aa70'
d.rectangle((25,25,1175,605),outline=gold,width=2); d.rectangle((36,36,1164,594),outline='#977b49',width=1)
for x in [55,1145]:
 for y in [55,575]:
  d.ellipse((x-4,y-4,x+4,y+4),fill=gold)
for i in range(50):
 x=random.choice([random.randint(45,230),random.randint(970,1155)]); y=random.randint(50,580);r=random.choice([1,2,3]);d.ellipse((x-r,y-r,x+r,y+r),fill=random.choice(['#957340','#b18a51','#d9b775']))
serif='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'; italic='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'; sans='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def text(y,t,font,size,color=gold):
 f=ImageFont.truetype(font,size); box=d.textbbox((0,0),t,font=f);d.text(((w-(box[2]-box[0]))/2,y),t,font=f,fill=color)
text(105,'TOGETHER WITH THEIR FAMILIES',sans,20,muted)
text(176,'You are invited',italic,75,'#f4dfa5')
d.line((465,290,735,290),fill=muted,width=1)
text(320,'The Wedding of Major Yasir Raza',serif,35,'#f7e8c7')
text(400,'NOVEMBER 2026  ·  RAWALPINDI',sans,20,muted)
text(500,'TAP TO OPEN YOUR INVITATION',sans,17,gold)
im.save('/home/user/invite-preview/preview.jpg',quality=90)
