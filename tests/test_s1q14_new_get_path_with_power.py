# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import *

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(get_path(g,1,3), ([1, 2, 3], 4))

    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(get_path(g,1,4), ([1, 4], 4))

if __name__ == '__main__':
    unittest.main()