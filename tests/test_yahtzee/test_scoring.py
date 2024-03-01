from typing import List

import pytest

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.score_turn import has_straight, score_any_of_a_kind, score_turn


@pytest.mark.parametrize("category", ScoreCategoriesEnum)
def test_all_score_categories_return_a_value(category: ScoreCategoriesEnum):
    dice_rolls = [1, 1, 1, 1, 1]
    result = score_turn(dice_rolls, category)
    assert result is not None


@pytest.mark.parametrize(
    ("category", "expected"),
    (
        (ScoreCategoriesEnum.THREE_OF_A_KIND, 15),
        (ScoreCategoriesEnum.FOUR_OF_A_KIND, 20),
        (ScoreCategoriesEnum.FIVE_OF_A_KIND, 50),
    ),
)
def test_score_turn_with_any_of_a_kind(category: ScoreCategoriesEnum, expected: int):
    dice_rolls = [5, 5, 5, 5, 5]
    result = score_turn(dice_rolls, category)
    assert result == expected


@pytest.mark.parametrize(
    ("dice_rolls", "target", "expected"),
    (
        ([1, 2, 3, 4, 5, 6, 7], 2, 0),
        ([2, 4, 2, 4, 2], 2, 4),
        ([2, 4, 2, 4, 2], 3, 6),
        ([2, 4, 2, 4, 2], 4, 0),
        ([6, 6, 6, 5, 6, 5], 4, 24),
        ([6, 6, 6, 5, 6, 5], 5, 0),
        ([-1, -1, -1, -1, 10, 10], 1, -1),
        ([-1, -1, -1, -1, 10, 10], 2, -2),
    ),
)
def test_score_any_of_a_kind(dice_rolls: list[int], target: int, expected: int):
    assert score_any_of_a_kind(dice_rolls, target) == expected


def test_score_any_of_a_kind_with_default():
    default_score = 100
    result = score_any_of_a_kind([-5, -5, 22, -5], target=2, default_score=default_score)
    assert result == default_score


@pytest.mark.xfail(reason="Logic not implemented yet")
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
def test_has_straight(rolls: List[int], target: int, expected: bool):
    assert has_straight(rolls, target) == expected
