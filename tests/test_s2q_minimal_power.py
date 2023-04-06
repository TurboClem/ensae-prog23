# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import *
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        g = kruskal(graph_from_file("input/network.00.in"))
        self.assertEqual(new_min_power(*g, 1, 4), 11)
        self.assertEqual(new_min_power(*g, 2, 4), 10)
        self.assertEqual(new_min_power(*g, 3, 7), (14))

    def test_network1(self):
        g = kruskal(graph_from_file("input/network.02.in"))
        self.assertEqual(new_min_power(*g, 3,1), (4))

    def test_network2(self):
        g = kruskal(graph_from_file("input/network.04.in"))
        self.assertEqual(new_min_power(*g, 1, 4), 4)

if __name__ == '__main__':
    unittest.main()
