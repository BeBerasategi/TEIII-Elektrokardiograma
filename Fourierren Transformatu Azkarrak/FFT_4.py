import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq

#Sarrerako arnasketaren eredu bat egiten saiatu:
#5 periodo

h0=dict()
k=0
for i in range(50):
    for j in range(10):
        k+=1
        h0[k]=0.0
    for j in range(10):
        k+=1
        h0[k]=1.0

with open("FFT_4_0.txt", "w") as f3:
    for k in range(1,len(h0)):
        s=f"{k:10}     {h0[k]:10}\n"
        f3.write(s)

plt.plot(h0.keys(), h0.values())
plt.show()

yf = rfft(list(h0.values()))
xf = rfftfreq(1000)

anplitude=np.abs(yf)
power=anplitude**2

plt.plot(xf, power)
plt.xlim([0.02, 0.5])
plt.ylim([0, 1100])
plt.ylim([0, 120000])
plt.title("Square Wave")
plt.grid(True)
plt.show()

with open("FFT_4_1.txt", "w") as f1:
    for i in range(len(xf)):
        s=f"{xf[i]:10.5}     {power[i]:10.5}\n"
        f1.write(s)


h=dict()
with open("data_osoa.txt","r") as data:
    for line in data:
        k,RR=line.split()
        h[int(k)]=float(RR)
            
mmax=max(h.keys())
mmin=min(h.keys())

N=mmax-mmin+1

SAMPLE_RATE=1
yf = rfft(list(h.values()))
xf = rfftfreq(N, 1 / SAMPLE_RATE)

anplitude=np.abs(yf)
power=anplitude**2

plt.plot(xf, power)
plt.xlim([0.02, 0.5])
#plt.ylim([-500, 1000000])
plt.ylim([-500, 130000000])
plt.title("Square Wave Response")
plt.grid(True)
plt.show()

with open("FFT_4_2.txt", "w") as f2:
    for i in range(len(xf)):
        s=f"{xf[i]:10.5}     {power[i]:10.5}\n"
        f2.write(s)


##h.clear()
##with open("data.txt","r") as data:
##    for line in data:
##        k,RR=line.split()
##        h[int(k)]=float(RR)
##            
##mmax=max(h.keys())
##mmin=min(h.keys())
##
##N=mmax-mmin+1
##
##SAMPLE_RATE=1
##yf = rfft(list(h.values()))
##xf = rfftfreq(N, 1 / SAMPLE_RATE)
##
##anplitude=np.abs(yf)
##power=anplitude**2
##
##plt.plot(xf, power)
##plt.xlim([0.02, 0.5])
##plt.ylim([-500, 19000000])
##plt.title("Square Wave Response")
##plt.grid(True)
##plt.show()

