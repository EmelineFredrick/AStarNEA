import unittest
import TubeAStar

class TestHCost(unittest.TestCase):
    def testHCost(self):
        graph = TubeAStar.testGraph
        print(TubeAStar.AStar('a', 'e', graph) )
        
        aNode = graph.get('a')
        dNode = graph.get('d')
        print(aNode)
        self.assertEqual(TubeAStar.HCost(aNode, dNode), 5)


unittest.main()                        

TestingFile = open("london.stations.csv", "r+")
array = []
Graph = {}
y = 0
for x in TestingFile:
    array.append(TestingFile.readline(y))
    y += 1

print(array)
    


TestingFile.close()
