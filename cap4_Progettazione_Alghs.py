
'''

#####Strategy Divide Et Impera

import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext
  #!sto usando su pc jdk23, che x pyspark è nuovo e da problemi.
wordlist = ['python','java','ottawa', 'ottawa', 'java', 'news']
wordsRDD = sc.parallelize(wordlist,4) #x convertire in struttura dati nativa di Spark (Resilient Distributed Dataset)
print(wordsRDD.collect())

wordPairs = wordsRDD.map(lambda w: (w,1))  #x comvertire in coppie key-value
print(wordPairs.collect())

wordCountsCollected = wordPairs.reduceByKey(lambda x,y: x+y)  #x aggregare e ottenere il result finale
print(wordCountsCollected.collect())
'''

'''
#####Strategy Brute Force x problema Commesso Viaggiatore

import random
from itertools import permutations
import matplotlib.pyplot as plt
from time import time
from collections import Counter

alltours = permutations
aCity = complex  # Un punto (città) sarà rappresentato come numero complesso

def distance_points(first, second):  #calc distanza assoluta tra 2 punti
    return abs(first - second)

def distance_tour(aTour):  #clac distanza totale per coprire un determinato percorsp
    return sum(distance_points(aTour[i - 1], aTour[i]) for i in range(len(aTour)))

def generate_cities(number_of_cities):  #genera casualmente un insieme di n citiesin rettangolo 500x300
    seed = 111
    width = 500
    height = 300
    random.seed(number_of_cities + seed)
    return frozenset(
        aCity(random.randint(1, width), random.randint(1, height))
        for c in range(number_of_cities)
    )

def brute_force(cities):
    return shortest_tour(alltours(cities))

def shortest_tour(tours):
    return min(tours, key=distance_tour)

def visualize_tour(tour, style='bo-'):  #traccia tutte le citta e collegamenti di un determinato percorso
    if len(tour) > 1000:
        plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')
    plt.show()

def visualize_segment(segment, style='bo-'):  #traccia le citta e i singoli collegamenti
    plt.plot([X(c) for c in segment],
             [Y(c) for c in segment],
             style,
             clip_on=False)
    plt.axis('scaled')
    plt.axis('off')

def X(city): return city.real
def Y(city): return city.imag

def tsp(algorithm, cities):  #generate path in base all'algh e al numero di citta richieste,cal il tempo dell'algh, genera un tracciato
    t0 = time()
    tour = algorithm(cities)
    t1 = time()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}: {} cities => tour length {:.0f} (in {:.3f} sec)".format(
        name(algorithm), len(tour), distance_tour(tour), t1 - t0))

def name(algorithm):
    return algorithm.__name__.replace('_tsp', '')

tsp(brute_force, generate_cities(10))  #max x 10-11 citta, xk complessita O(n!) (usa fattoriale)


#####Strategy Algh Greedy x problema Commesso Viaggiatore

def greedy_algorithm(cities, start=None):
    city_ = start or first(cities)
    tour = [city_]
    unvisited = set(cities - {city_})
    while unvisited:
        city_ = nearest_neighbor(city_, unvisited)
        tour.append(city_)
        unvisited.remove(city_)
    return tour

def first(collection):
    return next(iter(collection))

def nearest_neighbor(city_a, cities):
    return min(cities, key=lambda city_: distance_points(city_, city_a))

tsp(greedy_algorithm, generate_cities(200))  #O(n²) ma non garantisce il percorso ottimale
'''

'''
#####Algoritmo Page Rank (by larry page and sergey brin from Google)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Creazione grafo
my_web = nx.DiGraph()
my_pages = range(1, 6)  # includo anche il nodo 5
connections = [(1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 4), (4, 5), (5, 1), (5, 4)]
my_web.add_nodes_from(my_pages)
my_web.add_edges_from(connections)

# Disegno grafo
pos = nx.shell_layout(my_web)
nx.draw(my_web, pos, arrows=True, with_labels=True)
plt.show()

# Funzione per creare PageRank manualmente
def create_page_rank(a_graph):
    nodes_set = len(a_graph)
    M = nx.to_numpy_array(a_graph, dtype=float)  # matrice adiacenza
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))  # gradi uscenti
    prob_outwards = np.array([
        1.0 / count if count > 0 else 0.0
        for count in outwards
    ])
    G = np.asarray(np.multiply(M.T, prob_outwards))  # normalizzazione
    p = np.ones(nodes_set) / float(nodes_set)  # distribuzione iniziale uniforme
    return G, p

G, p = create_page_rank(my_web)
print("Matrice di transizione G:\n", G)
print("Vettore iniziale p:\n", p)
'''

#####Strategy Programmazione Lineare

import pulp

# Creazione modello
model = pulp.LpProblem("Profit_maximising_problem", pulp.LpMaximize)

# Variabili decisionali
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')

# Funzione obiettivo
model += 5000*A + 2500*B, "Profit"

# Vincoli
model += 3*A + 2*B <= 20
model += 4*A + 3*B <= 30
model += 4*A + 3*B <= 44

# Risoluzione
model.solve()

# Risultati
print("Status:", pulp.LpStatus[model.status])
print("A =", A.varValue)
print("B =", B.varValue)
print("Profitto massimo =", pulp.value(model.objective))


