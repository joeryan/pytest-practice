#!/usr/local/bin/python3
# tests for the fantasy game inventory practice project in
# Automate the Boring Stuff
import pytest

import inventory as inv

@pytest.fixture
def baseInv():
	return {'arrow': 12, 
	'dagger': 1,
	'gold coin': 2}


class TestDispalyInventory():
	def test_empty_inventory(self):
		expected = "Inventory:\n\nTotal number of items: 0\n"
		actual = inv.displayInventory({})
		assert expected == actual

	def test_one_item_inventory(self):
		expected = "Inventory:\n12 arrow\n\nTotal number of items: 12\n"
		actual = inv.displayInventory({'arrow': 12})
		assert expected == actual

	def test_multiple_item_inventory(self):
		expected = """\
Inventory:
12 arrow
1 dagger
42 gold coin
1 rope
6 torch

Total number of items: 62
"""
		testInv = {'arrow': 12, 
					'rope': 1,
					'torch': 6,
					'dagger': 1,
					'gold coin': 42}
		actual = inv.displayInventory(testInv)
		assert expected == actual

class TestaddToInventory():

	def test_add_empty_hoard_to_inventory(self):
		hoard = []
		testInv = baseInv()
		expected = """\
Inventory:
12 arrow
1 dagger
2 gold coin

Total number of items: 15
"""
		inv.addToInventory(testInv, hoard)
		actual = inv.displayInventory(testInv)
		assert expected == actual

	def test_add_single_item_hoard_to_inventory(self):
		hoard = ['necklace']
		testInv = baseInv()
		expected = """\
Inventory:
12 arrow
1 dagger
2 gold coin
1 necklace

Total number of items: 16
"""
		inv.addToInventory(testInv, hoard)
		actual = inv.displayInventory(testInv)
		assert expected == actual	

	def test_add_multiple_item_hoard_to_inventory(self):
		hoard = ['necklace', 'gold coin', 'gold coin']
		testInv = baseInv()
		expected = """\
Inventory:
12 arrow
1 dagger
4 gold coin
1 necklace

Total number of items: 18
"""
		inv.addToInventory(testInv, hoard)
		actual = inv.displayInventory(testInv)
		assert expected == actual	