# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_with_power(1,3,11), [1, 4, 3])

    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.get_path_with_power(1,4,11), [1, 4])

if __name__ == '__main__':
    unittest.main()
