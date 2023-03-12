# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.min_power(1, 4)[0], 11)
        self.assertEqual(g.min_power(2, 4)[0], 10)
        self.assertEqual(g.min_power(3, 7), (14, [3, 2, 5, 7]))

    def test_network1(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.min_power(3,1), (4, [3, 4, 1]))

    def test_network2(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.min_power(1, 4)[0], 4)

if __name__ == '__main__':
    unittest.main()
