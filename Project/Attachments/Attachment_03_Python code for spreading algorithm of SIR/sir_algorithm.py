# Import required modules
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import kshell as k_s

from operator import itemgetter

# Check if there is any node left with degree d
import kshell


def is_infected(b):
    check = False
    random_no = np.random.random()
    if(random_no <= b):
        check = True
    return check

def sir_routine_single_seed(graph,seed_node,beta1, beta2):
    G = graph.copy()
    I = []
    R = []
    C = []
    I.append(seed_node)

#    print("Infected:", I)
#    print("Recovered:", R)
#    print("Neighbors:", C)

    while(len(I)>0):
        for selected_i in I:
#           print("Selected infected:", selected_i)
            if (selected_i == seed_node):
                beta = beta1
            else:
                beta = beta2
            I.remove(selected_i)
            R.append(selected_i)
            C = []
            for n in G[selected_i]:
#                print("n=",n)
                C.append(n)
#                print("sn=",C)
#            print("Infected:", I)
#            print("Recovered:", R)
#            print("Neighbors:", C)
            for a in I:
                if(a in C):
                    C.remove(a)
            for b in R:
                if(b in C):
                    C.remove(b)
#            print("Neighbors in loop:", C)
            while(len(C)>0):
                for selected_c in C:
#                    print("Selected Neighbor:", selected_c)
                    C.remove(selected_c)
#                    print("Infected:", I)
#                    print("Recovered:", R)
#                    print("Neighbors:", C)
                    if(is_infected(beta)):
#                        print(selected_c, "is infected")
                        I.append(selected_c)
#                    print("Infected:", I)
#                    print("Recovered:", R)
#                    print("Neighbors:", C)

#    print("Infected:", I)
#    print("Recovered:", R)
#    print("Neighbors:", C)
    recovery_ratio = float(len(R)) / float(G.number_of_nodes())
    return recovery_ratio
