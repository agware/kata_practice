from typing import List

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum


def score_turn(rolls: List[int], category: ScoreCategoriesEnum) -> int:
    assert len(rolls) == 5, "Expecting exactly 5 dice to have been rolled"
    return 0
