"""Domain exceptions for Maintenance."""


class MaintenanceTaskNotFound(Exception):
    """Raised when a MaintenanceTask record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"MaintenanceTask {item_id} not found")
        self.item_id = item_id


class MaintenanceTaskValidationError(ValueError):
    """Raised when MaintenanceTask data breaks a business rule."""
