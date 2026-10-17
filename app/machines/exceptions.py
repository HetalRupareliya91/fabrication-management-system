"""Domain exceptions for Machines."""


class MachineNotFound(Exception):
    """Raised when a Machine record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Machine {item_id} not found")
        self.item_id = item_id


class MachineValidationError(ValueError):
    """Raised when Machine data breaks a business rule."""
