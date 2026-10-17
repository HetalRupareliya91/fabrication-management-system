"""Domain exceptions for Routings."""


class RoutingStepNotFound(Exception):
    """Raised when a RoutingStep record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"RoutingStep {item_id} not found")
        self.item_id = item_id


class RoutingStepValidationError(ValueError):
    """Raised when RoutingStep data breaks a business rule."""
