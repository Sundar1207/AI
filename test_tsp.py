import unittest
from TSP import traveling_salesman

class TestTSP(unittest.TestCase):
    def test_traveling_salesman(self):
        graph = {
            'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
            'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
            'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
            'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
        }
        path, cost = traveling_salesman(graph, 'A')
        self.assertEqual(path, ['A', 'B', 'D', 'C', 'A'])
        self.assertEqual(cost, 80)

    def test_larger_graph(self):
        graph = {
            'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20, 'E': 25, 'F': 30, 'G': 35, 'H': 40, 'I': 45},
            'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25, 'E': 30, 'F': 20, 'G': 15, 'H': 10, 'I': 5},
            'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30, 'E': 25, 'F': 40, 'G': 45, 'H': 50, 'I': 55},
            'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0, 'E': 10, 'F': 15, 'G': 20, 'H': 25, 'I': 30},
            'E': {'A': 25, 'B': 30, 'C': 25, 'D': 10, 'E': 0, 'F': 5, 'G': 10, 'H': 15, 'I': 20},
            'F': {'A': 30, 'B': 20, 'C': 40, 'D': 15, 'E': 5, 'F': 0, 'G': 5, 'H': 10, 'I': 15},
            'G': {'A': 35, 'B': 15, 'C': 45, 'D': 20, 'E': 10, 'F': 5, 'G': 0, 'H': 5, 'I': 10},
            'H': {'A': 40, 'B': 10, 'C': 50, 'D': 25, 'E': 15, 'F': 10, 'G': 5, 'H': 0, 'I': 5},
            'I': {'A': 45, 'B': 5, 'C': 55, 'D': 30, 'E': 20, 'F': 15, 'G': 10, 'H': 5, 'I': 0}
        }
        path, cost = traveling_salesman(graph, 'A')
        self.assertEqual(path, ['A', 'B', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'A'])
        self.assertEqual(cost, 90)

    def test_single_node(self):
        graph = {'A': {'A': 0}}
        path, cost = traveling_salesman(graph, 'A')
        self.assertEqual(path, ['A', 'A'])
        self.assertEqual(cost, 0)

if __name__ == '__main__':
    unittest.main()
