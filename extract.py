import requests
import time
url = "https://reco.nz/solve/10662"
n = 0

def infofind(link):
    purehtml = requests.get(link).text.split("\n")
    for line in purehtml:
        if "id=\"reconstruction" in line:
            scramble = ((purehtml[purehtml.index(line)+1]).split("<")[0].lstrip())

            #print(purehtml[purehtml.index(line):purehtml.index(line)+10])    
            rotation = ((purehtml[purehtml.index(line)+2]).split("<")[0].lstrip().split("//")[0].rstrip())
            cross = (purehtml[purehtml.index(line)+4]).split("<")[0].lstrip()
            return(scramble + " : " + rotation + " " + cross + "\n")
        
with open("tymon3x3only.txt", "r") as f:
    with open("tymoncross.txt", "a") as g:
        for link in f.readlines():
            n += 1
            g.write(infofind(link.split("\n")[0]))
            print(str(n) + " / 590")


with open("everytymonsolutionbuthtml.txt", "a") as f:
    with open("tymon3x3only.txt", "r") as g:
        for link in g.readlines():
            n += 1 
            print(requests.get(link.split("\n")[0]))
            f.write(str(n) + "::: \n" + str(requests.get(link.split("\n")[0]).text) + "\n")