# Import required modules
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from operator import itemgetter


def kdict(klist,G):
    for i in klist:
        for j in i[1]:
            G.nodes[j]['kshell']  = i[0]
            G.nodes[j]['nshell'] = i[0]
            G.nodes[j]['degree']  = G.degree(j)

def find_nk(G):
    for i in list(G.nodes):
        no_neighbors = len(list(G.neighbors(i)))
        for n in list(G.neighbors(i)):
            calc_nshell = math.log(no_neighbors/G.degree(n))*G.nodes[i]['kshell']
            if (calc_nshell > G.nodes[n]['nshell']):
                G.nodes[n]['nshell']= calc_nshell

# Check if there is any node left with degree d
def check(h, d):
    f = 0  # there is no node of deg <= d
    for i in h.nodes():
        if (h.degree(i) <= d):
            f = 1
            break
    return f

# Find list of nodes with particular degree
def find_nodes(h, it):
    set1 = []
    for i in h.nodes():
        if (h.degree(i) <= it):
            set1.append(i)
    return set1


def remove_self_cyles(G):
    for i in G.edges:
        if (i[0] == i[1]):
            G.remove_edge(i[0], i[1])


def find_k_shell(h):
    # Copy the graph
    H = h.copy()
    remove_self_cyles(H)
    it = 1

    # Bucket being filled currently
    tmp = []

    # list of lists of buckets
    buckets = []
    while (1):
        flag = check(H, it)
        if (flag == 0):
            buckets.append((it, tmp))
            it += 1
            tmp = []
        if (flag == 1):
            node_set = find_nodes(H, it)
            for each in node_set:
                H.remove_node(each)
                tmp.append(each)
        if (H.number_of_nodes() == 0):
            buckets.append((it, tmp))
            break
    return buckets


def list_k_shells(k_shell_list):
    for i in k_shell_list:
        print("k-shell:", i[0], "-", len(i[1]))
