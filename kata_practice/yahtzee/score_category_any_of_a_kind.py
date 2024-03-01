from collections import Counter

from kata_practice.yahtzee.score_categories import ScoreCategoriesEnum

ANY_OF_A_KIND_SCORE_CATEGORY = {
    ScoreCategoriesEnum.THREE_OF_A_KIND,
    ScoreCategoriesEnum.FOUR_OF_A_KIND,
    ScoreCategoriesEnum.FIVE_OF_A_KIND,
}


def score_any_of_a_kind(target: int, rolls: list[int]) -> int:
    """
    Checks whether there is a set of matching die values occuring at or more frequently than the target.
    It will always use the most frequently occurring die value for the calculation
    """
    counted_rolls = Counter(rolls)
    die_value, highest_count = counted_rolls.most_common()[0]

    if highest_count < target:
        return 0

    return die_value * target


def score_any_of_a_kind_category(category: ScoreCategoriesEnum, rolls: list[int]) -> int:
    if category not in ANY_OF_A_KIND_SCORE_CATEGORY:
        raise NotImplementedError

    any_of_a_kind_target_map = {
        ScoreCategoriesEnum.THREE_OF_A_KIND: 3,
        ScoreCategoriesEnum.FOUR_OF_A_KIND: 4,
        ScoreCategoriesEnum.FIVE_OF_A_KIND: 5,
    }

    target = any_of_a_kind_target_map[category]
    score = score_any_of_a_kind(target, rolls)

    # need to manage the edge case where Yahtzee comes with a default score
    if category == ScoreCategoriesEnum.FIVE_OF_A_KIND and score > 0:
        score = 50

    return score
