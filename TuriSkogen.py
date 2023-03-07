#################################################################################
#                                                                               #
#                     Spill laget av Christer Havn                              #
#                           21.11.2022                                          #
#                                                                               #
#                                                                               #
#################################################################################

import time
# Importerer time fra time library-et som blir brukt for å sakke tekst.

# Scene 1 er i en funksjon som er et gruppe av kode som berre blir brukt når den blir kallet fram. Jeg synest det er mykje ryddigere når jeg har dette sånn.

def Scene1():
        S1 = input("Du er på veien heim etter din daglige tur i skogen, på veien heim kommer du til en sti med tre veier, en vei *fram*, en annen vei til *venstre*, og en vei til *høgre*, hva velger du? \n") 
        # S1 = Spørsmål 1, så betyr at dette er første spørsmålet i teksten. Og her får du tre valg som er markert med *.  \n er for å få en ny linje.
        if S1 == "fram":
                print("Du velgte å gå rett fram og nå kom du trygt hjem.")
                Scene2fram()
        elif S1 == "venstre":
                print("Du bestemte deg til å gå til venstre og ser en flokk med ulver springe mot deg!!")
                Scene2venstre()
        elif S1 == "høgre":
            print("Du bestemte deg til å gå til høgre og du fant ett milliard kroner i et hus og blei rik!!!") 
            Scene2høgre()

        # Visst valget i første teksten var *fram* så går det øver til neste Scene.
        # Det er det samme her.
        # Det er også lurt å vete at "if" betyr visst og "elif" betyr eller vist. Som visst du går fram så går du der ELLER visst du går til venstre går du til venstre, osv.
        # Print skriver ut en melding som f.e print("Hello World").
        # Input er en kommndo som spør et spørsmål. I dette tilfelle brukes det for å fortelle historien.       

def Scene2fram():
        S3 = input("Endelig hadde du kommet heim og du tenkte skulle eg *drikke* litt vatn? eller burde jeg se på *TV*? \n")
        if S3 == "drikke":
                print("Du bestemte deg for å drikke vatn, og haldt deg hydrert! God slutt.")
        elif S3 == "TV":
                print("Du satt deg ned og såg på TV-en til du sovnet. Ok slutt")
        # Det er det samme her bortsettfra at det ikke kaller en funksjon på slutten, dette er fordi det er slutten av spillet. Her kan du vite om du får en God slutt eller en Dårlig slutt, det er også Ok slutt som er midt i mellom.

def Scene2høgre():
        S2 = input("Du er nå blitt rik og er på veien heim, men du ser en mann på en benk. Vill du si hei og *snakke* med han, eller vill du *gå* videre? \n")
        if S2 == "snakke":
                print("Du gikk bort til mannen og visste han pengene dine, men han sa til deg at pengene var falsk og verdt null komma niks. Dårlig slutt.")
        elif S2 == "gå":
                print("Du gikk forbi mannen og kom heim med pengene dine. God slutt")

def Scene2venstre():
        S4 = input("Det ser ut som du klarte å komme deg vekk i fra ulven, på en eller annen måte. Foran deg er et *hus* eller en *landsby*, hvor går du? \n")
        if S4 == "hus":
                print("Døren til huset var visst åpen, og det var en snill familie der inne som tok deg med varme hender. God slutt!")
        elif S4 == "landsby":
                print("Du gikk inne i landsbyen og fant desverre flere ulver og møtte på ditt siste syn før døden. Dårlig slutt.")

def Intro():
        navn = input("Velkommen til En tur i Skogen, hva heter du?")
        print("Glimrande,",navn, "då tar vi litt tid for å starte programmet.")
        time.sleep(2)
        Scene1()
Intro()

        # Dette er intro-en til spillet. Som då starter med å si navnet på spillet også spør et spørsmål. Visst du ser nøye ser du at spørsmålet er en del av navn variablen. Dette er for at spillet skal simulere at du har skrevet inn navnet ditt.
        # Jeg bruker også time.sleep her for å simulere at spillet tar tid for å starte.
        # Etter det så kaller spillet in Scene1.

time.sleep(1)
        
print("Takk for at du bestemte deg for å spillet dette! :)")

Slutt = input("Press hva som helst knapp for å slutte programmet.")

        # Slutt melding når du har blitt ferdig med spillet. Takk!
        # Input kommand for å forhindre at spillet lukker seg selv med engang etter siste linje.


