"""Task: This module finds the average colour of a polygon selection."""

# Imports --------------------------------------------------------------
from skimage import draw
import numpy


# Functions ------------------------------------------------------------

def ave_colour_from_selection(image, poly):
    """
    Credit to user Malibuoooo from StackOverflow.
    :param image: Our image file.
    :param poly: Numpy array of coordinates in which we are averaging.
    :return: Returns the average colour within our polygon.
    """

    # Generates a list of pixels that match in our polygon.

    pixels = image[draw.polygon(poly[:, 1], poly[:, 0])]

    # Use the channels of each pixel to get averages and convert them to ints.
    channels = numpy.average(pixels, 0).astype(int)

    # Return the average colour of every pixel.

    return numpy.average(pixels, 0).astype(int)
