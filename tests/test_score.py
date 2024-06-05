import unittest
from unittest.mock import patch
from pacman import check_collisions

class test_orb_and_score(unittest.TestCase):
    @patch('pacman.level', [[1],[2]])
    @patch('pacman.HEIGHT', 164)
    @patch('pacman.WIDTH', 60)
    @patch('pacman.center_x', 1)
    @patch('pacman.center_y', 1)
    def test_small_orb(self):
        assert check_collisions(100, False, 0, [False,False,False,False]) == (110, False, 0, [False,False,False,False])

    @patch('pacman.level', [[1],[2]])
    @patch('pacman.HEIGHT', 164)
    @patch('pacman.WIDTH', 60)
    @patch('pacman.center_x', 1)
    @patch('pacman.center_y', 4)
    def test_bonus_orb(self):
        assert check_collisions(0, False, 666, [True,True,True,True]) == (50, True, 0, [False,False,False,False])