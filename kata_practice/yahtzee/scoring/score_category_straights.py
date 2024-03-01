from kata_practice.yahtzee.scoring.score_categories import ScoreCategoriesEnum

STRAIGHT_SCORE_CATEGORIES = {ScoreCategoriesEnum.SMALL_STRAIGHT, ScoreCategoriesEnum.LARGE_STRAIGHT}


def has_straight(target: int, rolls: list[int]) -> bool:
    unique_rolls = list(set(rolls))
    unique_rolls.sort()

    prev_value = None
    current_straight = 0
    for die_value in unique_rolls:
        if prev_value is not None and prev_value + 1 != die_value:
            # break in the chain has occurred
            current_straight = 0
        else:
            current_straight += 1
            if current_straight >= target:
                return True

        prev_value = die_value

    return False


def score_any_straight_category(category: ScoreCategoriesEnum, rolls: list[int]) -> int:
    if category not in STRAIGHT_SCORE_CATEGORIES:
        raise ValueError(category)

    straight_target_map = {
        ScoreCategoriesEnum.SMALL_STRAIGHT: 4,
        ScoreCategoriesEnum.LARGE_STRAIGHT: 5,
    }
    target = straight_target_map[category]

    if not has_straight(target, rolls):
        return 0

    return 30 if category == ScoreCategoriesEnum.SMALL_STRAIGHT else 40
