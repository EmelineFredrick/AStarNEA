#!/usr/bin/python
import tkinter
from tkinter import *
from tkinter.messagebox import *
import StationGraph
import TubeAStar


Window = tkinter.Tk()
Window.title("Station Travel Path")
Window.geometry("500x500")
Window.configure(background = "#ffffff")


def enterStations():
    #WIDGETS HERE
    
    ### Starting
    startStationSelect = Label(Window, text = "Start Station: ")
    startStationSelect.grid(row =1, column = 1)

    nameToId = StationGraph.getNameToId()
    var1 = tkinter.StringVar()
    global startStation
    startStation = tkinter.OptionMenu(Window, var1, *nameToId)
    startStation.config(width=20)
    startStation.grid(row =1, column = 2)

    ###Ending
    endStationSelect = Label(Window, text = "End Station: ")
    endStationSelect.grid(row =2, column = 1)

    var2 = tkinter.StringVar()
    global endStation
    endStation = tkinter.OptionMenu(Window, var2, *nameToId)
    endStation.config(width=20)
    endStation.grid(row =2, column = 2)

    ###Stations Selected
    stationSelected = Label(Window, text = "Calculate Route: ")
    stationSelected.grid(row =3, column = 1)

    CalculateNow = Button (Window, text ="Click Here", command = Calculate)
    CalculateNow.grid(row = 3, column = 2)

def Calculate():
    CalculateLabel = Label(Window, text = "Shortest Route: ")
    CalculateLabel.grid(row = 4, column = 1)
    
    global startStation
    global endStation
    
    start = Label(Window, text = startStation)
    start.grid(row = 4, column = 2)
    end = Label(Window, text = endStation)
    end.grid(row = 4, column = 3)
    
    path = TubeAStar.AStar(startStation, endStation)
    graph = StationGraph.getGraph()
    stationPath = ""
    for station in result:
        stationData = graph.get(station)
        stationPath += (stationData[0]+", "+station+"\n")
    ShortestPath  = Label(Window, text = stationPath)
    

enterStations()
Window.mainloop()


##nameToId = StationGraph.getNameToId()
##
##def f(startingStation):
##    return startingStation
##start = interactive(f, startingStation=nameToId)
##
##def g(endingStation):
##    return endingStation
##end = interactive(g, endingStation=nameToId)
##
##display(start)
##display(end)
