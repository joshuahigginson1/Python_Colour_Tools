"""Task: This module checks the coordinates of our polygons to ensure they fit."""

# Imports --------------------------------------------------------------


# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------

def check_coordinates(image_size, coordinates):

    for coordinate in coordinates:

        if coordinate[0] > image_size[0] and coordinate[1] > image_size[1]:
            return "X and Y axis out of bounds error."

        if coordinate[0] > image_size[0]:
            return "X axis out of bounds error."

        if coordinate[1] > image_size[1]:
            return "Y axis out of bounds error."

        for point in coordinate:
            if point < 0:
                return "Negative coordinate not valid."

        # TODO: Check to see if the value provided is a rectangle.

    return "No errors."

# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
