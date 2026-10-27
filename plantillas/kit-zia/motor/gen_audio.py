# Musica original + efectos hechos en codigo, armados alrededor de la voz de Zia. Uso: python3 gen_audio.py (desde audio/), luego zsh master.sh.
# Corresponde a plantilla/index.html (17 s). En cada video nuevo cambia: DUR (duracion total), END (cuando empieza la firma), las secciones de musica y la lista C de efectos (un efecto en cada movimiento).
import numpy as np, wave, subprocess, json, os
SR=48000; DUR=17.0; N=int(SR*DUR); VO_OFF=0.4
HERE=os.path.dirname(os.path.abspath(__file__)); rng=np.random.default_rng(7)
def t(n): return np.arange(n)/SR
def read_wav(p):
    tmp=HERE+'/_tmp.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-i',p,'-ac','1','-ar',str(SR),'-c:a','pcm_s16le',tmp],check=True)
    w=wave.open(tmp); x=np.frombuffer(w.readframes(w.getnframes()),np.int16)/32768.0; return x
def write_wav(p,x,ch=1):
    x=np.clip(x,-1,1); w=wave.open(p,'w'); w.setnchannels(ch); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
def lp(x,fc):  # one-pole lowpass
    a=np.exp(-2*np.pi*fc/SR); y=np.empty_like(x); s=0.0
    for i in range(len(x)): s=(1-a)*x[i]+a*s; y[i]=s
    return y
def lp_fast(x,fc):
    X=np.fft.rfft(x); f=np.fft.rfftfreq(len(x),1/SR); X/= (1+(f/fc)**4); return np.fft.irfft(X,len(x))
def hp_fast(x,fc):
    X=np.fft.rfft(x); f=np.fft.rfftfreq(len(x),1/SR); X*= 1/(1+(fc/np.maximum(f,1))**4); return np.fft.irfft(X,len(x))
def bp_fast(x,lo,hi): return hp_fast(lp_fast(x,hi),lo)
def env(n,a,r,shape=4):
    e=np.ones(n); na=max(1,int(a*SR)); e[:na]=np.linspace(0,1,na)
    tt=np.arange(n-na)/SR; e[na:]=np.exp(-tt*shape/max(r,1e-3)); return e
def add(buf,x,at,g=1.0):
    i=int(at*SR); j=min(len(buf),i+len(x)); buf[i:j]+=x[:j-i]*g
def db(v): return 10**(v/20)
NOTE=lambda m:440*2**((m-69)/12)

# ---------- MUSICA: 118 bpm, Re mayor, alegre. Intro suave, progresion completa desde "increible", acorde final bajo la firma
BPM=118; beat=60/BPM; bar=4*beat
music=np.zeros(N)
def pad(notes,dur,bright=1.0):
    n=int(dur*SR); tt=t(n); s=np.zeros(n)
    for m in notes:
        for det in (-0.08,0.08):
            f=NOTE(m)*2**(det/12); s+=np.sin(2*np.pi*f*tt)+0.35*bright*np.sin(2*np.pi*2*f*tt)+0.12*bright*np.sin(2*np.pi*3*f*tt)
    s*=np.minimum(1,np.minimum(tt/0.3,(dur-tt)/0.3)).clip(0,1)
    return s/len(notes)
def pluck(m,dur=0.5):
    n=int(dur*SR); tt=t(n); f=NOTE(m)
    s=np.sin(2*np.pi*f*tt)+0.6*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*12)+0.25*np.sin(2*np.pi*4*f*tt)*np.exp(-tt*20)
    return s*env(n,0.003,dur,6)
def kick(dur=0.4):
    n=int(dur*SR); tt=t(n); f=46+110*np.exp(-tt*30); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*env(n,0.002,dur,6)
def hat(): n=int(0.05*SR); return hp_fast(rng.standard_normal(n),7000)*env(n,0.001,0.04,8)
def clap(): n=int(0.18*SR); x=bp_fast(rng.standard_normal(n),900,5000); tt=t(n); e=np.exp(-tt*28)+0.6*np.exp(-np.maximum(tt-0.012,0)*30)*(tt>0.012); return x*e/np.max(np.abs(x))
def sub(m,dur):
    n=int(dur*SR); tt=t(n); return np.sin(2*np.pi*NOTE(m)*tt)*np.minimum(1,np.minimum(tt/0.02,(dur-tt)/0.05)).clip(0,1)
prog=[[62,66,69,74],[59,62,66,71],[55,59,62,67],[57,61,64,69]]   # D Bm G A
bass=[38,35,43,45]
END=13.4
# A) 0-7,1: pad + plucks ligeros + hat, sin bombo fuerte (la voz saluda)
b=0
while b*bar/2<7.1:
    th=b*bar/2; ch=prog[b%4]; d=min(bar/2,7.1-th)
    add(music,pad(ch,d+0.2,0.6),th,0.12)
    for kk in range(4):
        tk=th+kk*beat/2
        if tk<7.1: add(music,pluck(ch[[0,2,1,3][kk]]+12,0.35),tk,0.05)
    b+=1
for q in range(int(7.1/(beat/2))):
    tq=q*beat/2
    if tq>0.4: add(music,hat(),tq,0.035 if q%2 else 0.05)
for q in range(int(7.1/beat)):
    tq=q*beat
    if tq>=0.4 and q%2==0: add(music,kick(0.3),tq,0.10)
# riser hacia "increible"
n=int(1.3*SR); tt=t(n); rs=bp_fast(rng.standard_normal(n),600,7000)*(tt/1.3)**2; add(music,rs/np.max(np.abs(rs)),5.85,0.08)
# B) 7,16-13,4: progresion completa, bombo en negras, palmas en 2 y 4
start=7.16; b=0
while start+b*bar/2<END:
    th=start+b*bar/2; ch=prog[b%4]; d=min(bar/2,END-th)
    add(music,pad(ch,d+0.25,1.0),th,0.13); add(music,sub(bass[b%4],d),th,0.20)
    for kk in range(4):
        tk=th+kk*beat/2
        if tk<END: add(music,pluck(ch[[1,3,2,0][kk]]+12,0.4),tk,0.065)
    for kk in range(2):
        tk=th+kk*beat
        if tk<END: add(music,kick(),tk,0.24 if kk==0 else 0.16); add(music,hat(),tk+beat/2,0.06)
        if kk==1 and tk<END: add(music,clap(),tk,0.10)
    b+=1
# C) firma: acorde de Re mayor add9 sonando hasta el final
fin=[50,57,62,64,66,69,74]; n=int((DUR-END)*SR); tt=t(n); s=np.zeros(n)
for m in fin: s+=np.sin(2*np.pi*NOTE(m)*tt)+0.3*np.sin(2*np.pi*2*NOTE(m)*tt)
s*=np.exp(-tt*0.5)*np.minimum(1,tt/0.01)*np.minimum(1,(DUR-END-tt)/0.6).clip(0,1); add(music,s/len(fin),END,0.4)
add(music,kick(0.9),END,0.3)
music=lp_fast(music,8000)

# ---------- EFECTOS
def noise(n): return rng.standard_normal(n)
def whoosh(dur=0.5,lo=300,hi=5000,rev=False):
    n=int(dur*SR); x=noise(n); tt=t(n)/dur
    # barrido: mezcla de bandas con envolvente en campana
    a=bp_fast(x,lo,hi*0.5); b=bp_fast(x,lo*3,hi)
    m=tt if not rev else 1-tt
    y=a*(1-m)+b*m; e=np.sin(np.pi*np.clip(tt,0,1))**2
    if rev: e=np.clip(tt,0,1)**2*(tt<0.97)+0
    return y*e/np.max(np.abs(y)+1e-9)
def hit(dur=0.6,body=55):
    n=int(dur*SR); tt=t(n); f=body+120*np.exp(-tt*35); ph=2*np.pi*np.cumsum(f)/SR
    s=np.sin(ph)*env(n,0.001,dur,5)+0.35*hp_fast(noise(n),2500)*env(n,0.001,0.05,6)
    return s/np.max(np.abs(s))
def pop(f=900,dur=0.12):
    n=int(dur*SR); tt=t(n); ff=f*(1+0.6*np.exp(-tt*60)); s=np.sin(2*np.pi*np.cumsum(ff)/SR)*env(n,0.002,dur,7); return s
def swish(dur=0.28): x=bp_fast(noise(int(dur*SR)),1500,9000); return x*np.sin(np.pi*t(len(x))/dur)**3/np.max(np.abs(x))
def click(): n=int(0.04*SR); return hp_fast(noise(n),3000)*env(n,0.0005,0.03,8)+0.5*pop(2200,0.04)
def ding(f=1318.5,dur=1.2):
    n=int(dur*SR); tt=t(n); s=sum(np.sin(2*np.pi*f*k*tt)*np.exp(-tt*(3+k*2))/k for k in (1,2.76,5.4)); return s*np.minimum(1,tt/0.002)
def chime():
    out=np.zeros(int(1.4*SR)); 
    for i,m in enumerate([81,85,88,93]): add(out,ding(NOTE(m),1.2),i*0.07,0.5)
    return out
def ring():
    n=int(0.5*SR); tt=t(n); s=(np.sin(2*np.pi*440*tt)+np.sin(2*np.pi*480*tt))*((tt*20).astype(int)%2==0)
    return lp_fast(s,3000)*np.minimum(1,np.minimum(tt/0.01,(0.5-tt)/0.05))*0.5
def tick(): return pop(3000,0.03)
def subdrop(dur=1.4):
    n=int(dur*SR); tt=t(n); f=70*np.exp(-tt*1.2)+28; return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*2)*np.minimum(1,tt/0.02)
def riser_down(dur=2.0):
    n=int(dur*SR); tt=t(n); f=900*np.exp(-tt*1.4)+120; s=np.sin(2*np.pi*np.cumsum(f)/SR)*0.3+0.6*bp_fast(noise(n),500,4000)*np.exp(-tt*1.2)
    return s*np.minimum(1,tt/0.05)*np.exp(-tt*0.8)
def sparkle():
    out=np.zeros(int(0.9*SR))
    for i,m in enumerate([93,97,100,105,109]): add(out,ding(NOTE(m),0.6),i*0.045,0.35)
    return out
def boing():
    n=int(0.35*SR); tt=t(n); f=300+250*np.sin(2*np.pi*6*tt)*np.exp(-tt*6); return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,0.005,0.35,5)

def glitch(dur=0.3):
    n=int(dur*SR); x=np.zeros(n); i=0
    while i<n:
        L=int(SR*rng.uniform(0.008,0.03)); f=rng.choice([180,420,900,2400])
        tt=t(min(L,n-i)); x[i:i+len(tt)]=np.sign(np.sin(2*np.pi*f*tt))*rng.uniform(0.3,1); i+=L+int(SR*rng.uniform(0,0.01))
    return x*0.8
def buzz(dur=0.25):
    n=int(dur*SR); tt=t(n); s=np.sign(np.sin(2*np.pi*110*tt))*0.5+np.sin(2*np.pi*220*tt)*0.3; return lp_fast(s,2500)*env(n,0.005,dur,4)
def suck(dur=0.55): return whoosh(dur,200,7000,rev=True)
def clunk():
    h=hit(0.25,140)*0.7; c=click(); h[:len(c)]+=c; return h
def success():
    out=np.zeros(int(1.6*SR))
    for i,m in enumerate([72,76,79,84,88]): add(out,ding(NOTE(m),1.3),i*0.06,0.45)
    return out
def riser(dur=1.7):
    n=int(dur*SR); tt=t(n); f=200*np.exp(tt*1.6); s=np.sin(2*np.pi*np.cumsum(f)/SR)*0.25+0.5*bp_fast(rng.standard_normal(n),800,7000)
    return s*(tt/dur)**2

sfx=np.zeros(N)
C=[]
# S1 hola
C+=[(0.05,whoosh(0.45,150,4000,rev=True),0.12),(0.5,boing(),0.2),(0.52,pop(420,0.14),0.25),(0.15,sparkle(),0.08)]
for k in range(4): C.append((0.62+k*0.28,pop(1700,0.04),0.05))
for i in range(11): C.append((0.98+i*0.035+0.3,pop(900+i*70,0.05),0.09))
C+=[(1.88,whoosh(0.3,300,8000),0.24)]
# S2 soy zia
C+=[(2.38,whoosh(0.3,200,6000,rev=True),0.16),(2.42,hit(0.5,64),0.32),(2.5,sparkle(),0.14),(2.64,pop(780,0.14),0.3),(2.96,whoosh(0.3,300,8000),0.28)]
# S3 chat
C+=[(3.0,whoosh(0.5,150,5000,rev=True),0.18),(3.42,hit(0.35,90),0.22),(3.26,pop(1300,0.1),0.3),(3.5,boing(),0.12)]
for i in range(3):
    for r in range(2): C.append((3.95+i*0.08+r*0.3,tick(),0.06))
C+=[(4.57,pop(1500,0.1),0.32),(4.97,pop(500,0.12),0.14),(5.48,whoosh(0.35,300,8000),0.3)]
# S4 increible
C+=[(5.95,boing(),0.12),(5.86,swish(0.2),0.08),(6.24,swish(0.2),0.08),(6.76,whoosh(0.25,300,7000),0.14),(6.8,hit(0.4,80),0.25)]
for i in range(9): C.append((7.08+i*0.03+0.25,pop(1100+i*90,0.05),0.08))
C+=[(7.12,hit(1.0,44),0.6),(7.14,sparkle(),0.25),(7.16,whoosh(0.5,200,9000),0.2),(7.16,glitch(0.12),0.02)]
for k in range(16): C.append((7.2+k*0.045,pop(2000+((k*37)%9)*120,0.03),0.07))
C+=[(7.76,whoosh(0.3,300,8000),0.24)]
# S5 cada semana
C+=[(8.0,swish(0.3),0.14),(8.18,whoosh(0.25,400,8000),0.1)]
for i in range(6): C.append((8.15+i*0.1,pop(600+i*120,0.1),0.24))
C+=[(8.3,riser(0.7),0.07),(9.12,pop(380,0.14),0.3),(9.14,boing(),0.14),(9.16,ding(1760,0.7),0.14),(9.4,whoosh(0.3,300,8000),0.26)]
# S6 gracias
C+=[(9.62,swish(0.5),0.2),(9.66,hit(0.6,52),0.4),(9.72,pop(700,0.14),0.25),(9.7,whoosh(0.4,150,3000),0.12)]
for k in [10.2,10.62,11.0]: C+=[(k,clunk(),0.22),(k,whoosh(0.2,150,2000),0.08)]
C+=[(11.26,riser(0.4),0.08),(11.3,whoosh(0.45,300,9000),0.26),(11.32,boing(),0.12),(11.48,whoosh(0.25,300,8000),0.2)]
# S7 sigan asi
C+=[(11.66,boing(),0.14)]
for k in range(12): C.append((11.95+k*0.18,clap(),0.09))
C+=[(12.7,whoosh(0.3,200,6000,rev=True),0.16),(12.74,hit(0.7,48),0.5),(12.76,sparkle(),0.2)]
for i in range(14): C.append((11.75+i*0.07+0.3,pop(1400+(i%5)*160,0.04),0.05))
C+=[(13.28,whoosh(0.3,300,8000),0.24)]
# S8 firma
C+=[(13.45,hit(1.0,42),0.55),(13.47,sparkle(),0.2),(13.8,whoosh(0.32,400,7000),0.14),(14.14,pop(420,0.14),0.3),(14.15,boing(),0.1),
    (14.45,pop(1600,0.05),0.08),(14.7,pop(1700,0.05),0.08),(15.12,whoosh(0.45,300,8000),0.2),(15.26,swish(0.3),0.14),
    (15.74,pop(2100,0.08),0.3),(15.76,ding(2093,0.8),0.18),(15.78,chime(),0.12),(15.9,swish(0.3),0.08)]
for at,x,g in C: add(sfx,x,at,g)
sfx=hp_fast(sfx,50)

# ---------- VOZ + carve de la musica bajo la voz
vo=np.zeros(N); v=read_wav(HERE+'/../voz/zia-voz-limpia.wav'); add(vo,v,VO_OFF,1.0)
win=int(0.05*SR); e=np.sqrt(np.convolve(vo**2,np.ones(win)/win,'same')); active=(e>db(-40)).astype(float)
hold=np.convolve(active,np.ones(int(0.18*SR)),'same')>0; g=lp_fast(hold.astype(float),4.0).clip(0,1)
music_g=music*(1-g*(1-db(-16)))
MG=1.05; FG=0.55
mix=vo*1.0+music_g*MG+sfx*FG
stems={'voz':vo,'musica':music_g*MG,'efectos':sfx*FG}
os.makedirs(HERE+'/stems',exist_ok=True)
for k,x in stems.items(): write_wav(f'{HERE}/stems/{k}.wav',x)
write_wav(HERE+'/mezcla-pre.wav',mix)
m=hold>0
def lvl(x): return 20*np.log10(np.sqrt(np.mean(x**2))+1e-12)
print('voz',round(lvl(vo[m]),1),'musica bajo voz',round(lvl((music_g*MG)[m]),1),'diferencia',round(lvl(vo[m])-lvl((music_g*MG)[m]),1),'dB')
