import unittest
from maze import Maze
from graphs import Window


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 12
        win = Window(1080,720)
        m1 = Maze(0,0, num_rows, num_cols, 10, win)
        m1.create_cells()
        self.assertEqual(
                len(m1.get_cells()),
                num_cols
                )
        
        self.assertEqual(
                len(m1.get_cells()[0]),
                num_rows
                )

if __name__ == "__main__":
    unittest.main()

