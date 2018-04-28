#Module: TubeAStar.py
import StationGraph
import math

# graph format
# key = station identifier
# value = array of data
#{"ID" : ["Station Name", [latitude, longitude], [neighbour ID, connection line, time to neighbour]]}

Example = {"13": ["Bank", [51.5133,-0.0886], [156, 2, 2], [250, 2, 2], [225, 13, 2], [157, 9, 2], [167, 9, 3], [279, 12, 4]],
           "156":["Liverpool Street", [51.5178,-0.0823], [13, 2, 2], [24, 2, 3], [14, 3], [2, 8, 2], [167, 6, 2]],
           "250":["St.Paul's", [51.5146,-0.0973], [13, 2, 2], [48, 2, 2]],
           "225":["Shadwell", [51.5117,-0.056], [13, 13, 2], [155, 13, 2], [262, 13, 2], [276, 5, 1], [295, 5, 2]],
           "157":["London Bridge", [51.5052,-0.0864], [23, 7, 3], [233, 7, 2], [13, 9, 2], [29, 9, 2]],
           "167":["Moorgate", [51.5186,-0.0886], [14, 3, 2], [156, 3, 2], [13, 9, 3], [188, 9, 1]],
           "188":["Old Street", [51.5263,-0.0873], [7, 9, 3], [167, 9, 1]],
           "7"  :["Angel", [51.5322,-0.1058], [188, 9, 3]]}

def getGraph():
    return StationGraph.getGraph()

def AStar (StartKey, EndKey):
    graph = getGraph()
    ClosedSet = set()
    OpenSet = set()
    OpenSet.add(StartKey)
    CameFrom = {}

    gScore = {}
    gScore[StartKey] = 0

    fScore = {}
    fScore[StartKey] = HCost(graph.get(StartKey), graph.get(EndKey))

    while len(OpenSet) > 0:
        Current = FindCurrent(OpenSet, fScore)
        if Current == EndKey:
            return Recon(CameFrom, Current)

        OpenSet.discard(Current)
        ClosedSet.add(Current)

        stuff = graph.get(Current)
        NeighbourEntries = stuff[2:]
        Neighbours = []
        for entry in NeighbourEntries:
            Neighbours.append(entry[0])

        for Neighbour in Neighbours:
            if Neighbour in ClosedSet:
                continue
            if Neighbour not in OpenSet:
                OpenSet.add(Neighbour)
            PossGScore = gScore.get(Current) + Dist(Current, Neighbour, graph)
            if Neighbour in gScore:
                if PossGScore >= gScore.get(Neighbour):
                    continue

            CameFrom[Neighbour] = Current
            gScore[Neighbour] = PossGScore
            fScore[Neighbour] = gScore[Neighbour] + HCost(graph.get(Neighbour), graph.get(EndKey))

    return False

def Recon (CameFrom, Current):
    TotalPath = [Current]
    while Current in CameFrom:
        Current = CameFrom[Current]
        TotalPath.append(Current)
    return TotalPath

#The actual distance eg. time    
def Dist (Current, Neighbour, graph):
    currentNode = graph.get(Current)
    for x in currentNode[2::]:
        if str(x[0]) == Neighbour:
            return x[2]
    print("problem! could not find neighbour in current node: " + currentNode[0] + ", " + Neighbour)
        
def HCost (From, To):
     #X is longitude
    x1 = From[1][1]
    x2 = To[1][1]

   #Y is latitude
    y1 = From[1][0]
    y2 = To[1][0]

    #deltaX is equal to the metres difference along the E/W axis between current and end
    deltaX = (x2-x1)*111320*math.cos(math.radians(y2))
    #deltaY is equal to the metres difference along the N/S axis
    deltaY = (y2-y1)*110574

    Distance = (deltaX**2 + deltaY**2)**0.5

    # max tube speed in meters per minute (Met line : 65 mph)
    Velocity = 1743.456
    Time = Distance / Velocity
    return Time

def FindCurrent (OpenSet, fScore):
    working = OpenSet.copy()
    current = working.pop()
    while len(working) > 0:
        nextCandidate = working.pop()
        if fScore[nextCandidate] < fScore[current]:
            current = nextCandidate
    return current

    
    



#Tube Line files from: https://github.com/nicola/tubemaps/tree/master/datasets
                         
