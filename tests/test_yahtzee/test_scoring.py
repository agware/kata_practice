from typing import List

import pytest

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.score_turn import score_turn


@pytest.mark.xfail(
    reason="Scoring methods haven't been implemented for all categories yet"
)
@pytest.mark.parametrize("category", ScoreCategoriesEnum)
def test_all_score_categories_return_a_value(category: ScoreCategoriesEnum):
    dice_rolls = [1, 1, 1, 1, 1]
    result = score_turn(dice_rolls, category)
    assert result is not None


@pytest.mark.parametrize(
    ("dice_rolls", "expected_score"),
    (
        ([1, 2, 3, 4, 5, 6, 7], 0),
        ([2, 3, 2, 3, 5], 0),
        ([1, 1, 1], 3),
        ([-2, 1, -2, -2], -6),
        ([6, 6, 6, 5, 6, 5], 18),
        ([5, 5, 5, 5, 5], 15),
    ),
)
def test_score_3_of_a_kind(dice_rolls: List[int], expected_score: int):
    result = score_turn(dice_rolls, ScoreCategoriesEnum.THREE_OF_A_KIND)
    assert result == expected_score


@pytest.mark.parametrize(
    ("dice_rolls", "expected_score"),
    (
        ([1, 2, 3, 4, 5, 6, 7], 0),
        ([2, 3, 2, 3, 2], 0),
        ([1, 1, 1, 1], 4),
        ([2, 1, 2, 2, 2], 8),
        ([6, 6, 6, 5, 6, 5], 24),
        ([5, 5, 5, 5, 5], 20),
    ),
)
def test_score_4_of_a_kind(dice_rolls: List[int], expected_score: int):
    result = score_turn(dice_rolls, ScoreCategoriesEnum.FOUR_OF_A_KIND)
    assert result == expected_score


@pytest.mark.parametrize(
    ("dice_rolls", "expected_score"),
    (
        ([1, 2, 3, 4, 5, 6, 7], 0),
        ([2, 3, 2, 3, 2], 0),
        ([6, 6, 6, 5, 6, 5], 0),
        ([5, 5, 5, 5, 5], 50),
        ([4, 4, 4, 4, 4], 50),
    ),
)
def test_score_5_of_a_kind(dice_rolls: List[int], expected_score: int):
    result = score_turn(dice_rolls, ScoreCategoriesEnum.FIVE_OF_A_KIND)
    assert result == expected_score
