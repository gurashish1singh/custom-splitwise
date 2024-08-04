from __future__ import annotations


class SplitwiseAccessDenied(Exception):
    """
    Splitwise authentication failed. Check the API key.
    """


class EntityExistsError(Exception):
    """
    Row already exists in the table.
    """
