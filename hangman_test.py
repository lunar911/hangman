import unittest
from hangman import has_player_won


class TestHangman(unittest.TestCase):

    def test_has_player_won(self):
        self.assertTrue(has_player_won(["a", "b"], "ab"))
        self.assertTrue(has_player_won(["a", "b"], "abaa"))
        self.assertFalse(has_player_won(["a", "b"], "c"))
        self.assertFalse(has_player_won(["c"], "aba"))


if __name__ == "__main__":
    unittest.main()
