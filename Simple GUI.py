#import tkinter
from tkinter import *
from tkinter.messagebox import *
import StationGraph
import TubeAStar


Window = Tk()
Window.title("Station Travel Path")
Window.geometry("500x500")
Window.configure(background = "#ffffff")

def Calculate():
    print ("value is", var1.get())
    CalculateLabel = Label(Window, text = "Shortest Route: ")
    CalculateLabel.grid(row = 4, column = 1)
    print("step 6")
    
    startingStation = var1.get()
    endingStation = var2.get()
    
##    path = TubeAStar.AStar(startingStation, endingStation)
##    graph = StationGraph.getGraph()
##    stationPath = ""
##    for station in result:
##        stationData = graph.get(station)
##        stationPath += (stationData[0]+", "+station+"\n")
##    ShortestPath  = Label(Window, text = stationPath)
    Window.quit()


### WIDGETS OUTSIDE OF FUNCTION
print("Welcome")
#WIDGETS HERE
print("step 2")

nameToId = StationGraph.getNameToId()
stationNames = StationGraph.getNameOnly()
print("step 3")

### Starting
startStationSelect = Label(Window, text = "Start Station: ")
startStationSelect.grid(row =1, column = 1)

var1 = StringVar(Window)
var1.set("Default")
startStation = OptionMenu(Window, var1, *stationNames)
startStation.pack()
startStation.config(width=20)
startStation.grid(row =1, column = 2)


print("step 4")
###Ending
endStationSelect = Label(Window, text = "End Station: ")
endStationSelect.grid(row =2, column = 1)


var2 = StringVar(Window)
var2.set("Default")
endStation = OptionMenu(Window, var2, *stationNames)
endStation.pack()
endStation.config(width=20)
endStation.grid(row =2, column = 2)


print("step 5")
###Stations Selected
stationSelected = Label(Window, text = "Calculate Route: ")
stationSelected.grid(row =3, column = 1)

CalculateNow = Button(Window, text ="Click Here", command=Calculate())
CalculateNow.pack()
CalculateNow.grid(row = 3, column = 2)   

mainloop()
