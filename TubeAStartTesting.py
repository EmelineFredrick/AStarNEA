import unittest
import TubeAStar
import StationGraph
import csv

class TestHCost(unittest.TestCase):

    Example = {"13": ["Bank", [51.5133,-0.0886], [156, 2, 2], [250, 2, 2], [225, 13, 2], [157, 9, 2], [167, 9, 3], [279, 12, 4]],
               "156":["Liverpool Street", [51.5178,-0.0823], [13, 2, 2], [24, 2, 3], [14, 3], [2, 8, 2], [167, 6, 2]],
               "250":["St.Paul's", [51.5146,-0.0973], [13, 2, 2], [48, 2, 2]],
               "225":["Shadwell", [51.5117,-0.056], [13, 13, 2], [155, 13, 2], [262, 13, 2], [276, 5, 1], [295, 5, 2]],
               "157":["London Bridge", [51.5052,-0.0864], [23, 7, 3], [233, 7, 2], [13, 9, 2], [29, 9, 2]],
               "167":["Moorgate", [51.5186,-0.0886], [14, 3, 2], [156, 3, 2], [13, 9, 3], [188, 9, 1]],
               "188":["Old Street", [51.5263,-0.0873], [7, 9, 3], [167, 9, 1]],
               "7"  :["Angel", [51.5322,-0.1058], [188, 9, 3]]}

    # test to show entry in graph from files for 188 matches our example
    def testGraphLoadedCorrectly(self):
        graph = TubeAStar.getGraph()
        stationNode = graph["188"]
        self.assertEqual(stationNode[0], "Old Street")

    # test to show HCost works with real examples
    def testHCost(self):
        return

    # test to show Dist is longer than HCost for all neighbors

    # test to show we get the right answer for the simples case (Bank to Bank)
    def testBankToBank(self):
        result = TubeAStar.AStar("13", "13")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "13")
    
    # test to show we get the right answer for a simple case (Bank to Angel)
    def testBankToAngel(self):
        result = TubeAStar.AStar("13", "7")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "7")
        self.assertEqual(result[1], "188")
        self.assertEqual(result[2], "167")
        self.assertEqual(result[3], "13")

    #test for longer case (Clapham South to Paddington)
    def testClaphamSouthToPaddington(self):
        result = TubeAStar.AStar("56", "193")
        #print(result)
        graph = TubeAStar.getGraph()
        for station in result:
            stationData = graph.get(station)
            #print(stationData[0])

    def testForMap(self):
        nameToId = StationGraph.getNameToId()
        self.assertEqual(nameToId.get("Bank"), "13")
        self.assertEqual(nameToId.get("London Bridge"), "157")

    def testForCalculatingTime(self):
        result = TubeAStar.AStar("13", "7")
        totalTime = StationGraph.calculateTime(result)
        self.assertEqual(totalTime, 7)
        
        

if __name__ == '__main__':
    unittest.main()
