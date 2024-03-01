import pytest

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.score_turn import has_full_house, score_turn


@pytest.mark.parametrize("category", ScoreCategoriesEnum)
def test_all_score_categories_return_a_value(category: ScoreCategoriesEnum):
    dice_rolls = [1, 1, 1, 1, 1]
    result = score_turn(category, dice_rolls)
    assert result is not None


@pytest.mark.parametrize(
    ("category", "dice_rolls", "expected"),
    (
        (ScoreCategoriesEnum.ACES, [1, 2, 1, 1], 3),
        (ScoreCategoriesEnum.TWOS, [2, 3, 3], 2),
        (ScoreCategoriesEnum.THREES, [3, 3, 1, 3, 3], 12),
        (ScoreCategoriesEnum.FOURS, [5, 5, 4, 3], 4),
        (ScoreCategoriesEnum.FIVES, [2, 3, 4, 5], 5),
        (ScoreCategoriesEnum.SIXES, [6, 6, 6, 7], 18),
        (ScoreCategoriesEnum.THREE_OF_A_KIND, [2, 2, 2], 6),
        (ScoreCategoriesEnum.FOUR_OF_A_KIND, [4, 6, 4, 4, 4, 4], 16),
        (ScoreCategoriesEnum.FIVE_OF_A_KIND, [5, 5, 5, 5, 5], 50),
        (ScoreCategoriesEnum.SMALL_STRAIGHT, [1, 2, 3, 4], 30),
        (ScoreCategoriesEnum.LARGE_STRAIGHT, [1, 2, 3, 4, 5], 40),
        (ScoreCategoriesEnum.FULL_HOUSE, [2, 2, 3, 3, 3], 25),
        (ScoreCategoriesEnum.CHANCE, [1, 2, 3, 4, 5], 15),
    ),
)
def test_all_score_categories(category: ScoreCategoriesEnum, dice_rolls: list[int], expected: int):
    assert score_turn(category, dice_rolls) == expected


@pytest.mark.parametrize(
    ("dice_rolls", "expected"),
    (
        ([1, 2, 3, 1, 2], False),
        ([5, 3, 3, 5, 5], True),
        ([1, 1, 1, 1, 2, 2], False),
        ([2, 2, 2, 3, 3, 3], False),
        ([1, 1, 1, 6, 7, 4, 4], True),
    ),
)
def test_has_full_house(dice_rolls: list[int], expected: bool):
    assert has_full_house(dice_rolls) == expected


@pytest.mark.parametrize(
    "dice_rolls",
    (
        [1, 2, 3, 4, 5],
        [6, 7, 9, 10, 22, -5, 7],
        [7, 2, 3, 4, 1, 3],
        [1, 2],
    ),
)
def test_scoring_chance(dice_rolls: list[int]):
    assert score_turn(ScoreCategoriesEnum.CHANCE, dice_rolls) == sum(dice_rolls)
