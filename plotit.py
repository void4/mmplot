import pandas as pd
import matplotlib.pyplot as plt
from math import log

df = pd.read_csv("thmsteps.csv", sep="\t", header=None, names=["thm", "steps", "subtheorems", "totalsteps", "expandedsteps"])#remove 1
print(df)

ax = df.set_index("totalsteps")["subtheorems"].plot(style="o")

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))

label_point(df.totalsteps, df.subtheorems, df.thm, ax)
#plt.savefig("figure.png")
plt.show()
