from operator import indexOf
from Graph_Creator import *
import random
import time
start = time.time()
PERIOD_OF_TIME = 45


        
def main():
    gc = Graph_Creator()
    #edges = gc.CreateGraphWithRandomEdges(500)  # Creates a random graph with 50 vertices and 200 edges
    edges = gc.ReadGraphfromCSVfile("Testcases/200") # Reads the edges of the graph from a given CSV file
#Initializing population
    population = []
    for i in range(100):
        population.append([random.randint(0,2) for i in range(50)])
    
    print("Roll no : 2020A7PS1394G")
    print("Number of edges : ",len(edges))
    print("Best state :")

#Genetic Algorithm
    def Genetic_Algorithm(population,weights):
        population2 = []  
        #sort population 
        population.sort(key=lambda x: CalculateFitness(x,edges),reverse=True)
        for m in range(20):
            population2.append(population[m])  
        for i in range(len(population) - 20):
            parent1, parent2 = random.choices(population, weights=weights, k=2)
            child = Crossover(parent1,parent2)
            if random.random() < 0.1:
                child = Mutation(child)
            population2.append(child)
        return population2

    for z in range(10000):
        fitness = []
        for i in range(len(population)):
            fitness.append(CalculateFitness(population[i],edges))

        weights = []
        for k in range(len(population)):
            weights.append(fitness[k]/sum(fitness))

        population = Genetic_Algorithm(population,weights)
        best = [population[indexOf(fitness,max(fitness))]]

        if(time.time() - start > PERIOD_OF_TIME or max(fitness) == 50):
            break
    #print the best population corresponding to the maximum fitness
    dic = {0:"R",1:"G",2:"B"}
    for x in range(50):
        print("{}:{}".format(x, dic[best[0][x]]),end=", " if x < 49 else "")
    print()
    print("Fitness value of best state : ",max(fitness))
    print("Time taken : ",time.time() - start)
    



#Calculating fitness of each state in population
def CalculateFitness(state,edges):
    unfits = set()
    for edge in edges:
        if state[edge[0]] == state[edge[1]]:
            unfits.add(edge[0])
            unfits.add(edge[1])
    return 50 - len(unfits)

#Crossover
def Crossover(parent1,parent2):
    k = random.randint(0,49)
    child = []
    child = parent1[:k] + parent2[k:]
    return child

#Mutation
def Mutation(child):
    for i in range(50):
        if random.random() < 0.1:
            child[i] = random.randint(0,2)
    return child

if __name__=='__main__':
    main()
