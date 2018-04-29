from tkinter import *
from tkinter.messagebox import *
import StationGraph
import TubeAStar

Window = Tk()
Window.title("Station Travel Path")
Window.geometry("500x500")
Window.configure(background = "#ffffff")

nameToId = StationGraph.getNameToId()
stationNames = StationGraph.getNameOnly()

###
startStationSelect = Label(Window, text = "Start Station: ")
startStationSelect.grid(row =1, column = 1)

var1 = StringVar(Window)
var1.set("Default") # initial value
startStation = OptionMenu(Window, var1, *stationNames)
startStation.pack()
startStation.grid(row =1, column = 2)


#############
endStationSelect = Label(Window, text = "End Station: ")
endStationSelect.grid(row =2, column = 1)

var2 = StringVar(Window)
var2.set("Default")
endStation = OptionMenu(Window, var2, *stationNames)
endStation.pack()
endStation.grid(row =2, column = 2)


#
# test stuff

def Calculate():
    startingStation = var1.get()
    startingStationID = nameToId[startingStation]
    endingStation = var2.get()
    endingStationID = nameToId[endingStation]

    path = TubeAStar.AStar(startingStationID, endingStationID)
    pathNames = []
    graph = TubeAStar.getGraph()
    for station in path:
        stationData = graph.get(station)
        stationData = str(stationData[0])
        pathNames.append(stationData)
    pathNames = pathNames[::-1]
    temp = ""
    for x in pathNames:
        if x == endingStation:
            temp += x
            continue
        temp += x+", "
    totalTime = StationGraph.calculateTime(path)
    mainMessage = temp+"\nTotal Tube Travel Time: "+str(totalTime)+" minutes"
    titleMessage = "Shortest Route from "+str(startingStation)+" to "+str(endingStation)
    shortestRoute = messagebox.showinfo(titleMessage, mainMessage)
    Window.quit()
    

CalculateNow = Button(Window, text="Click Here", command=Calculate)
CalculateNow.pack()
CalculateNow.grid(row = 3, column = 2) 

mainloop()
