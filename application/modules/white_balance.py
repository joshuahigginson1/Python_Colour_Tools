"""Task: This module sorts out auto white balance for our picture."""


# Functions ------------------------------------------------------------

def auto_white_balance(colour, white):

    luminance = (white[0] + white[1] + white[2]) / 3

    print(luminance)

    colour[0] = round(colour[0] * luminance / white[0])
    colour[1] = round(colour[1] * luminance / white[1])
    colour[2] = round(colour[2] * luminance / white[2])

    return colour
