import pytest

from src.tracker import CallsTracker


# Тестируемые функции
def function_a():
    """Первая функия"""
    function_b()


def function_b():
    """Вторая функция"""
    function_c(1)


def function_c(a):
    """Третье функция"""
    if a == 0:
        pass
    else:
        function_d()


def function_d():
    """Четвертая функция"""
    function_c(0)


def test_tracker_basic():
    """Проверяем, что tracker корректно отслеживает вызовы функций."""
    tracker = CallsTracker()
    tracked_function_a = tracker.add_tracking(function_a)

    tracked_function_a()

    assert tracker.call_sequence == ["function_a", "function_b", "function_c", "function_d", "function_c"]


def test_tracker_empty_call_sequence():
    """Проверяем, что при отсутствии вызовов возникает исключение."""
    tracker = CallsTracker()

    with pytest.raises(ValueError, match="Call sequence is empty!"):
        _ = tracker.call_sequence


def test_tracker_multiple_calls():
    """Проверяем, что последовательность вызовов накапливается при нескольких запусках."""
    tracker = CallsTracker()
    tracked_function_a = tracker.add_tracking(function_a)

    tracked_function_a()
    tracked_function_a()

    assert tracker.call_sequence == [
        "function_a",
        "function_b",
        "function_c",
        "function_d",
        "function_c",
        "function_a",
        "function_b",
        "function_c",
        "function_d",
        "function_c",
    ]


def test_tracker_clear_sequence():
    """Проверяем, что последовательность вызовов очищается"""
    tracker = CallsTracker()
    tracked_function_a = tracker.add_tracking(function_a)

    tracked_function_a()
    tracker.clear_call_sequence()
    tracked_function_a()

    # Два вызова должны удвоить последовательность вызовов
    with pytest.raises(ValueError, match="Call sequence is empty!"):
        _ = tracker.call_sequence


def test_tracker_clear_empty_sequence():
    """Проверяем, что пустая последовательность вызовов не очищается."""
    tracker = CallsTracker()

    with pytest.raises(ValueError, match="Call sequence is already empty!"):
        tracker.clear_call_sequence()
