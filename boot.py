print("-----------Boot.py start------------")
#imports
import machine
import time
from machine import UART

#Setter opp fysiske grensesnitt

#lora
lora = UART(1, 57600, rx=16, tx=17)
lora.init(57600, rx=16, tx=17)
lora_nrst = machine.Pin(4, machine.Pin.OUT)
lora_nrst.value(0)
time.sleep(1)
lora_nrst.value(1)
time.sleep(2)

#Funksjon for å skrive til lorabrikken
def lora_write( inndata ):
    utdata = str(inndata) + "\r\n"
    lora.write(utdata)
    time.sleep(1)
    return

#Funksjon for å lese data fra lora uten \r\n bak og foran
def lora_read():
    inndata = str(lora.readln())
    utdata = inndata.replace("\r\n", "")
    return utdata

#Funksjon for å skrive til lora og lese svaret
def lora_return( inndata ):
    utdata = str(inndata) + "\r\n"
    lora.write(utdata)
    time.sleep(1)
    inndata = str(lora.readln())
    utdata = inndata.replace("\r\n", "")
    return utdata

#Setter spreading factor og kanaler
lora_return("mac set dr 5") #dr 3 = SF9, dr 0 = SF12, dr 5 = SF7
lora_return("mac set adr on") #Kan velge SF ved behov
lora_return("mac set ch dcycle 0 256") #Lav verdi vil si at den brukes ofte
lora_return("mac set ch dcycle 1 65535") #Høy verdi betyr at den nesten ikke brukes
lora_return("mac set ch dcycle 2 65535")
lora_return("mac set ch dcycle 3 65535")
lora_return("mac set ch dcycle 4 65535")
lora_return("mac set ch dcycle 5 65535")
lora_return("mac set ch dcycle 6 65535")
lora_return("mac set ch dcycle 7 65535")
lora_return("mac set ch dcycle 8 65535")
lora_return("mac set ch dcycle 9 65535")
lora_return("mac set ch dcycle 10 65535")
lora_return("mac set ch dcycle 11 65535")
lora_return("mac set ch dcycle 12 65535")
lora_return("mac set ch dcycle 13 65535")
lora_return("mac set ch dcycle 14 65535")
lora_return("mac set ch dcycle 15 65535")
lora_return("mac set ch dcycle 16 65535")


#Setter opp TTN
#lora_return("mac set dr 0") #Dette er SF12 (Liten payload-storrelse og lav datarate)
lora_return("mac set deveui 0004A30B00210AD0")
lora_return("mac set appeui 70B3D57ED00098A3")
lora_return("mac set appkey BB20FE6877D411F8D87FBE616986EFC1")
lora_return("mac set devaddr 260118BC")

#Skriver info
lora.flush()
print("Lora system: " + lora_return("sys get ver"))
print("Voltage: " + lora_return("sys get vdd"))
print("Adaptive data rate is: " + lora_return("mac get adr"))
print("Actual data rate is: " + lora_return("mac get dr"))
print("Band is : " + lora_return("mac get band"))
print("DEVADR: " + lora_return("mac get devaddr"))
print("DEVEUI: " + lora_return("mac get deveui"))
print("APPEUI: " + lora_return("mac get appeui"))

lora.flush()
#Joiner TTN

#Dette er for OTTA (som ikke fungerer?)
#print("Lora OTAA TTN info : " + lora_return("mac join otaa"))

#Dette er for ABP
lora_return("mac set nwkskey 4D4C6D51180C6796747740DFC6C144E0")
lora_return("mac set appskey AC2F3543F86E63382E78580D80D6E477")
print("Lora ABP TTN info : " + lora_return("mac join abp"))

#time.sleep(10)
print("Lora OTAA TTN join status: " + lora_read())
print("Sender confirmed melding: " + lora_return("mac tx cnf 1 FAFAFA"))

print("-----------Boot.py ferdig------------")