import sys
from pathlib import Path

jfile = Path('./data/default.jrn')
print('-'*40 + "\n")
print("\t\tJOURNAL APP")
print('-'*40 + "\n")

journal = []

if jfile.is_file():
	count = 0
	print("... loading journal from ./data/default.jrn ...")
	with open(jfile) as jf:
		for entry in jf.readlines():
			journal.append(entry.strip())
			count += 1
	print("... loaded {c} journal entries ...".format(c=count))

def list_entries():
	count = 1
	for item in journal:
		print(str(count) +".\t"+item)
		count += 1

while True:
	choice = input("What do you want to do? [L]ist, [A]dd, or E[x]it: ")
	if choice.upper() == "L":
		list_entries()
	if choice.upper() == "A":
		entry = input("Enter your journal entry:\n")
		journal.append(entry)
	if choice.upper() == "X":
		break

print("... saving journal to ./data/default.jrn ...")
count = 0
with open(jfile, 'w') as jf:
	for entry in journal:
		jf.write(entry + "\n")
		count += 1
print("... saved {c} journal entries ...".format(c=count))