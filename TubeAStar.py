Module: TubeAStar.py

#NEXT STEP: TODO GRAPH <-----------


# graph format
# key = station identifier
# value = array of data
# value[0] = coordinates of station, latitude & longitude
# value[n] = neighbor key value

testGraph = {'a': [[1,1],'b', 'c'],
             'b': [[3,1],'a'],
             'c': [[2,2],'d',],
             'd': [[4,5],'c', 'e'],
             'e': [[1,3],'b', 'd']}

# TODO (graph):
# decide new graph format (including actual times)
# adjust testGraph to new format 
# build graph from london.connections.csv
# implement Dist using new graph

# TODO (HCost):
# reimplement HCost using haversine formula
# https://www.movable-type.co.uk/scripts/latlong.html

# from london.stations.csv
# min latitude: 51.4022
# max latitude: 51.7052
# min longitude:-0.0021
# max longitude: 0.251

#Next step is set up HCost properly
def AStar (StartKey, EndKey, graph):
    ClosedSet = set()
    OpenSet = set(StartKey)

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
        Neighbours = stuff[1:]

        for Neighbour in Neighbours:
            if Neighbour in ClosedSet:
                continue
            if Neighbour not in OpenSet:
                OpenSet.add(Neighbour)
            PossGScore = gScore.get(Current) + Dist(Current, Neighbour)
            if Neighbour in gScore:
                if PossGScore >= gScore.get(Neighbour):
                    continue

            CameFrom[Neighbour] = Current
            gScore[Neighbour] = PossGScore
            fScore[Neighbour] = gScore[Neighbour] + HCost(graph.get(Neighbour), graph.get(EndKey))

    return False

#When gScore doesn't have a value for neighbour
##gTest = {'c': 100}
##default = "1000000"
##print(gTest['c'])
##val = 'd'
##if val in gTest:
##    print(gTest[val])
##else:
##    print(default)
##
##x = set()
##x.add("hello")
##print(x)

def Recon (CameFrom, Current):
    TotalPath = [Current]
    while Current in CameFrom:
        Current = CameFrom[Current]
        TotalPath.append(Current)
    return TotalPath

def Dist (Current, Neighbour):
#The actual distance eg. time
    return 10
        
def HCost (From, To):
#heuristic score (in minutes) is not the actual cost
    return 1

def FindCurrent (OpenSet, fScore):
    working = OpenSet.copy()
    current = working.pop()
    while len(working) > 0:
        nextCandidate = working.pop()
        if fScore[nextCandidate] < fScore[current]:
            current = nextCandidate
    return current            
    
#TheSet = set(["a", "b", "c", "d"])
#TheScores = {"a": 5, "b": 4, "c": 2, "d": 6}
#print(FindCurrent(TheSet, TheScores))



#Tube Line files from: https://github.com/nicola/tubemaps/tree/master/datasets
                         
