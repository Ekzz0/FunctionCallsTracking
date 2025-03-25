from tracecall.tracker import CallsTracker


def function_a() -> None:
    """First function"""
    function_b()


def function_b() -> None:
    """Second fuction"""
    function_c(1)


def function_c(a: int) -> None:
    """Third function"""
    if a == 0:
        pass
    else:
        function_d()


def function_d() -> None:
    """Fourth function"""
    function_c(0)


if __name__ == "__main__":
    tracker = CallsTracker()  # Init calls tracker class
    function_a = tracker.add_tracking(function_a)  # Or rename target function like tracked_function_a
    function_a()  # Run the main function
    print("Call sequence:", tracker.call_sequence)  # See the calls sequence
    # Output: ['function_a', 'function_b', 'function_c', 'function_d', 'function_c']
