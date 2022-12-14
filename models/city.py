#!/usr/bin/env python3
"""
City module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Description: The city

    Attributes:
        state_id: the state id (string)
        name: the name of the city (string)
    """
    state_id = ''
    name = ''
