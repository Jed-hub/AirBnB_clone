#!/usr/bin/env python3
"""
Review module
"""


class Review(BaseModel):
    """
    Description: rewiew

    Attributes:
        place_id: the place uniq id (string)
        user_id: user uniq id (string)
        text: a text (string)
    """
    place_id = ''
    user_id = ''
    text = ''
