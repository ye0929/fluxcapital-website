src=open("make_logo.py").read(); exec(src[:src.index('out="/home')])
import cairosvg,io
from PIL import Image
im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=f'<svg xmlns="http://www.w3.org/2000/svg" width="640" height="640" viewBox="0 0 64 64">{mark(G)}</svg>'.encode())))
bx=[v/10 for v in im.getchannel("A").point(lambda a:255 if a>20 else 0).getbbox()]
def stacked(fn,ms,ts,gap):
    C=1080
    p1,e1=text(inter,"FLUX CAPITAL",0,0,40,3); p2,e2=text(inter,"LTD",e1+12,0,20,2)
    p3,e3=text(cjk,"通量资本",0,0,28,14)
    mw,mh=(bx[2]-bx[0])*ms,(bx[3]-bx[1])*ms
    capH=29*0.88*ts; th=capH+16*ts+28*ts
    tot=mh+gap+th; y0=(C-tot)/2
    mx=(C-mw)/2-bx[0]*ms; my=y0-bx[1]*ms
    ty=y0+mh+gap+capH
    tx=(C-e2*ts)/2; cx=(C-e3*ts)/2; cy=ty+16*ts+28*ts*0.86
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{C}" height="{C}"><rect width="{C}" height="{C}" fill="{N}"/><g transform="translate({mx},{my}) scale({ms})">{mark(G)}</g><g transform="translate({tx},{ty}) scale({ts},{ts*0.88})"><path d="{p1}" fill="{W}"/><path d="{p2}" fill="{G}"/></g><g transform="translate({cx},{cy}) scale({ts})"><path d="{p3}" fill="{G}"/></g></svg>'
    cairosvg.svg2png(bytestring=svg.encode(),write_to=fn)
stacked("logo-mark-square-1080-stacked.png",11.5,2.0,170)
stacked("logo-stacked-1080.png",9,1.6,140)
