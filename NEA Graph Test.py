graph = {'a': [[1,1],'b', 'c'],
         'b': [[3,1],'a', 'e'],
         'c': [[2,2],'d',],
         'd': [[4,2],'c', 'e'],
         'e': [[1,3],'b', 'd']}

StartNode = "a"
EndNode = "e"

def Distance(graph):
    return("here")
Open = []
Closed = []
FoundStart = False
FoundRoute = False
CurrentNode = 'None'

Open.append(StartNode)
Current_Node = StartNode
while Open != []:
    print("Step 1")
    for key in graph:
        if key == Current_Node:
            print(graph[Current_Node])
            FoundStart = True
            
        else:
            print (key)

    if FoundStart == False:
        print("Start not found")
    else:
        if CurrentNode == EndNode:
            FoundRoute = True
        break
    break
