from enum import Enum


class ScoreCategoriesEnum(Enum):
    THREE_OF_A_KIND = "3 of a kind"
    FOUR_OF_A_KIND = "4 of a kind"
    FIVE_OF_A_KIND = "Yahtzee"
    SMALL_STRAIGHT = "Small straight"
    LARGE_STRAIGHT = "Large straight"
