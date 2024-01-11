#!/usr/bin/python3
"""Defines the `State` class.

Sub-classes the `BaseModel` class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
