from tkinter import *
from PIL import *
from PIL import Image
import math
primzahlen = [2]
global Pixelpos
global Kandidat
global i
global n

Kandidat = 3

def isprime():
    k = Kandidat
    i = 1
    for i in primzahlen:
        # print("Iterarting Kandidat "+str(k)+" with i="+str(i))
        if k%i == 0: # K is not a prime since it can be divide by the prime i
            return False
        if math.sqrt(k) <= i: #reduces search time
            # print("Tiggering break of for sqrt:"+str(math.sqrt(k))+"and prime"+str(i))
            break
    return True

Volume = int(input("How many digits do you want to generate:"))
while len(primzahlen) < Volume:
    if isprime() == True:
        primzahlen.append(Kandidat)
        # print("Added Number: "+str(Kandidat))
    Kandidat +=1

Info = input("Do you want to display the list (1), display the last digit (2) or nothing (n)")
if Info== "1":
    for primzahl in primzahlen:
      print(primzahl)
if Info== "2":
      print(primzahlen[-1])

Sizeinfo = int(input("How big do you want the Canvas to be in px:"))
canvas = Sizeinfo
center = round(canvas/2)
canvassum = canvas**2
img  = Image.new( mode = "1", size = (canvas, canvas),color = 1)
 
#This new Initialization is for drawcalculation and drawing 
tempdraw =[center+1 , center]
drawpos = 1
scale  = 1

Macrointel = math.floor(math.sqrt(drawpos)) #Breaks if you remove this part ¯\_(ツ)_/¯ 
if Macrointel%2==1:
    Macrointel -= 1 
    
def gettempdraw():
    global tempdraw
    Macropos = math.floor(math.sqrt(drawpos)) #Figuring out the Macro position
    if Macropos%2==1:
        Macropos -= 1 #To make programming simpler only even Macropositions are used

    tempdraw = [center+1 , center]# Resets to the first even Macropos
    #print("Neutral tempdraw (Now: "+str(tempdraw)+" )")
    tempdraw[0]-= (Macropos /2 ) # x coordiante
    tempdraw[1]-= (Macropos /2 ) # y coordiante
    #print("Selcted Macrointel Tempdraw (Now: "+str(tempdraw)+" )")
    Micropos = (drawpos - Macropos**2) # This is the distance from our starting point furhter down the line,
                                 # now to make the turns with loads of if's
    #print("Micropos: "+ str(Micropos)+ " Macropos: "+str(Macropos))
    if Micropos == 1: # One bigger than Macropos
        tempdraw[0] -= 1
        #print("One past Macropos")
    elif Micropos <= Macropos+1 :#Max (1*Macropos +1) bigger than Macropos (left line)
        tempdraw[0] -= 1
        tempdraw[1] += Micropos-1
        #print("One Macropos past Macropos")
    elif Micropos <= (2*Macropos)+1:#Max (2*Macropos +1) bigger than Macropos (bottom line)
        tempdraw[0] += Micropos-Macropos -2
        tempdraw[1] += Macropos
        #print("Two Macropos past Macropos")
    elif Micropos <= (3*Macropos)+2:#Max (3*Macropos +2) bigger than Macropos (right line)
        tempdraw[0] += Macropos
        #tempdraw[1] += Macropos- ((Micropos - (2*Macropos +1))-1)<- How it originally was
        tempdraw[1] += (3*Macropos - Micropos) + 2
        #print("Three Macropos past Macropos")
    else: # God, I hope this only chatches top line and no errors -_-
        tempdraw[0] += Macropos -(Micropos - (3*Macropos +3))
        tempdraw[1] -= 1
        #print("Four Macropos past Macropos")

def placepixel():
    gettempdraw() # Puts the Correct place into tempdraw based on drawpos
    #print("One Pixel coming up")
    #Window.create_rectangle(tempdraw[0],tempdraw[1],tempdraw[0]+1,tempdraw[1]+1,fill="black")

#print("while "+str(drawpos)+" is sammaller than "+str(canvassum))
    
#Window.create_rectangle(1,1,10,10,fill="Yellow")
#Window.create_rectangle(canvas-3,canvas-3,canvas,canvas,fill="Red") #This is used to check for dev sanity
while drawpos <= canvassum:
    if drawpos in primzahlen:
        #print("Drawpos: "+str(drawpos))
        placepixel()
        if int(tempdraw[0]) < canvas and int(tempdraw[1]) < canvas:
            #print("adding pixel")
            img.putpixel((int(tempdraw[0]),int(tempdraw[1])), 0)
    if drawpos > primzahlen[-1]:
        break
    else:
        drawpos += 1
  
print("Done")
img.show()
