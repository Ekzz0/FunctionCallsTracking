import sys
from types import FrameType
from typing import Any, Callable, List


def track_decorator(call_sequence: List[str]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator for calls sequence tracking"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Inner decorator"""

        def trace_calls(frame: FrameType, event: str, _: Any) -> Callable[..., Any]:
            """Main tracking function"""

            if event == "call":
                func_name = frame.f_code.co_name
                call_sequence.append(func_name)
            return trace_calls

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Main wrapper for function."""

            sys.settrace(trace_calls)
            result = func(*args, **kwargs)
            sys.settrace(None)
            return result

        return wrapper

    return decorator
