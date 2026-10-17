"""Domain exceptions for Users."""


class UserNotFound(Exception):
    """Raised when a User record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"User {item_id} not found")
        self.item_id = item_id


class UserValidationError(ValueError):
    """Raised when User data breaks a business rule."""
