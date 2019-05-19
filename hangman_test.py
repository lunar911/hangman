import unittest
from hangman import has_player_won
from hangman import is_one_single_character
from hangman import only_characters_in_input


class TestHangman(unittest.TestCase):

    def test_has_player_won(self):
        self.assertTrue(has_player_won(["a", "b"], "ab"))
        self.assertTrue(has_player_won(["a", "b"], "abaa"))
        self.assertFalse(has_player_won(["a", "b"], "c"))
        self.assertFalse(has_player_won(["c"], "aba"))

    def test_is_one_single_letter(self):
        should_evaluate_to_true = ["a", "b", "c"]
        for element in should_evaluate_to_true:
            self.assertTrue(is_one_single_character(element))

        should_evaluate_to_false = ["aaa", "111", "!!!"]
        for element in should_evaluate_to_false:
            self.assertFalse(is_one_single_character(element))

    def test_only_characters_in_input(self):
        should_evaluate_to_true = ["aaa", "bbb", "ccc"]
        for element in should_evaluate_to_true:
            self.assertTrue(only_characters_in_input(element))

        should_evaluate_to_false = ["a1a", "111", "!!!"]
        for element in should_evaluate_to_false:
            self.assertFalse(only_characters_in_input(element))


if __name__ == "__main__":
    unittest.main()
