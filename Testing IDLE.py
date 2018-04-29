from tkinter import *
from tkinter.messagebox import *
import StationGraph
import TubeAStar

Window = Tk()
nameToId = StationGraph.getNameToId()
stationNames = StationGraph.getNameOnly()

var1 = StringVar(Window)
var1.set("Default")
startStation = OptionMenu(Window, var1, *stationNames)
startStation.pack()

def Calculate():
    print ("value is", var1.get())

CalculateNow = Button(Window, text ="Click Here", command=Calculate())
CalculateNow.pack()

mainloop()
