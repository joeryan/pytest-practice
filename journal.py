import sys


print('-'*40 + "\n")
print("\t\tJOURNAL APP")
print('-'*40 + "\n")

journal = []

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
