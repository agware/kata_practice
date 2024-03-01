from enum import Enum


class ScoreCategoriesEnum(Enum):
    ACES = "Aces"
    TWOS = "Twos"
    THREES = "Threes"
    FOURS = "Fours"
    FIVES = "Fives"
    SIXES = "Sixes"
    THREE_OF_A_KIND = "3 of a kind"
    FOUR_OF_A_KIND = "4 of a kind"
    FIVE_OF_A_KIND = "Yahtzee"
    SMALL_STRAIGHT = "Small straight"
    LARGE_STRAIGHT = "Large straight"
    FULL_HOUSE = "Full house"
    CHANCE = "Chance"
