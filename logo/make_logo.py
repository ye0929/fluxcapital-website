from fontTools.ttLib import TTFont, TTCollection
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import cairosvg, os
G,N,W="#d4a84a","#0b1426","#e6ebf5"
inter=instancer.instantiateVariableFont(TTFont("/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"),{"wght":650,"opsz":32})
cjk=TTCollection("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc").fonts[2]  # SC
def text(font,s,x,y,size,track=0):
    gs=font.getGlyphSet(); cmap=font.getBestCmap(); upm=font['head'].unitsPerEm; sc=size/upm
    pen=SVGPathPen(gs); cx=x
    for ch in s:
        gn=cmap[ord(ch)]
        gs[gn].draw(TransformPen(pen,(sc,0,0,-sc,cx,y)))
        cx+=gs[gn].width*sc+track
    return pen.getCommands(), cx-track
import math
def arrow(x0,y0,x1,y1,w0,w1,hl,hw):
    dx,dy=x1-x0,y1-y0;L=math.hypot(dx,dy);ux,uy=dx/L,dy/L;nx,ny=-uy,ux
    bx,by=x1-ux*hl,y1-uy*hl
    P=[(x0+nx*w0/2,y0+ny*w0/2),(bx+nx*w1/2,by+ny*w1/2),(bx+nx*hw/2,by+ny*hw/2),(x1,y1),(bx-nx*hw/2,by-ny*hw/2),(bx-nx*w1/2,by-ny*w1/2),(x0-nx*w0/2,y0-ny*w0/2)]
    return "M"+" L".join(f"{a:.2f} {b:.2f}" for a,b in P)+" Z"
UPA=arrow(12.1,57,30.4,5,5.5,5.5,10,14)
TOP="M21 17.5 C29 14.5 37 20.5 45 17.5 C48 16.4 51 16.4 53 17.5"
BOT="M15 34.5 C23 31.5 31 37.5 39 34.5 C42 33.4 45 33.4 47 34.5"
PAPER="M21 17.5 C29 14.5 37 20.5 45 17.5 C48 16.4 51 16.4 53 17.5 L47 34.5 C45 33.4 42 33.4 39 34.5 C31 37.5 23 31.5 15 34.5 Z"
SIDE="#2c4170"
def mark(c,bg=None,r=14):
    b=f'<rect width="64" height="64" rx="{r}" fill="{bg}"/>' if bg else ''
    k=(c+(bg or "t")).replace("#","")
    defs=f'<defs><linearGradient id="g{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c}" stop-opacity="0.55"/><stop offset="1" stop-color="{SIDE}" stop-opacity="0.95"/></linearGradient><clipPath id="a{k}"><rect x="0" y="0" width="64" height="37.5"/></clipPath><clipPath id="p{k}"><path d="{PAPER}"/></clipPath></defs>'
    import math
    PTS=[(2,56),(8,46),(11,52.5),(29,23)];WS=[0,2.6,6,2.1]
    def off(sg):
        L=[]
        for i in range(3):
            (x0,y0),(x1,y1)=PTS[i],PTS[i+1];m=math.hypot(x1-x0,y1-y0);nx,ny=-(y1-y0)/m,(x1-x0)/m
            L.append(((x0+sg*nx*WS[i]/2,y0+sg*ny*WS[i]/2),(x1+sg*nx*WS[i+1]/2,y1+sg*ny*WS[i+1]/2)))
        out=[L[0][0]]
        for i in range(2):
            (p1,p2),(p3,p4)=L[i],L[i+1]
            d=(p1[0]-p2[0])*(p3[1]-p4[1])-(p1[1]-p2[1])*(p3[0]-p4[0])
            t=((p1[0]-p3[0])*(p3[1]-p4[1])-(p1[1]-p3[1])*(p3[0]-p4[0]))/d
            out.append((p1[0]+t*(p2[0]-p1[0]),p1[1]+t*(p2[1]-p1[1])))
        out.append(L[2][1]);return out
    pl=off(1);pr=off(-1)
    BODY="M"+" L".join(f"{x:.2f} {y:.2f}" for x,y in pl+pr[::-1])+" Z";joints=''
    bz=lambda t:PTS[-1]
    ex,ey=bz(1);ux,uy=18/math.hypot(18,29.5),-29.5/math.hypot(18,29.5)
    T=(ex+ux*6.5,ey+uy*6.5);nx,ny=-uy,ux
    B1=(ex-ux*1.8+nx*4.6,ey-uy*1.8+ny*4.6);B2=(ex-ux*1.8-nx*4.6,ey-uy*1.8-ny*4.6);K=(ex+ux*0.9,ey+uy*0.9)
    HD="M"+" L".join(f"{a:.2f} {b:.2f}" for a,b in (T,B1,K,B2))+" Z"

    up=joints+f'<path d="{BODY}" fill="{c}"/><path d="{HD}" fill="{c}" stroke="{c}" stroke-width="0.6" stroke-linejoin="miter"/>'
    sheet=f'<path d="{PAPER}" fill="{N}" fill-opacity="0.45"/><path d="{PAPER}" fill="url(#g{k})"/>'
    def edge(d):
        return f'<g clip-path="url(#p{k})">'+''.join(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-opacity="{o}"/>' for w,o in [(12-i*1.1,0.09+0.006*i*i) for i in range(10)])+'</g>'
    far=edge(TOP); near=edge(BOT)
    # arrow below pierce point is under the sheet; above it emerges over sheet and far edge
    fm=f'<defs><linearGradient id="fg{k}" gradientUnits="userSpaceOnUse" x1="9" y1="0" x2="49" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.275" stop-color="#fff"/><stop offset="0.72" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><mask id="m{k}"><rect width="64" height="64" fill="url(#fg{k})"/></mask></defs>'
    return b+'<g transform="translate(0,7.04) scale(1,0.78)">'+defs+fm+up+f'<g mask="url(#m{k})"><g transform="translate(-5,12)">'+sheet+far+'</g></g>'+f'<g clip-path="url(#a{k})">{up}</g>'+f'<g mask="url(#m{k})"><g transform="translate(-5,12)">'+near+'</g></g></g>'
out="/home/box/fluxcapital-website/logo/"
def save(n,s): open(out+n,"w").write(s)
save("logo-mark.svg",f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{mark(G,N)}</svg>')
save("logo-mark-transparent.svg",f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{mark(G)}</svg>')
open("/home/box/fluxcapital-website/favicon.svg","w").write(open(out+"logo-mark.svg").read())
def horiz(markc,txt,sub,bg=None):
    H=120; p1,e1=text(inter,"FLUX CAPITAL",120,58,40,3); p2,e2=text(inter,"LTD",e1+12,58,20,2)
    p3,e3=text(cjk,"通量资本",121,100,28,14)
    Wd=int(max(e2,e3)+24)
    b=f'<rect width="{Wd}" height="{H}" fill="{bg}"/>' if bg else ''
    return Wd,H,f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {Wd} {H}" width="{Wd}" height="{H}">{b}<g transform="translate(12,12) scale(1.5)">{mark(markc)}</g><g transform="translate(0,6.96) scale(1,0.88)"><path d="{p1}" fill="{txt}"/><path d="{p2}" fill="{sub}"/></g><path d="{p3}" fill="{sub}"/></svg>'
for n,a in [("logo.svg",(G,W,G)),("logo-dark-bg.svg",(G,W,G,N)),("logo-light.svg",(N,N,"#9a7a2e"))]:
    save(n,horiz(*a)[2])
for s in [64,128,256,512,1024]: cairosvg.svg2png(url=out+"logo-mark.svg",write_to=out+f"logo-mark-{s}.png",output_width=s,output_height=s)
for w in [600,1200]:
    cairosvg.svg2png(url=out+"logo.svg",write_to=out+f"logo-{w}.png",output_width=w)
    cairosvg.svg2png(url=out+"logo-dark-bg.svg",write_to=out+f"logo-dark-bg-{w}.png",output_width=w)
for z in [16,32,64,256]: cairosvg.svg2png(url=out+"logo-mark.svg",write_to=f"/tmp/lg/c{z}.png",output_width=z)
from PIL import Image
im=Image.new("RGB",(1250,560),"#ffffff");x=10
for z in [16,32,64,256]:
    t=Image.open(f"/tmp/lg/c{z}.png");im.paste(t,(x,10),t);x+=z+20
for i,n in enumerate(["logo-1200.png","logo-dark-bg-600.png"]):
    t=Image.open(out+n).convert("RGBA");im.paste(t,(10 if i==0 else 640,290),t)
im.save("/tmp/lg/chk.png")
