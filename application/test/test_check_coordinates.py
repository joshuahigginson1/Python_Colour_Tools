"""Task: Test the check co-ordinates function."""

# Imports --------------------------------------------------------------

from modules.check_coordinates import check_coordinates

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------

def test_check_coordinates():
    """This function checks our 'test coordinates' function."""

    x_error = "X axis out of bounds error."
    y_error = "Y axis out of bounds error."
    xy_error = "X and Y axis out of bounds error."

    neg_error = "Negative coordinate not valid."

    expected_message = "No errors."

    image_size = (200, 200)

    out_of_bounds_x = [[0, 0], [0, 100], [300, 0], [300, 100]]
    out_of_bounds_y = [[0, 0], [0, 300], [100, 0], [100, 300]]
    out_of_bounds_xy = [[0, 0], [300, 300], [300, 0], [0, 300]]

    assert check_coordinates(image_size, out_of_bounds_x) == x_error
    assert check_coordinates(image_size, out_of_bounds_y) == y_error
    assert check_coordinates(image_size, out_of_bounds_xy) == xy_error

    negative_x = [[0, 0], [0, 100], [-100, 0], [-100, 100]]
    negative_y = [[0, 0], [0, -100], [100, 0], [100, -100]]
    negative_xy = [[0, 0], [0, 100], [100, 0], [-100, -100]]

    assert check_coordinates(image_size, negative_x) == neg_error
    assert check_coordinates(image_size, negative_y) == neg_error
    assert check_coordinates(image_size, negative_xy) == neg_error

    expected = [[0, 0], [0, 100], [100, 0], [100, 100]]

    assert check_coordinates(image_size, expected) == expected_message

# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
