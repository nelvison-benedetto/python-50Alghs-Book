
'''

#Strategy Divide Et Impera

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

#Strategy Brute Force x problema Commesso Viaggiatore

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

# Esecuzione
tsp(brute_force, generate_cities(10))



