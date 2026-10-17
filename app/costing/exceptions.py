"""Domain exceptions for Job Costing."""


class JobCostNotFound(Exception):
    """Raised when a JobCost record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"JobCost {item_id} not found")
        self.item_id = item_id


class JobCostValidationError(ValueError):
    """Raised when JobCost data breaks a business rule."""
