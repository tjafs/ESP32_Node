print("-----------main.py ferdig------------")

import time
gps.flush()

#Aktiv settes til 0 dersom en gpio ligger høy eller lav slik at vi kan droppe til repl ved behov
aktiv = 0


gps = UART(2, 9600, rx=12, tx=27)
gps.init(9600, rx=12, tx=27)
gps_nrst.value(1)

print("Setter korrekte GPS pinner i 60 sekunder og bytter deretter til ubrukte pinner, men lar GPS-en stå på!")

while aktiv is not 120:

    print(str(aktiv) + str(gps.read()))

    time.sleep(1)
    aktiv = aktiv + 1

    #Kjører en 30 sekunders innhentingstid av data
    #while innhentingstid <= 60:
        #Sjekk om gyldig GPS-data eksiterer og hent disse. Legg til i arbeidsarray for GPS-data
        #Sjekk om gyldig Tempraturdata eksiterer og hent disse. Legg til i arbeidsarray for Temp data
        #Sjekk om gyldig luftfuktighetsdata eksiterer og hent disse. Legg til i arbeidsarray for Temp data
        #Sjekk om gyldig Partikkelmålingdata eksiterer og hent disse. Legg til i arbeidsarray for partikkelmåledata
        #Eventuelt: Når det blir foretatt en gyldig avlesning av en verdi så skal denne også legges  på UART0
        #med en prefix. På den måten kan vi ha en applikasjon på PC med kontinuerlig plotting av data
        #Teller
        #innhentingstid = innhentingstid +1
        #time.sleep(0.5)
        #Heartbeat
        #print(".")
    #Nå er det opprettet en array for hver måleverdi over en periode på 30 sekunder
    #Disse arrayene lavpassfiltreres, eventuelt om vi tar statistisk middelverdi og kaster alt utenfor +- 1 sigma
    #Vi ender opp med en tallverdi for hver type måledata. Denne settes sammen med klokkeslett fra GPS og sendes via lora

gps = UART(2, 9600, rx=12, tx=27)
gps.init(9600, rx=12, tx=27)
gps_nrst.value(1)

print("-----------Boot.py ferdig------------")