#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Prevents user from dynamically creating new
    instance attributes, except if the new instance
    attribute is called first_name."""

    __lock__ = ["first_name"]
