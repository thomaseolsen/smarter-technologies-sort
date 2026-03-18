import pytest

from utils import sort


@pytest.mark.parametrize(
    "width, height, length, mass, expected",
    [
        (10, 10, 10, 10, "STANDARD"),  # Standard
        (100, 100, 100, 10, "SPECIAL"),  # Special (bulky)
        (10, 10, 10, 20, "SPECIAL"),  # Special (heavy)
        (100, 100, 100, 20, "REJECTED"),  # Rejected
        (0, 0, 0, 0, "STANDARD"),  # Edge cases
        (10, 10, 10, 19.9, "STANDARD"),  # Edge case just below heavy threshold
        (100, 100, 100, 10, "SPECIAL"),  # Edge case just below bulky threshold
    ],
)
def test_sort(width: int, height: int, length: int, mass: float, expected: str):
    assert sort(width, height, length, mass) == expected


@pytest.mark.parametrize(
    "width, height, length, mass",
    [
        (-1, 10, 10, 10),  # Negative width
        (10, -1, 10, 10),  # Negative height
        (10, 10, -1, 10),  # Negative length
        (10, 10, 10, -1),  # Negative mass
    ],
)
def test_sort_invalid_inputs(width: int, height: int, length: int, mass: float):
    with pytest.raises(ValueError):
        sort(width, height, length, mass)
