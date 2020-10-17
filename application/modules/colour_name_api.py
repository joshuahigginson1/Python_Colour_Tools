"""Task: Retrieve the colour name from TheColourAPI."""

# Imports --------------------------------------------------------------

import requests

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------
import requests as requests


def retrieve_colour(red, green, blue):

    colour_to_api = f"rgb({red},{green},{blue})"

    print(f"Sending colour data to API: {colour_to_api}")

    r = requests.get(f'https://www.thecolorapi.com/id?rgb={colour_to_api}')

    output_colour_name = r.json()['name']['value']

    print(f"The colour is: {output_colour_name}")
    return output_colour_name


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
