from collections import Counter

from kata_practice.yahtzee.scoring.score_categories import ScoreCategoriesEnum


def score_any_combination(target: int, rolls: list[int]) -> int:
    counted_rolls = Counter(rolls)

    if target not in counted_rolls:
        return 0

    return target * counted_rolls[target]


def score_any_combination_category(category: ScoreCategoriesEnum, rolls: list[int]) -> int:
    combo_target_map = {
        ScoreCategoriesEnum.ACES: 1,
        ScoreCategoriesEnum.TWOS: 2,
        ScoreCategoriesEnum.THREES: 3,
        ScoreCategoriesEnum.FOURS: 4,
        ScoreCategoriesEnum.FIVES: 5,
        ScoreCategoriesEnum.SIXES: 6,
    }

    if category not in combo_target_map:
        raise ValueError(category)

    target = combo_target_map[category]
    return score_any_combination(target, rolls)
