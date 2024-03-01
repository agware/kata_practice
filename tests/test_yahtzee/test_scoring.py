import pytest

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum
from kata_practice.yahtzee.score_turn import score_turn


@pytest.mark.parametrize("category", ScoreCategoriesEnum)
def test_all_score_categories_return_a_value(category: ScoreCategoriesEnum):
    dice_rolls = [1, 1, 1, 1, 1]
    result = score_turn(dice_rolls, category)
    assert result is not None
