from src.tracker import CallsTracker


# Тестируемые функции
def function_a() -> None:
    """Первая функия"""
    function_b()


def function_b() -> None:
    """Вторая функция"""
    function_c(1)


def function_c(a: int) -> None:
    """Третье функция"""
    if a == 0:
        pass
    else:
        function_d()


def function_d() -> None:
    """Четвертая функция"""
    function_c(0)


if __name__ == "__main__":
    tracker = CallsTracker()  # Init calls tracker class
    function_a = tracker.add_tracking(function_a)  # Or rename target function like tracked_function_a
    function_a()  # Run the main function
    print("Call sequence:", tracker.call_sequence)  # See the calls sequence
    # ['function_a', 'function_b', 'function_c', 'function_d', 'function_c']
