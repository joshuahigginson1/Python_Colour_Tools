"""Task: This module sorts out auto white balance for our picture."""


# Functions ------------------------------------------------------------

def auto_white_balance(colour, white):
    luminance = (white[0] + white[1] + white[2]) / 3

    print(luminance)

    colour[0] = clip_colours(colour[0] * luminance / white[0])
    colour[1] = clip_colours(colour[1] * luminance / white[1])
    colour[2] = clip_colours(colour[2] * luminance / white[2])

    return colour


def clip_colours(value):
    if value <= 0:

        # Value of 0 is absolute black and cannot go lower.
        value = 0

    elif value >= 255:

        # Value of 255 is absolute white and cannot go higher.
        value = 255

    # Value must be whole number.
    return round(value)
