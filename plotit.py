import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time
import sys

DPI = 96
WIDTH = 1920
HEIGHT = 1080

plt.figure(figsize=(WIDTH/DPI, HEIGHT/DPI), dpi=DPI)

names = "thm, steps, subtheorems_dup, totalsteps_dup, subtheorems, totalsteps, expandedsteps, maxpathlength".split(", ")
#"metamath-exe/out2.csv"
data = open("thmstats.csv").read().splitlines()
print("DA", data[1])
data = "\n".join(["\t".join([d for d in line.replace(",",":").split(":")[1::2]]) for line in data])

with open("new.csv", "w+") as f:
    f.write(data)

df = pd.read_csv("new.csv", sep="\t", header=None, names=names)#remove 1
print(df)

plt.title("Metamath's set.mm: %i proofs plotted" % len(df))

NSAMPLE = 100

df = df.sample(len(df)//NSAMPLE)

X = "expandedsteps"
Y = "subtheorems"

XLOG = True
YLOG = False

df[X] = df[X].astype("float")
df[Y] = df[Y].astype("float")

#df[Y] = [len(y) for y in df[Y]]
if XLOG:
    df[X] = np.log(df[X])

if YLOG:
    df[Y] = np.log(df[Y])

ax = df.set_index(X)[Y].plot(style="o", markersize=1)

xlabel = "log(%s)" % X if XLOG else X
ylabel = "log(%s)" % Y if YLOG else Y

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

d = {}

with open("proof_with_comments.txt") as pc:
    for line in pc.read().splitlines():
        line = line.split(";")
        d[line[0]] = " ".join(line[1:])

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        text = str(point['val'])
        if text in d:
            text += " "+d[text]
        ax.text(point['x'], point['y'], text)

label_point(df[X], df[Y], df.thm, ax)

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "%i.png" % int(time())
plt.savefig("images/"+name, dpi=DPI)
plt.show()
