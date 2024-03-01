from collections import Counter
from typing import Callable

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum


def has_straight(rolls: list[int], target: int) -> bool:
    return True


def score_small_straight(rolls: list[int]) -> int:
    return 30 if has_straight(rolls, target=4) else 0


def score_large_straight(rolls: list[int]) -> int:
    return 40 if has_straight(rolls, target=5) else 0


def score_any_of_a_kind(rolls: list[int], target: int, default_score: int | None = None) -> int:
    """
    Checks whether there is a set of matching die values occuring at or more frequently than the target.
    It will always use the most frequently occurring die value for the calculation
    """
    counted_rolls = Counter(rolls)
    die_value, highest_count = counted_rolls.most_common()[0]

    if highest_count < target:
        return 0

    if default_score is not None:
        return default_score

    return die_value * target


def score_3_of_a_kind(rolls: list[int]) -> int:
    return score_any_of_a_kind(rolls, target=3)


def score_4_of_a_kind(rolls: list[int]) -> int:
    return score_any_of_a_kind(rolls, target=4)


def score_5_of_a_kind(rolls: list[int]) -> int:
    return score_any_of_a_kind(rolls, target=5, default_score=50)


def get_scoring_method(category: ScoreCategoriesEnum) -> Callable[[list[int]], int]:
    """A factory method to match a given scoring category to its method for scoring"""

    if category == ScoreCategoriesEnum.THREE_OF_A_KIND:
        return score_3_of_a_kind
    elif category == ScoreCategoriesEnum.FOUR_OF_A_KIND:
        return score_4_of_a_kind
    elif category == ScoreCategoriesEnum.FIVE_OF_A_KIND:
        return score_5_of_a_kind
    elif category == ScoreCategoriesEnum.SMALL_STRAIGHT:
        return score_small_straight
    elif category == ScoreCategoriesEnum.LARGE_STRAIGHT:
        return score_large_straight
    else:
        raise NotImplementedError


def score_turn(rolls: list[int], category: ScoreCategoriesEnum) -> int:
    """Applies a scoring category to a set of rolls and returns the associated score"""
    return get_scoring_method(category)(rolls)
