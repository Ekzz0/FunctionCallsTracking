import sys
from types import FrameType
from typing import Any, Callable, List


def track_decorator(call_sequence: List[str]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор для отслеживания последовательности вызовов функций."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Декоратор, оборачивающий функцию и отслеживающий ее вызовы."""

        def trace_calls(frame: FrameType, event: str, _: Any) -> Callable[..., Any]:
            """Функция трассировки, отслеживающая вызовы функций."""

            if event == "call":
                func_name = frame.f_code.co_name
                call_sequence.append(func_name)
            return trace_calls

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обертка, устанавливающая трассировку перед вызовом функции и отключающая её после."""

            sys.settrace(trace_calls)
            result = func(*args, **kwargs)
            sys.settrace(None)
            return result

        return wrapper

    return decorator
