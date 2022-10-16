import numpy as np
import csv

class Graph_Creator:
    def __init__(self):
        self._Vsize = 50  # Number of vertices
        self._E = []  # Edges in the graph

    def _FindAllTheEdges(self):
        v = self._Vsize
        allTheEdges = list()
        for i in range(v):
            for j in range(i+1,v):
                allTheEdges.append([i,j])
        return allTheEdges

    def CreateGraphWithRandomEdges(self,Esize):  #Esize is the number of edges in the graph
        allTheEdges = self._FindAllTheEdges()
        edgeChoiceIndices = np.random.choice(len(allTheEdges),Esize,replace=False)
        edgeChoiceIndices.sort()
        #print(edgeChoiceIndices)
        self._E = [allTheEdges[i] for i in edgeChoiceIndices]
        #print(self._E)
        #print(len(self._E))
        return self._E

    def CreateCSVFileForRandomGraph(self,Esize):
        self.CreateGraphWithRandomEdges(Esize)
        fileName ="{0}.csv".format(Esize)
        with open(fileName, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self._E)
        
    def ReadGraphfromCSVfile(self,fileName):
        fileName ="{0}.csv".format(fileName)
        with open(fileName) as csvfile:
            rows = csv.reader(csvfile)
            rows = list(rows)
            self._E = [[int(i) for i in ro] for ro in rows]
        #print(self._E)
        return self._E
        
def main():
    graph = Graph_Creator()
    graph.CreateGraphWithRandomEdges(200) # Creates a random graph with 50 vertices and 200 edges
    graph.ReadGraphfromCSVfile("Testcases/50") # Reads the edges of the graph from a given CSV file
    
    

if __name__=='__main__':
    main()