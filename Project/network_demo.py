import networkx as nx
import mathplotlib.pyplot as plt
import pandas as pd
import numpy as np

G = nx.barabasi_albert_graph(100,2)
nx.draw_spring(G);
