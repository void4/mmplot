import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names = "thm, steps, subtheorems_dup, totalsteps_dup, subtheorems, totalsteps, expandedsteps, maxpathlength".split(", ")
#"metamath-exe/out2.csv"
data = open("out20.csv").read().splitlines()
print("DA", data[1])
data = "\n".join(["\t".join([d for d in line.replace(",",":").split(":")[1::2]]) for line in data])

with open("new.csv", "w+") as f:
    f.write(data)

df = pd.read_csv("new.csv", sep="\t", header=None, names=names)#remove 1
print(df)

NSAMPLE = 1

df = df.sample(len(df)//NSAMPLE)

X = "maxpathlength"
Y = "expandedsteps"

XLOG = False
YLOG = True

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

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))

#label_point(df[X], df[Y], df.thm, ax)
#plt.savefig("figure.png")
plt.show()
