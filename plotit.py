import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("thmsteps.csv", sep="\t", header=None, names=["thm", "steps", "subtheorems", "totalsteps", "expandedsteps"])#remove 1
print(df)

NSAMPLE = 20#1

df = df.sample(len(df)//NSAMPLE)

X = "expandedsteps"
Y = "subtheorems"

#df[Y] = [len(y) for y in df[Y]]
df[X] = np.log(df[X].astype("float"))
#df[Y] = np.log(df[Y].astype("float"))

ax = df.set_index(X)[Y].plot(style="o", markersize=1)

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))

#label_point(df[X], df[Y], df.thm, ax)
#plt.savefig("figure.png")
plt.show()
