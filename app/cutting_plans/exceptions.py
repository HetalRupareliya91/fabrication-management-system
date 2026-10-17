"""Domain exceptions for Cutting Plans."""


class CuttingPlanNotFound(Exception):
    """Raised when a CuttingPlan record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"CuttingPlan {item_id} not found")
        self.item_id = item_id


class CuttingPlanValidationError(ValueError):
    """Raised when CuttingPlan data breaks a business rule."""
