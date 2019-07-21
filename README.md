# MMplot

Plots Metamath theorem statistics

Examples:

Number of proof steps vs number of subtheorems:

![Figure_1.png](images/Figure_1.png)

Number of total (deduplicated) proof steps vs number of subtheorems:

![Figure_2.png](images/Figure_2.png)

Number of the log of expanded (including duplicate) proof steps vs number of subtheorems:

![Figure_6.png](images/Figure_6.png)


Maximum path length (proof depth) vs number of subtheorems

![maxpathlengths_vs_subtheorems.png](images/maxpathlengths_vs_subtheorems.png)

Proof depth vs expanded steps

![maxpl_vs_logexpsteps.png](images/maxpl_vs_logexpsteps.png)

## Install

`pip install -r requirements.txt`

## Plot
`python plotit.py`

## Update data

This is only necessary to update the data which is included in this repository!

This step may take > 1 hour

```
cd metamath && gcc m*.c -O3 -o metamath && ./metamath set.mm > out2.csv
show trace_back * /essential /count_steps
exit
```
Can't tell when it exits this way, maybe `tee` it.
TODO new format
