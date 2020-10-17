"""Task: This file executes our application."""

# Imports --------------------------------------------------------------

from modules.average_colour import ave_colour_from_selection
from modules.white_balance import auto_white_balance

import numpy
from skimage import io

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------

IMAGE_PATH = "test/test_image.png"

# Execute Code ---------------------------------------------------------

image = io.imread(IMAGE_PATH)

# First, we find the average colour of our white sheet of paper.

# Our four co-ordinates, read 'backwards'.: [[x,y], [x,y], [x,y], [x,y]]

WHITE_COORDS = [[56, 234], [56, 256], [76, 234], [76, 256]]
white_selection = numpy.array(WHITE_COORDS)

ave_white_value = ave_colour_from_selection(image, white_selection).tolist()

# Now, find the colour we want to sample.

COLOUR_COORDS = [[0, 52], [52, 0], [75, 52], [52, 75]]
colour_selection = numpy.array(COLOUR_COORDS)

ave_colour_value = ave_colour_from_selection(image, colour_selection).tolist()

print(f"The average white value is: {ave_white_value}")
print(f"The average colour value is: {ave_colour_value}")

# Run our white balance tool.

output = auto_white_balance(ave_colour_value, ave_white_value)

print(f"The colour corrected value is: {output}")

