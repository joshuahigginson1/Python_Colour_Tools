"""Task: Test the white_balance module."""

# Imports --------------------------------------------------------------

from modules.white_balance import clip_colours, auto_white_balance

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------

def test_clip_colours():

    # Test for Lower Bounds

    value = -4
    assert clip_colours(value) == 0

    # Test for Higher Bounds

    value = 340
    assert clip_colours(value) == 255

    # Test for Round

    value = 124.35
    assert clip_colours(value) == 124

# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
