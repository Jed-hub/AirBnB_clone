#!/usr/bin/env python3
"""
User module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Description: Creates a new user

    Attributes:
        email: the user email (string)
        password: the user password (string)
        first_name: the user first_name (string)
        last_name: the user last_name (string)
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
