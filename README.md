# MMplot

Plots Metamath theorem statistics

Examples:

Number of proof steps vs number of subtheorems:

![Figure_1.png](Figure_1.png)

Number of total (deduplicated) proof steps vs number of subtheorems:

![Figure_2.png](Figure_2.png)

Number of the log of expanded (including duplicate) proof steps vs number of subtheorems:

![Figure_6.png](Figure_6.png)


Maximum path length (proof depth) vs number of subtheorems

![maxpathlengths_vs_subtheorems.png](maxpathlengths_vs_subtheorems.png)

Proof depth vs expanded steps

![maxpl_vs_logexpsteps.png](maxpl_vs_logexpsteps.png)

## Install

`pip install -r requirements.txt`

## Plot
`python plotit.py`

## Update data

This is only necessary to update the data which is included in this repository!

Collect all proof labels

`python print_prooflabels_mmverify.py > prooflabels.txt`

This next step may take > 1 hours

`python thmstats.py > thmsteps.csv`

Or, to append to existing file:

`python thmstats.py >> thmsteps.csv`
