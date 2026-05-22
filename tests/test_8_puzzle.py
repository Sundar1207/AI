import unittest
from importlib.util import spec_from_file_location, module_from_spec
import os
import sys

# Load the script
script_path = os.path.join(os.path.dirname(__file__), '..', '8 puzzle problem.py')
spec = spec_from_file_location('puzzle8', script_path)
puzzle8 = module_from_spec(spec)
sys.modules['puzzle8'] = puzzle8
spec.loader.exec_module(puzzle8)

class Test8Puzzle(unittest.TestCase):
    def test_solve_8_puzzle(self):
        start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        path = puzzle8.solve_8_puzzle(start, goal)
        self.assertEqual(path, ['Down', 'Right'])

if __name__ == '__main__':
    unittest.main()
