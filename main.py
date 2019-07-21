import pexpect
import sys

m = pexpect.spawn("./metamath set.mm")
m.expect(".\nMM> ")
m.expect(".\nMM> ")

theorems = open("prooflabels.txt").read().splitlines()

START = 0

for i, thm in enumerate(theorems[START:]):

	sys.stderr.write("%i/%i\n" % (i, len(theorems)-START))

	if not thm:
		continue

	m.sendline("show trace_back %s /essential /count_steps" % thm)

	index = m.expect([".\nMM> ", "to scroll to end"])
	r = m.before
	if index == 1:
		m.sendline("q")
		m.expect("MM> ")


	try:
		r = r.decode("ascii").split()
		#for i,w in enumerate(r):
		#	print(i,w)

		steps = r[10]
		subtheorems_dup = r[18]
		totalsteps_dup = r[29]
		subtheorems = r[45]
		totalsteps = r[57]
		expandedsteps = r[63]
		print("\t".join([str(x) for x in [thm, steps, subtheorems, totalsteps, expandedsteps]]))
	except IndexError as e:
		print(e)
		print(r)
		continue
