#!/usr/local/bin/python3
# inventory.py
# contains functions for fantasy game inventory

def displayInventory(inv):
	output = "Inventory:\n"
	itemCount = 0
	#keys = List(inv.keys()).sort()
	for k in sorted(inv.keys()):
		output += "{val} {k}\n".format(val=inv[k], k = k)
		itemCount += inv[k]
	output += "\nTotal number of items: {count}\n".format(count = itemCount)
	return output

def addToInventory(inv, items):
	for item in items:
		inv[item] = inv[item] + 1 if item in inv.keys() else 1