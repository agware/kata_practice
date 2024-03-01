from collections import Counter

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum

COMBO_SCORE_CATEGORIES = {
    ScoreCategoriesEnum.ACES,
    ScoreCategoriesEnum.TWOS,
    ScoreCategoriesEnum.THREES,
    ScoreCategoriesEnum.FOURS,
    ScoreCategoriesEnum.FIVES,
    ScoreCategoriesEnum.SIXES,
}


def score_any_combination(target: int, rolls: list[int]) -> int:
    counted_rolls = Counter(rolls)

    if target not in counted_rolls:
        return 0

    return target * counted_rolls[target]


def score_any_combination_category(category: ScoreCategoriesEnum, rolls: list[int]) -> int:
    if category not in COMBO_SCORE_CATEGORIES:
        raise ValueError(category)

    combo_target_map = {
        ScoreCategoriesEnum.ACES: 1,
        ScoreCategoriesEnum.TWOS: 2,
        ScoreCategoriesEnum.THREES: 3,
        ScoreCategoriesEnum.FOURS: 4,
        ScoreCategoriesEnum.FIVES: 5,
        ScoreCategoriesEnum.SIXES: 6,
    }
    target = combo_target_map[category]

    return score_any_combination(target, rolls)
