import pytest

from kata_practice.yahtzee.scoring.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.scoring.score_category_any_of_a_kind import (
    ANY_OF_A_KIND_SCORE_CATEGORY,
    score_any_of_a_kind,
    score_any_of_a_kind_category,
)


def test_score_any_of_a_kind_raises_error():
    with pytest.raises(ValueError):
        score_any_of_a_kind_category(ScoreCategoriesEnum.ACES, [])


@pytest.mark.parametrize("category", ANY_OF_A_KIND_SCORE_CATEGORY)
def test_score_any_of_a_kind_no_match_with_category(category: ScoreCategoriesEnum):
    dice_rolls = [1, 2, 3, 4, 5]
    result = score_any_of_a_kind_category(category, dice_rolls)
    assert result == 0


@pytest.mark.parametrize(
    ("category", "expected"),
    (
        (ScoreCategoriesEnum.THREE_OF_A_KIND, 15),
        (ScoreCategoriesEnum.FOUR_OF_A_KIND, 20),
        (ScoreCategoriesEnum.FIVE_OF_A_KIND, 50),
    ),
)
def test_score_any_of_a_kind_with_category(category: ScoreCategoriesEnum, expected: int):
    dice_rolls = [5, 5, 5, 5, 5]
    result = score_any_of_a_kind_category(category, dice_rolls)
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
    assert score_any_of_a_kind(target, dice_rolls) == expected
