"""Task: Get the height and width of an numpy array."""


# Functions ------------------------------------------------------------

def get_size(image_array):
    """ This function gets the size of our original image.
    :param image_array: Our image as a numpy array.
    :return: Returns a tuple (width, height)
    """

    # The method .shape returns a list of features about the numpy array.
    shape = image_array.shape

    width = shape[1]
    height = shape[0]

    return width, height
