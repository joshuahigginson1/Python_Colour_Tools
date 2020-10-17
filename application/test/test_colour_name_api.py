"""Task: Test the colour name API module."""

# Imports --------------------------------------------------------------

from modules.colour_name_api import retrieve_colour


# Functions ------------------------------------------------------------

def test_colour_name_api():
    """This function tests our colour name API."""

    red = retrieve_colour(255, 0, 0)
    assert red == "Red"

    green = retrieve_colour(0, 255, 0)
    assert green == "Green"

    blue = retrieve_colour(0, 0, 255)
    assert blue == "Blue"

    navy_blue = retrieve_colour(28, 116, 226)
    assert navy_blue == "Navy Blue"

