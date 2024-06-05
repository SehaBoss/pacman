import pytest
import unittest
from unittest.mock import patch
from pacman import get_targets

class test_target(unittest.TestCase):
    @patch('pacman.player_x', 400)
    @patch('pacman.player_y', 400)
    @patch('pacman.powerup', True)
    @patch('pacman.red.dead', False)
    @patch('pacman.blue.dead', False)
    @patch('pacman.pink.dead', False)
    @patch('pacman.orange.dead', False)
    @patch('pacman.eaten_ghost', [False,False,False,False])
    def test_run_away(self):
        assert get_targets(0,0,0,0,0,0,0,0) == [(900,900),(900,400),(400,900),(450,450)]

    @patch('pacman.player_x', 500)
    @patch('pacman.player_y', 500)
    @patch('pacman.powerup', True)
    @patch('pacman.red.dead', False)
    @patch('pacman.blue.dead', False)
    @patch('pacman.pink.dead', False)
    @patch('pacman.orange.dead', False)
    @patch('pacman.eaten_ghost', [True,True,True,True])
    def test_eaten_in_box(self):
        assert get_targets(400,400,400,400,400,400,400,400) == [(400, 100),(400, 100),(400, 100),(400, 100)]

    @patch('pacman.player_x', 500)
    @patch('pacman.player_y', 500)
    @patch('pacman.powerup', True)
    @patch('pacman.red.dead', False)
    @patch('pacman.blue.dead', False)
    @patch('pacman.pink.dead', False)
    @patch('pacman.orange.dead', False)
    @patch('pacman.eaten_ghost', [True,True,True,True])
    def test_eaten_not_in_box(self):
        assert get_targets(300,300,300,300,300,300,300,300) == [(500, 500),(500, 500),(500, 500),(500, 500)]

    @patch('pacman.player_x', 400)
    @patch('pacman.player_y', 400)
    @patch('pacman.powerup', True)
    @patch('pacman.red.dead', True)
    @patch('pacman.blue.dead', True)
    @patch('pacman.pink.dead', True)
    @patch('pacman.orange.dead', True)
    @patch('pacman.eaten_ghost', [True,True,True,True])
    def test_return(self):
        assert get_targets(0,0,0,0,0,0,0,0) == [(380, 400),(380, 400),(380, 400),(380, 400)]

    @patch('pacman.player_x', 400)
    @patch('pacman.player_y', 400)
    @patch('pacman.powerup', False)
    @patch('pacman.red.dead', False)
    @patch('pacman.blue.dead', False)
    @patch('pacman.pink.dead', False)
    @patch('pacman.orange.dead', False)
    def test_not_powerup_in_box(self):
        assert get_targets(400,400,400,400,400,400,400,400) == [(400, 100),(400, 100),(400, 100),(400, 100)]

    @patch('pacman.player_x', 500)
    @patch('pacman.player_y', 500)
    @patch('pacman.powerup', False)
    @patch('pacman.red.dead', False)
    @patch('pacman.blue.dead', False)
    @patch('pacman.pink.dead', False)
    @patch('pacman.orange.dead', False)
    def test_not_powerup_not_in_box(self):
        assert get_targets(300,300,300,300,300,300,300,300) == [(500, 500),(500, 500),(500, 500),(500, 500)]

    @patch('pacman.player_x', 400)
    @patch('pacman.player_y', 400)
    @patch('pacman.powerup', True)
    @patch('pacman.red.dead', True)
    @patch('pacman.blue.dead', True)
    @patch('pacman.pink.dead', True)
    @patch('pacman.orange.dead', True)
    def test_dead_not_powerup(self):
        assert get_targets(0,0,0,0,0,0,0,0) == [(380, 400),(380, 400),(380, 400),(380, 400)]

if __name__ == "__main__":
    pytest.main()   