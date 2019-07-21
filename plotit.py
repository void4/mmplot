import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names = "thm, steps, subtheorems_dup, totalsteps_dup, subtheorems, totalsteps, expandedsteps, maxpathlength".split(", ")

df = pd.read_csv("thmstats.csv", sep="\t", header=None, names=names)#remove 1
print(df)

NSAMPLE = 20#1

df = df.sample(len(df)//NSAMPLE)

X = "expandedsteps"
Y = "subtheorems"

XLOG = True
YLOG = False

#df[Y] = [len(y) for y in df[Y]]
if XLOG:
    df[X] = np.log(df[X].astype("float"))

if YLOG:
    df[Y] = np.log(df[Y].astype("float"))

ax = df.set_index(X)[Y].plot(style="o", markersize=1)

xlabel = "log(%s)" % X if XLOG else X
ylabel = "log(%s)" % Y if YLOG else Y

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))

#label_point(df[X], df[Y], df.thm, ax)
#plt.savefig("figure.png")
plt.show()
