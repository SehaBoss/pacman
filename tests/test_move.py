import pytest
import unittest
from unittest.mock import patch
from pacman import move_player

class test_move_pacman(unittest.TestCase):
    @patch('pacman.direction', 0)
    def test_move_right(self):
        assert move_player(450, 663) == (452, 663)

    @patch('pacman.direction', 1)
    def test_move_left(self):
        assert move_player(450, 663) == (448, 663)

    @patch('pacman.direction', 2)
    @patch('pacman.turns_allowed', [True, True, True, True])
    def test_move_up(self):
        assert move_player(450, 663) == (450, 661)

    @patch('pacman.direction', 3)
    @patch('pacman.turns_allowed', [True, True, True, True])
    def test_move_down(self):
        assert move_player(450, 663) == (450, 665)

    @patch('pacman.direction', 0)
    @patch('pacman.turns_allowed', [False, True, True, True])
    def test_move_right_negative(self):
        assert move_player(450, 663) == (450, 663)

    @patch('pacman.direction', 1)
    @patch('pacman.turns_allowed', [True, False, True, True])
    def test_move_left_negative(self):
        assert move_player(450, 663) == (450, 663)

    @patch('pacman.direction', 2)
    def test_move_up_negative(self):
        assert move_player(450, 663) == (450, 663)

    @patch('pacman.direction', 3)
    def test_move_down_negative(self):
        assert move_player(450, 663) == (450, 663)

