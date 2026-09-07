import unittest

from bowling_game import BowlingGame


class BowlingGameTests(unittest.TestCase):
    def play(self, rolls):
        game = BowlingGame()
        for pins in rolls:
            game.roll(pins)
        return game

    def test_gutter_game(self):
        self.assertEqual(self.play([0] * 20).score(), 0)

    def test_all_ones(self):
        self.assertEqual(self.play([1] * 20).score(), 20)

    def test_all_twos(self):
        self.assertEqual(self.play([2] * 20).score(), 40)

    def test_regular_game(self):
        rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1, 7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
        self.assertEqual(self.play(rolls).score(), 72)

    def test_single_spare(self):
        self.assertEqual(self.play([5, 5, 3] + [0] * 17).score(), 16)

    def test_single_strike(self):
        self.assertEqual(self.play([10, 3, 4] + [0] * 16).score(), 24)

    def test_two_consecutive_spares(self):
        self.assertEqual(self.play([5, 5, 5, 5, 2] + [0] * 15).score(), 29)

    def test_two_consecutive_strikes(self):
        self.assertEqual(self.play([10, 10, 3, 4] + [0] * 14).score(), 47)

    def test_all_spares(self):
        self.assertEqual(self.play([5] * 21).score(), 150)

    def test_perfect_game(self):
        self.assertEqual(self.play([10] * 12).score(), 300)

    def test_tenth_frame_open(self):
        self.assertEqual(self.play([0] * 18 + [4, 5]).score(), 9)

    def test_tenth_frame_spare_with_bonus(self):
        self.assertEqual(self.play([0] * 18 + [7, 3, 6]).score(), 16)

    def test_tenth_frame_strike_with_two_bonuses(self):
        self.assertEqual(self.play([0] * 18 + [10, 4, 5]).score(), 19)

    def test_sample_game(self):
        rolls = [10, 3, 6, 5, 5, 8, 1, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
        self.assertEqual(self.play(rolls).score(), 190)

    def test_roll_count(self):
        game = self.play([1, 2, 3])
        self.assertEqual(game.current_roll, 3)
        self.assertEqual(game.rolls, [1, 2, 3])
        for invalid_pins in (-1, 11):
            with self.subTest(invalid_pins=invalid_pins):
                with self.assertRaises(ValueError):
                    game.roll(invalid_pins)
        for invalid_pins in ("5", 5.0, True):
            with self.subTest(invalid_pins=invalid_pins):
                with self.assertRaises(TypeError):
                    game.roll(invalid_pins)

    def test_zero_score_open_frames(self):
        self.assertEqual(self.play([0, 0] * 10).score(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)