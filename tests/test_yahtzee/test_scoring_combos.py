import pytest

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.score_category_combos import (
    COMBO_SCORE_CATEGORIES,
    score_any_combination,
    score_any_combination_category,
)


def test_score_any_combination_raises_error():
    with pytest.raises(ValueError):
        score_any_combination_category(ScoreCategoriesEnum.THREE_OF_A_KIND, [])


@pytest.mark.parametrize("category", COMBO_SCORE_CATEGORIES)
def test_score_any_combination_no_match_with_category(category: ScoreCategoriesEnum):
    dice_rolls = [7, 7, 7, 7, 7]
    result = score_any_combination_category(category, dice_rolls)
    assert result == 0


@pytest.mark.parametrize(
    ("category", "target"),
    (
        (ScoreCategoriesEnum.ACES, 1),
        (ScoreCategoriesEnum.TWOS, 2),
        (ScoreCategoriesEnum.THREES, 3),
        (ScoreCategoriesEnum.FOURS, 4),
        (ScoreCategoriesEnum.FIVES, 5),
        (ScoreCategoriesEnum.SIXES, 6),
    ),
)
def test_score_any_of_a_kind_with_category(category: ScoreCategoriesEnum, target: int):
    num_matches = 4
    dice_rolls = [-3] + [target] * num_matches + [99, 7, 20]
    result = score_any_combination_category(category, dice_rolls)
    assert result == num_matches * target


@pytest.mark.parametrize(
    ("dice_rolls", "target", "expected"),
    (
        ([1, 2, 3, 4, 5, 6, 7], 2, 2),
        ([2, 4, 2, 4, 2], 2, 6),
        ([2, 4, 2, 4, 2], 4, 8),
        ([2, 4, 2, 4, 2], 3, 0),
        ([6, 6, 6, 5, 6, 5], 6, 24),
        ([6, 6, 6, 5, 6, 5], 5, 10),
        ([-1, -1, -1, -1, 10, 10], -1, -4),
        ([-1, -1, -1, -1, 10, 10], 10, 20),
    ),
)
def test_score_any_of_a_kind(dice_rolls: list[int], target: int, expected: int):
    assert score_any_combination(target, dice_rolls) == expected
