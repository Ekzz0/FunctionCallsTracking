from typing import Any, Callable, List

from src.decorator import track_decorator


class CallsTracker:
    """
    Class for calls sequence tracking
    """

    def __init__(self) -> None:
        """Init main attributes"""
        self._call_sequence: List[str] = []

    def add_tracking(self, tracing_function: Callable[..., Any]) -> Callable[..., Any]:
        """Метод добавляет к отслеживанию функцию"""
        if not callable(tracing_function):
            raise ValueError("Name must be a callable object!")

        decorated_function = track_decorator(self._call_sequence)(tracing_function)
        return decorated_function

    @property
    def call_sequence(self) -> List[str]:
        """Getter for _call_sequence"""
        if not self._call_sequence:
            raise ValueError("Call sequence is empty!")
        return self._call_sequence

    def clear_call_sequence(self) -> None:
        """Clearing the call sqeuence attribute"""
        if not self._call_sequence:
            raise ValueError("Call sequence is already empty!")
        self._call_sequence = []
