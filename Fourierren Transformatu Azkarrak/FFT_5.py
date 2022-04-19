import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq

h=dict()
ht=dict()
with open("RR_etzanda.txt","r") as data:
    for line in data:
        k,t,RR=line.split()
        h[int(k)]=float(RR)
        ht[int(t)]=float(RR)
            
mmax=max(h.keys())
mmin=min(h.keys())

N=mmax-mmin+1

SAMPLE_RATE=1.3
yf = rfft(list(h.values()))
xf = rfftfreq(N, 1 / SAMPLE_RATE)

anplitude=np.abs(yf)
power=anplitude**2

plt.plot(xf, power)
plt.xlim([0.02, 0.5])
plt.ylim([-500, 10000000])
plt.title("Etzanda")
plt.grid(True)
plt.show()

with open("FFT_5_1.txt", "w") as f:
    for i in range(len(xf)):
        s=f"{xf[i]:10.5}     {power[i]:10.5}\n"
        f.write(s)



h=dict()
with open("RR_zutik.txt","r") as data:
    for line in data:
        k,t,RR=line.split()
        h[int(k)]=float(RR)
        ht[int(t)]=float(RR)
            
mmax=max(h.keys())
mmin=min(h.keys())

N=mmax-mmin+1

SAMPLE_RATE=1.65
yf = rfft(list(h.values()))
xf = rfftfreq(N, 1 / SAMPLE_RATE)

anplitude=np.abs(yf)
power=anplitude**2

plt.plot(xf, power)
plt.xlim([0.015, 0.5])
plt.ylim([-500, 2000000])
plt.title("Zutik")
plt.grid(True)
plt.show()

with open("FFT_5_2.txt", "w") as f:
    for i in range(len(xf)):
        s=f"{xf[i]:10.5}     {power[i]:10.5}\n"
        f.write(s)
