#!/usr/bin/python3
"""
Class review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class review with public attribute
    """
    place_id = ''
    user_id = ''
    text = ''
