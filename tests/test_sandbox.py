import pytest

from .context import kata_practice


@pytest.mark.parametrize(
    ("first_number", "second_number"),
    (
        (5, 10),
        (-2, 100),
        (99999, 11),
        (-999, -7777),
    ),
)
def test_add(first_number: int, second_number: int) -> None:
    result = kata_practice.add(first_number, second_number)
    assert result == first_number + second_number
