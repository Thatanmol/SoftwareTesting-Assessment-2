"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    """Track bowling rolls and calculate a ten-frame game score."""

    def __init__(self):
        """Create an empty bowling game."""
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """Record a valid roll with a pin count from 0 through 10."""
        if isinstance(pins, bool) or not isinstance(pins, int):
            raise TypeError("pins must be an integer")
        if not 0 <= pins <= 10:
            raise ValueError("pins must be between 0 and 10")
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """Return the score for the completed rolls using bowling rules."""
        score = 0
        frame_index = 0

        for frame in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        """Return whether the frame starts with a strike."""
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """Return whether the frame's first two rolls make a spare."""
        return (
            frame_index + 1 < len(self.rolls)
            and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
        )

    def _strike_bonus(self, frame_index):
        """Return the two bonus rolls following a strike."""
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """Return the bonus roll following a spare."""
        return self.rolls[frame_index + 2]