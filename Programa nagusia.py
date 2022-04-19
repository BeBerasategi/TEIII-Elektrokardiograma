import serial
import time
import matplotlib.pyplot as plt

name="_00_"   #Sortuko diren fitxategiak izendatzeko.
denbora=1      #Neurketak iraungo duen denbora, minututan.

def datuak_irudikatu():
    plt.plot(data.keys(),data.values())
    plt.xlabel('Denbora (ms)')
    plt.ylabel('Voltaia (mV)')
    plt.title('Sentsorearen irakurketa vs. Denbora')
    plt.show()

def taupada_irudikatu():
    plt.plot(RR_d.keys(),RR_d.values())
    plt.xlabel('Taupada')
    plt.ylabel('RR (ms)')
    plt.title('RR vs. Taupadak')
    plt.show()

def taupada_kalkulatu(t):       #Honek taupadak/minutu kalkulatzen ditu.
    global taupada_zaharra
    taupada_berria=t
    dif=taupada_berria-taupada_zaharra
    BPM=60000/dif
    taupada_zaharra=taupada_berria
    return BPM

def RR_kalkulatu(t):            #Honek RR milisegundutan ematen du.
    global taupada_zaharra
    taupada_berria=t
    RR=taupada_berria-taupada_zaharra
    taupada_zaharra=taupada_berria
    return RR
    
    
#Zati honek arduinoaren informazioa programara ekartzen du.---------------------------------------------------------------------------
#Internetetik hartutakoa delako dago inglesez.

# set up the serial line
ser = serial.Serial('COM5', 9600)
time.sleep(3)

# Read and record the data
data =dict()                      # empty list to store the data
trigger=True

ft=1
while ft<denbora*60000:
    print(ft/1000)                 #Segunduak inprimatu
    try:
        b = ser.readline()         # read a byte string
        string_n = b.decode()      # decode byte string into Unicode  
        string = string_n.rstrip() # remove \n and \r
        strings = string.split("sep")
        ft = int(strings[0])      # convert string to int
        fv = int(strings[1])
    except:
        continue
    if ft==0:
        trigger=False
    elif trigger==True:
        continue
        
    data[ft]=fv                # add to the end of data list
    #time.sleep(0.1)           # wait (sleep) 0.1 seconds

ser.close()
#-----------------------------------------------------------------------------------------------------------------------------------------
 
#Neurketa guztiak testu fitxategi batean gordeko dira. Zutabe batean denbora, bestean voltaia.

with open("data"+name+".txt", "w") as f1:
    for t,v in data.items():
        s=f"{t:10}   {v:10}\n"
        f1.write(s)
        #print(s, end="")
        
print("Neurketa guztiak hartuta")

datuak_irudikatu()

#RR-ren kalkulua:

muga=550                 #Proba batzuk egin ondoren eta ajustatuz, balio egokia lortzen da.
muga_azpitik=True
taupada_zaharra=0.0001
k=0
RR_d=dict()

with open("RR"+name+".txt", "w") as f2:    #Taupaden arteko denbora erregistratuko da.
    for t,v in data.items():
        if v>muga and muga_azpitik==True:
            muga_azpitik=False
            RR=RR_kalkulatu(t)
            k=k+1
            if k<2:
                continue
            s=f"{k:5}   {RR:10}\n"
            f2.write(s)
            RR_d[k]=RR
            #print(s,end="")
        elif v<muga:
            muga_azpitik=True
            
print("Taupadak kalkulatuta")

taupada_irudikatu()

print("Programa bukatu da")
        
