import numpy as np
from matplotlib import pyplot as plt

def RSA_kalkulatu(f):
    h=dict()
    fitx="RR_6_"+str(f)+"s1.txt"
    with open(fitx,"r") as data:
        for line in data:
            k,RR=line.split()
            h[int(k)]=float(RR)

    k0=min(h.keys())
    kmax=max(h.keys())

    k=k0+1
    #Datu sorta guztiak dira hasieran gorakorrak.
    #Agertuko den lehenengoa maximo bat izango da.
    #(max,min)_i bikoteak izango ditugu.
    i=0
    hmm=dict()

    while k<kmax:
        if h[k]>h[k-1]: #Gorakorra da
            if h[k]>=h[k+1]: #Maximoa da
                hmm[i]=[h[k]]
        elif h[k]<h[k-1]: #Beherakorra da
            if h[k]<=h[k+1]: #Minimoa da
                try:
                    hmm[i].append(h[k])
                except:
                    pass
                i+=1
        k=k+1

    kendu=[]
    for i in hmm:
        if len(hmm[i])==1:
            kendu.append(i)
    print(kendu)
    for i in kendu:
        del hmm[i]

    print("RSA, banaka:",[(k-v)/2 for k,v in hmm.values()])
    RSA=sum([(k-v)/2 for k,v in hmm.values()])/len(hmm)
    print("RSA batezbeste:", RSA)
    return RSA

l=[0]*5
for j in range(5):
    l[j]=RSA_kalkulatu(j+1)

v=[4,5,6,8,10]

plt.plot(v, l)
##plt.xlim([0.02, 0.5])
##plt.ylim([-500, 10000000])
plt.title("Erresonantzia")
plt.grid(True)
plt.show()

with open("RSA.txt", "w") as f:
    for i in range(len(v)):
        s=f"{v[i]}    {l[i]:10.5}\n"
        f.write(s)

