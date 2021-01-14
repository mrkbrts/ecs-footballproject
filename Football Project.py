#
# Football Project made by Engame Coding Society
# Members: 
# Created on the 21th of December 2020.
# Version: 1.0
#

import sys
import subprocess

endSignal = ""

while endSignal != "end":    
    #The program asks you to choose a team and a function:
    clubName = str(input("Bayern München or Liverpool FC? "))
    print("\n[nationality/uniform/captain/youngest and oldest member/members]") #still to be filled in!!
    programFunction = str(input("What information would you like to get? "))
    print("\n-----", clubName, "-", programFunction, "-----\n")

    #Clarification
    if clubName == "Bayern München" or clubName == "Bayern Munchen":
        clubName = "Bayern"
    if clubName == "Liverpool F.C." or clubName == "Liverpool FC" or clubName == "Liverpool Football club":
        clubName = "Liverpool"

    #Bánk - Name of the coach

    #Máté - Nationality:
    if programFunction == "nationality":
        if clubName.lower() == "liverpool":
            print("Liverpool Football Club is a professional football club in Liverpool, England, that competes in the Premier League, the top tier of English football. A total of 28 footballers play in Liverpool FC : Goalkeepers: Alisson Becker(BRA), Adrián(ESP) , Caoimhin Kelleher(IRL), Defenders: Virgil Van Dijk(NED), Joe Gomez(ENG), Kostas Tsimikas(GRE), Andrew Robertson(SCO), Joel Matip(CMR), Trent-Alexander Arnold(ENG), Sepp van den Berg(NED), Neco Williams(WAL) Midfielders: Fabinho(BRA), Wijnaldum(NED), Thiago Alcantara(ESP), James Milner(ENG), Naby Keita(GUI), Jordan Henderson(ENG), Alex Oxlade-Chamberlain(ENG), Curtis Jones(ENG), Ben Woodburn(WAL) Attackers: Roberto Firmino(BRA), Sadio Mané(SEN), Mohamed Salah(EGY), Minamino Takumi(JAP), Diego Jota(POR), Xherdan Shaqiri(SUI), Divock Origi(BEL), Harry Wilson(WAL)")
        elif clubName.lower() == "bayern":
            print("FC Bayern, is a German professional sports club based in Munich, Bavaria, that competes in the Bundesliga. A total of 19 fotballers play in Bayern München: Goalkeepers: Manuel Neuer(GER), Alexander Nübel(GER), Defenders: Niklas Süle(GER), Benjamin Pavard(FRA), Jerome Boateng(GER), Alphonso Davies(CAN), Lucas Hernández(FRA), David Alaba(AUT) Midfielders: Javi Martínez(ESP), Mickael Cuisance(FRA), Leon Goretzka(GER), Corentin Tolisso(FRA), Joshua Kimmich(GER) Attackers: Robert Lewandowski(POL), Leroy Sané(GER), Serge Gnabry(GER), Thomas Müller(GER), Kingsley Coman(FRA), Joshua Zirkzee(NED)")


    #Márk - Picture of their unifrom
    if programFunction == "uniform":
            def openImage(path):
                imageViewerFromCommandLine = {'linux':'xdg-open',
                                              'win32':'explorer',
                                              'darwin':'open'}[sys.platform]
                subprocess.run([imageViewerFromCommandLine, path])

            if clubName == "Bayern":
                openImage("/Users/bartosmark/Google Drive/ENGAME /{coding} Society/4th meeting/Bayern.jpg")
            elif clubName == "Liverpool":
                openImage("/Users/bartosmark/Google Drive/ENGAME /{coding} Society/4th meeting/Liverpool.jpg")

    #Barnabás - Salary of the most famous member

    #Boti - Name of the captain
    if programFunction == "captain":
        if clubName.lower() == "bayern":
                print("The captain of FC Bayern München is Manuel Neuer.")
        elif clubName.lower() == "liverpool":
                print("The captain of Liverpool FC is Jordan Henderson.")
        else:
            print("Please write 'Liverpool' or Bayern München!")
            clubName = input("Which team's captain would you like to know? Bayern München or Liverpool? ")

    #Heni - Youngest and oldest member
    if programFunction == "youngest and oldest member":
        if clubName.lower() == "bayern":
            print("The youngest member is Marcelo Pitaluga(20.12.02), the oldest member is James Milner(04.01.86)")

        elif clubName.lower() == "liverpool":
            print("The youngest member is Jamal Musiala(26.02.03), the oldest member is Manuel Neuer(27.03.86).")

            

    #Heni - List of the team members' names
    if programFunction == "members":
        if clubName.lower() == "bayern":
            print("Goalkeepers: Manuel Neuer, Alexander Nübel, Ron-Thorben Hoffmann Defenders: Niklas Süle, Benjamin Pavard, Jerome Boateng, Alphonso Davies, Lucas Hernández, David Alaba, Bouna Sarr, Tanguy Nianzou, Chris Richards Midfielders: Javi Martínez, Leon Goretzka, Corentin Tolisso, Joshua Kimmich, Tiago Dantas, Marc Roca Attackers: Robert Lewandowski, Leroy Sané, Serge Gnabry, Thomas Müller, Kingsley Coman, Joshua Zirkzee, Douglas Costa de Souza, Eric Maxim Choupo-Moting, Kingsley Coman, Jamal Musiala")
        elif clubName.lower() == "liverpool":
            print("Goalkeepers: Alisson Becker, Adrián, Caoimhin Kelleher, Marcelo Pitaluga Defenders: Virgil Van Dijk, Joe Gomez, Kostas Tsimikas, Andrew Robertson, Joel Matip, Trent-Alexander Arnold, Sepp van den Berg, Neco Williams, Nathaniel Phillips, Rhys Williams Midfielders: Fabinho, Wijnaldum, Thiago Alcantara, James Milner, Naby Keita, Jordan Henderson, Alex Oxlade-Chamberlain, Curtis Jones, Xherdan Shaqiri  Attackers: Roberto Firmino, Sadio Mané, Mohamed Salah, Minamino Takumi, Diego Jota, Divock Origi")

    print("----------------------------\n")
    endSignal = str(input("Write [end] to end the program, press [Enter] to continue. "))
