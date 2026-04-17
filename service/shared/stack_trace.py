"""
Helper: Stack Trace.

Key Points:

* Stack trace shows where the error started and how it propagated up through
your functions/files.

* Each line shows a file, line number, and function name.

* It's super helpful for debugging—find out exactly where your code failed.
"""

import sys
import traceback

from service.shared.logger import get_logger
from service.shared.terminal import ColorCode


def log_stack_trace() -> None:  # pragma: no cover
    logger = get_logger()
    exc_type, exc_value, exc_tb = sys.exc_info()
    tb = traceback.extract_tb(exc_tb)
    last_call = tb[-1]  # The last item is where the exception happened
    COLOR = ColorCode.LIGHT_CYAN_TXT
    RESET = ColorCode.RESET
    logger.error(
        f"Function: {COLOR}{last_call.name}{RESET}"
        f" - File: {COLOR}{last_call.filename}{RESET}"
        f" - Line number: {COLOR}{last_call.lineno}{RESET}"
        f" - Info: {COLOR}{last_call.line}{RESET}"
    )
