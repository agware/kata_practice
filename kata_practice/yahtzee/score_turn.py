from collections import Counter
from typing import Callable, List, Optional

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum


def score_turn(rolls: List[int], category: ScoreCategoriesEnum) -> int:
    """Applies a scoring category to a set of rolls and returns the associated score"""
    counted_rolls = Counter(rolls)
    return get_scoring_method(category)(counted_rolls)


def get_scoring_method(category: ScoreCategoriesEnum) -> Callable[[Counter], int]:
    """A factory method to match a given scoring category to its method for scoring"""

    if category == ScoreCategoriesEnum.THREE_OF_A_KIND:
        return score_3_of_a_kind
    elif category == ScoreCategoriesEnum.FOUR_OF_A_KIND:
        return score_4_of_a_kind
    elif category == ScoreCategoriesEnum.FIVE_OF_A_KIND:
        return score_5_of_a_kind
    else:
        raise NotImplementedError


def score_3_of_a_kind(counted_rolls: Counter) -> int:
    return score_any_of_a_kind(counted_rolls, target=3)


def score_4_of_a_kind(counted_rolls: Counter) -> int:
    return score_any_of_a_kind(counted_rolls, target=4)


def score_5_of_a_kind(counted_rolls: Counter) -> int:
    return score_any_of_a_kind(counted_rolls, target=5, default_score=50)


def score_any_of_a_kind(
    counted_rolls: Counter, target: int, default_score: Optional[int] = None
) -> int:
    """
    Checks whether there is a set of matching die values occuring at or more frequently than the target.
    It will always use the most frequently occurring die value for the calculation
    """
    die_value, highest_count = counted_rolls.most_common()[0]

    if highest_count < target:
        return 0

    if default_score is not None:
        return default_score

    return die_value * target
