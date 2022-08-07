#!/usr/bin/env python3
"""
Place module
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Description: place

    Attributes:
        city_id: the id of the city (string)
        user_id: the user id (string)
        name: the name of the place (string)
        description: the place description (string)
        number_rooms: the number of rooms (integer)
        number_bathrooms: the number of bathrooms (interger)
        max_guest: the max number of guest (integer)
        price_by_night: the price of the place by night (integer)
        latitude: the latitude of the place (float)
        longitude: the longitude of the place (float)
        amenity_ids: a list of amenity ids (list)
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
