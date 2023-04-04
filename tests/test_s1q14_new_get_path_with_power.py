# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import *

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.1.in")
        self.assertEqual(get_path(*kruskal(g), 10, 5), [10, 16, 7, 14, 1, 5])

    def test_network2(self):
        g = graph_from_file("input/network.4.in")
        self.assertEqual(get_path(*kruskal(g), 1, 2), [])

if __name__ == '__main__':
    unittest.main()