with open("proof_with_comments.txt") as f:
    lines = f.read().splitlines()

def node(a,g):
    return {"id":a, "group":g}

def edge(a,b):
    return {"source":a, "target":b}#, "value":1}

nodes = []
edges = []

for line in lines[:1000]:
    line = line.split(";")
    if len(line) < 2:
        continue
    nodes.append(node(line[0], 0))
    for e in line[1:]:
        nodes.append(node(e, 1))
        edges.append(edge(line[0], e))

graph = {"nodes":nodes, "links":edges}

import json

with open("graph.json", "w+") as f:
    f.write(json.dumps(graph))
