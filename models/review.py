#!/usr/bin/python3
"""This module defines the class method"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class represents a review model"""
    place_id = ""
    user_id = ""
    text = ""
