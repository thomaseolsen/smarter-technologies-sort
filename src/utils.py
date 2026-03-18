# Ideally these are env vars and can be modified without code changes
BULKY_DIMENSION_THRESHOLD = 150
BULKY_VOLUME_THRESHOLD = 1000000
HEAVY_MASS_THRESHOLD = 20


def sort(width: int, height: int, length: int, mass: float) -> str:
    """
    Sorts an item based on its dimensions and mass.

    Inputs:
        - width: The width of the item in centimeters
        - height: The height of the item in centimeters
        - length: The length of the item in centimeters
        - mass: The mass of the item in kilograms

    Returns:
        - "STANDARD" if the item is neither bulky nor heavy
        - "SPECIAL" if the item is either bulky or heavy
        - "REJECTED" if the item is both bulky and heavy

    Raises:
        - ValueError: If any of the dimensions or mass are negative
    """
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative")

    volume = width * height * length
    is_bulky = (
        volume >= BULKY_VOLUME_THRESHOLD
        or max(width, height, length) >= BULKY_DIMENSION_THRESHOLD
    )
    is_heavy = mass >= HEAVY_MASS_THRESHOLD

    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"
