#Homework: reproduce computation of ml and web degree of nodes either in R or Python (libraries you can use are e.g. igraph or NetworX)
import os
import time
from urllib.request import urlopen
import zipfile
import pandas as pd
import networkx
file_name = "git_web_ml.zip"
link = "https://snap.stanford.edu/data/git_web_ml.zip"

print(os.getcwd())
if not os.path.isfile(file_name):
    print("Downloading data from web")
    with urlopen(link) as content, open(file_name, "wb") as file:
        file.write(content.read())
if not os.path.isdir(file_name):
    print("Directory Found. Unpacking file")
    with zipfile.ZipFile(file_name, 'r') as zip:
        zip.extractall("")
print("Data available")

print("Data Loading")
edges = pd.read_csv("git_web_ml/musae_git_edges.csv")
clas = pd.read_csv("git_web_ml/musae_git_target.csv")

print("Creating graph")
graph = networkx.Graph()
graph.add_nodes_from(clas["id"])
for index, row in edges.iterrows():
    graph.add_edge(row["id_1"],row["id_2"])

start_time = time.time() #Count execution time
deg_ml = [0]*len(clas)
deg_web = [0]*len(clas)
ml_target = clas["ml_target"].tolist()

for edge in graph.edges():
    edge_source, edge_destination = edge[0], edge[1]
    if ml_target[edge_destination] == 1:
        deg_ml[edge_source] = 1
    else:
        deg_web[edge_source] = 1

    if ml_target[edge_source] == 1:
        deg_ml[edge_destination] = 1
    else:
        deg_web[edge_destination] = 1

end_time = time.time()
print("Execution time : %s"%(end_time-start_time))