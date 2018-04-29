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
    endingStation = var2.get()
    print ("Start is "+ startingStation)
    print ("End is "+ endingStation)

    path = TubeAStar.AStar(startingStation, endingStation)

    shortestRoute = messagebox.showinfo("Shortest Route:\n", startingStation)
    Window.quit()
    

CalculateNow = Button(Window, text="Click Here", command=Calculate)
CalculateNow.pack()
CalculateNow.grid(row = 3, column = 2) 

mainloop()
