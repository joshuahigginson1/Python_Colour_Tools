"""Task: This file executes our application."""

# Imports --------------------------------------------------------------

from modules.average_colour import ave_colour_from_selection

import numpy
import skimage

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------

IMAGE_PATH = "test/white.png"

# Execute Code ---------------------------------------------------------

image = skimage.io.imread(IMAGE_PATH)


# First, we find the average colour of our white sheet of paper.

WHITE_COORDS = [[0, 0], [1, 0], [1, 1], [0, 1]]
white_selection = numpy.array(WHITE_COORDS)

ave_white_value = ave_colour_from_selection(image, white_selection)

# Run our white balance tool.
