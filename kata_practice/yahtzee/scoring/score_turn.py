from collections import Counter

from kata_practice.yahtzee.scoring.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.scoring.score_category_any_of_a_kind import (
    ANY_OF_A_KIND_SCORE_CATEGORY,
    score_any_of_a_kind_category,
)
from kata_practice.yahtzee.scoring.score_category_combos import COMBO_SCORE_CATEGORIES, score_any_combination_category
from kata_practice.yahtzee.scoring.score_category_straights import (
    STRAIGHT_SCORE_CATEGORIES,
    score_any_straight_category,
)


def has_full_house(rolls: list[int]) -> bool:
    """
    Defined as exactly 3 of one number and 2 of a different number
    """
    counted_rolls = Counter(rolls)

    has_three = 3 in counted_rolls.values()
    has_two = 2 in counted_rolls.values()

    return has_three and has_two


def score_turn(category: ScoreCategoriesEnum, rolls: list[int]) -> int:
    """Applies a scoring category to a set of rolls and returns the associated score"""
    if category in COMBO_SCORE_CATEGORIES:
        return score_any_combination_category(category, rolls)

    if category in ANY_OF_A_KIND_SCORE_CATEGORY:
        return score_any_of_a_kind_category(category, rolls)

    if category in STRAIGHT_SCORE_CATEGORIES:
        return score_any_straight_category(category, rolls)

    if category == ScoreCategoriesEnum.FULL_HOUSE:
        return 25 if has_full_house(rolls) else 0

    if category == ScoreCategoriesEnum.CHANCE:
        return sum(rolls)

    raise NotImplementedError(category)
