import pytest

from tracecall.tracker import CallsTracker


def function_a():
    """First function"""
    function_b()


def function_b():
    """Second function"""
    function_c(1)


def function_c(a):
    """Third function"""
    if a == 0:
        pass
    else:
        function_d()


def function_d():
    """Fourth function"""
    function_c(0)


def test_tracker_basic():
    """Test Tracker main functional"""
    tracker = CallsTracker()
    tracked_function_a = tracker.add_tracking(function_a)

    tracked_function_a()

    assert tracker.call_sequence == ["function_a", "function_b", "function_c", "function_d", "function_c"]


def test_tracker_empty_call_sequence():
    """Test Tracker empty call exception"""
    tracker = CallsTracker()

    with pytest.raises(ValueError, match="Call sequence is empty!"):
        _ = tracker.call_sequence


def test_tracker_multiple_calls():
    """Test calls sequence with multiple calls"""
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
    """Test calls sequence clearing"""
    tracker = CallsTracker()
    tracked_function_a = tracker.add_tracking(function_a)

    tracked_function_a()
    tracker.clear_call_sequence()
    tracked_function_a()

    with pytest.raises(ValueError, match="Call sequence is empty!"):
        _ = tracker.call_sequence


def test_tracker_clear_empty_sequence():
    """Test empty call sequence clearing exception"""
    tracker = CallsTracker()

    with pytest.raises(ValueError, match="Call sequence is already empty!"):
        tracker.clear_call_sequence()
