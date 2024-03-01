import pytest

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.score_category_straights import (
    STRAIGHT_SCORE_CATEGORIES,
    has_straight,
    score_any_straight_category,
)


def test_score_any_combination_raises_error():
    with pytest.raises(NotImplementedError):
        score_any_straight_category(ScoreCategoriesEnum.CHANCE, [])


@pytest.mark.parametrize("category", STRAIGHT_SCORE_CATEGORIES)
def test_score_turn_with_straight_no_match(category: ScoreCategoriesEnum):
    dice_rolls = [1, 1, 1, 1, 1]
    result = score_any_straight_category(category, dice_rolls)
    assert result == 0


@pytest.mark.parametrize(
    ("category", "expected"),
    (
        (ScoreCategoriesEnum.SMALL_STRAIGHT, 30),
        (ScoreCategoriesEnum.LARGE_STRAIGHT, 40),
    ),
)
def test_score_turn_with_straight(category: ScoreCategoriesEnum, expected: int):
    dice_rolls = [1, 2, 3, 4, 5]
    result = score_any_straight_category(category, dice_rolls)
    assert result == expected


@pytest.mark.parametrize(
    ("rolls", "target", "expected"),
    (
        ([1, 2, 3, 4], 2, True),
        ([1, 2, 3, 4], 3, True),
        ([1, 2, 3, 4], 4, True),
        ([1, 2, 3, 4], 5, False),
        ([7, 6, 3, 4, 2, 5, 10], 5, True),
        ([9, 5, 2, 3, 4, 8, 11], 5, False),
    ),
)
def test_has_straight(rolls: list[int], target: int, expected: bool):
    assert has_straight(target, rolls) == expected
