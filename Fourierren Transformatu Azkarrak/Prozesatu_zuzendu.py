import serial
import time
import matplotlib.pyplot as plt

name="_5_1s1"   
denbora=1   

def RR_kalkulatu(t): 
    global taupada_zaharra
    taupada_berria=t
    RR=taupada_berria-taupada_zaharra
    taupada_zaharra=taupada_berria
    return RR
    

data =dict()                

with open("data"+name+".txt", "r") as f1:
    for line in f1:
        t,v=line.split()
        data[int(t)]=int(v)

#RR-ren kalkulua
muga=550
muga_azpitik=True
taupada_zaharra=0.0001
k=0
RR_d=dict()

with open("RR"+name+".txt", "w") as f2:
    for t,v in data.items():
        if v>muga and muga_azpitik==True:
            muga_azpitik=False
            RR=RR_kalkulatu(t)
            k=k+1
            if k<2:
                continue
            s=f"{k:5}   {t:10}   {RR:10}\n"
            f2.write(s)
            RR_d[k]=RR
            #print(s,end="")
        elif v<muga:
            muga_azpitik=True
            
        
            
        
        
        
    
    
