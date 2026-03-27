"""
Exceptions for the service.
"""

from service.shared.registry import ServiceRegistry


class EventAlreadyExists(Exception):
    def __init__(self, id: str) -> None:
        super().__init__(
            f"Event with id '{id}' already exists.",
        )
        self.id = id


# ------------------------------------------------------------
# Event Exceptions
# ------------------------------------------------------------
class EventNotFound(Exception):
    """
    Event not found
    ### Parameters:
    - id: str
        - Event id
    """

    def __init__(self, id: str) -> None:
        super().__init__(
            f"Event with id '{id}' not found.",
        )
        self.id = id


class EventBadFormat(Exception):
    """
    Event Bad Format
    ### Parameters:
    - field: str
        - Event field
    - reason: str
        - Reason of the bad format
    """

    def __init__(self, field: str, reason: str) -> None:
        super().__init__(f"Event field '{field}' is invalid: {reason}.")
        self.field = field
        self.reason = reason


# ------------------------------------------------------------
# Event Job Exceptions
# ------------------------------------------------------------
class EventJobNotFound(Exception):
    """Event job not found by job_id."""

    def __init__(self, event_job_id: str) -> None:
        super().__init__(f"Event job with job_id '{event_job_id}' not found.")
        self.event_job_id = event_job_id


class EventJobAlreadyExists(Exception):
    """Event job already exists for (id, job_id)."""

    def __init__(self, id: str, job_id: str) -> None:
        super().__init__(f"Event job already exists for id '{id}', job_id '{job_id}'.")
        self.id = id
        self.job_id = job_id


# ------------------------------------------------------------
# Event Message Exceptions
# ------------------------------------------------------------
class EventMessageNotFound(Exception):
    """Event message not found by message_id."""

    def __init__(self, message_id: str) -> None:
        super().__init__(f"Event message with message_id '{message_id}' not found.")
        self.message_id = message_id


# ------------------------------------------------------------
# Workflow State Exceptions
# ------------------------------------------------------------
class WorkflowStateNotFound(Exception):
    """Workflow state not found by id."""

    def __init__(self, id: str) -> None:
        super().__init__(f"Workflow state with id '{id}' not found.")
        self.id = id


# ------------------------------------------------------------
# Handle Exception
# ----------------
# Rational: Interface layer must handle exceptions and
# return the proper status according to the client
# ------------------------------------------------------------
def handle_exception(exception: Exception) -> None:
    """
    Standandar way to deal with exceptions
    """
    logger = ServiceRegistry.get_logger()
    logger.error(
        f"Error: {exception}",
        exc_info=True,
    )


# ------------------------------------------------------------
# AI Provider Exceptions
# ------------------------------------------------------------


class AIProviderInsufficientCredits(RuntimeError):
    """AI provider insufficient credits."""

    def __init__(self, provider: str) -> None:
        super().__init__(f"AI provider '{provider}' insufficient credits.")
        self.provider = provider


class AIProviderAuthenticationFailed(RuntimeError):
    """AI provider authentication failed."""

    def __init__(self, provider: str) -> None:
        super().__init__(f"AI provider '{provider}' authentication failed.")
        self.provider = provider


class AIAPIKeyNotFound(RuntimeError):
    """AI API key not found."""

    def __init__(self, message: str | None = None) -> None:
        if message:
            super().__init__(message)
        super().__init__("AI API key not found. Please set it in your .env file.")


class AIProviderUnknownError(RuntimeError):
    """AI provider unknown error."""

    def __init__(self, provider: str) -> None:
        super().__init__(f"AI provider '{provider}' unknown error.")
        self.provider = provider


# ------------------------------------------------------------
# Event Prediction Processed Message Exceptions
# ------------------------------------------------------------
class EventPredictionProcessedMessageNotFound(Exception):
    """Event prediction processed message not found by message_id."""

    def __init__(self, message_id: str) -> None:
        super().__init__(
            f"Event prediction processed message with message_id '{message_id}' not found."
        )
        self.message_id = message_id


class EventPredictionProcessedMessageBadFormat(Exception):
    """Event prediction processed message bad format."""

    def __init__(self, reason: str, id: str | None = None) -> None:
        super().__init__(f"Bad format in message: {reason}.")
        self.id = id
        self.reason = reason
