"""Task: This module sorts out auto white balance for our picture."""


# Functions ------------------------------------------------------------

def auto_white_balance(colour, white):
    """ This function corrects the white balance of our image.
    The math is a basic colour correction algorithm from photo stack-exchange.
    :param colour: The average colour RGB array.
    :param white: The white balance RGB array.
    :return: The colour corrected colour RGB array.
    """
    luminance = (white[0] + white[1] + white[2]) / 3

    # Normalise for Red, Green, and Blue channels.

    for channel in range(2):
        colour[channel] = clip_colours(colour[channel] * luminance / white[channel])

    return colour


def clip_colours(colour_value):
    """ This function ensures that our auto white balance module does not
    exceed the limits of our RGB spectrum.

    :param colour_value: The value of our colour channel.
    :return: The normalised value of our colour channel.
    """

    if colour_value <= 0:

        # Value of 0 is absolute black and cannot go lower.
        value = 0

    elif colour_value >= 255:

        # Value of 255 is absolute white and cannot go higher.
        colour_value = 255

    # Value must be whole number.
    return round(colour_value)
