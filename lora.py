#Denne filen inneholder metoder/funksjoner  tilknyttet lora


#Funksjon for å skrive data til lora
lora_write = lambda data: print(data+"\r\n")


#Funksjon for å lese data fra lora uten \r\n bak og foran
def lora_read():
    inndata = str(lora.readln())
    utdata = inndata.replace("\r\n", "")
    return utdata
