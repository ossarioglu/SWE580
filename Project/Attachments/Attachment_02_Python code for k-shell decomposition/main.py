# Import required modules
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import kshell as k_s
import sir_algorithm as sir
from datetime import datetime


def run_sir(listed_k, times, prob):
    recovery_array = []
    for t in range(len(listed_k)):
        k_core_values = listed_k[t][1]
        #    print(k_core_values)
        for i in k_core_values:
            temp_array = []
            for tc in range(times):
                temp_array.append(sir.sir_routine_single_seed(G, i, prob, prob))
            recovery_array.append([i, temp_array])

    print("After SIR Operation =", datetime.now())
    return recovery_array

def run_sir(listed_k, times, prob1, prob2):
    recovery_array = []
    for i in listed_k:
        temp_array = []
        for tc in range(times):
            temp_array.append(sir.sir_routine_single_seed(G, i, prob1, prob2))
        recovery_array.append([i, temp_array])

    print("After SIR Operation =", datetime.now())
    return recovery_array


def summarize_sir_results(recovery_array):
    ratio_summary = []
    for i in recovery_array:
        temp_sum = 0.0
        temp_average = 0.0
        for nname in i[1]:
            temp_sum = temp_sum + nname
        temp_average = temp_sum / len(i[1])
        ratio_summary.append(
            [i[0], G.degree(i[0]), G.nodes[i[0]]['betweenness'], G.nodes[i[0]]['kshell'], temp_average])
    print("FINISH =", datetime.now())
    return ratio_summary

def export_results(summary_data,all_data, summary_array, all_array):
    tofile = open(summary_data, "w")
    tofile.write(str(summary_array) + "\n")
    for element in summary_array:
        tofile.write(str(element) + "\n")
    tofile.close()
    tofile = open(all_data, "w")
    tofile.write(str(all_array) + "\n")
    for element in all_array:
        tofile.write(str(element) + "\n")
    tofile.close()


# datetime object containing current date and time
now = datetime.now()
print("Start =", now)

# Create graph object and add nodes

# G_IMDB = nx.read_edgelist(
#    'C:\\Users\\Osman Selcuk Sariogl\\Desktop\\BOUN\\SWE580\\Project\\Network_Data\\IMDB\\IMDB.edges')

G_gen = nx.read_edgelist(
    'C:\\Users\\Osman Selcuk Sariogl\\Desktop\\BOUN\\SWE580\\Project\\Network_Data\\IMDB\\G6-1000-105.edges')

G = G_gen

bc = nx.betweenness_centrality(G)
nx.set_node_attributes(G, bc, "betweenness")

k_list = k_s.find_k_shell(G)
k_dict = k_s.kdict(k_list,G)
k_s.find_nk(G)

k_s.list_k_shells(k_list)

n_shell_list = []
for i in list(G.nodes()):
    n_shell_list.append([i,G.nodes[i]['nshell']])

query_nshell = []
for i in n_shell_list:
    if (i[1] > 300):
        query_nshell.append(i[0])

print(query_nshell)


print("After K-Shell Operation =", datetime.now())

#recovery_array = run_sir(k_list,100, 0.01)
#ratio_summary = summarize_sir_results(recovery_array)

recovery_array2 = run_sir(query_nshell, 25, 0.5, 0.005)
ratio_summary = summarize_sir_results(recovery_array2)
export_results("summary-data.txt","all-data.txt", ratio_summary, recovery_array2 )


#nx.draw(G, with_labels= True)
#plt.show()
