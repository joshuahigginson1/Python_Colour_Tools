"""Task: Get the height and width of an numpy array."""


# Functions ------------------------------------------------------------

def get_size(image):
    """ This function gets the size of our original image.
    :param image: Our image as a numpy array.
    :return: Returns a tuple (width, height)
    """

    shape = image.shape

    width = shape[1]
    height = shape[0]

    return width, height
