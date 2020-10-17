"""Task: Get the height and width of an numpy array."""


# Functions ------------------------------------------------------------

def get_size(image):
    """ This function gets the size of our original image.
    :param image: Our image as a numpy array.
    :return: Returns a tuple (height, width)
    """

    shape = image.shape
    height = shape[0]
    width = shape[1]

    return height, width
