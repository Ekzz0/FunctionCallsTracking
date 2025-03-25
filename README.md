# Python Package: tracecall
The project provides functionality for tracking the sequence of execution of python methods.
The work is done through the ``CallsTracker`` python object, which implements the ``add_tracking(function)``
and ``clear_call_sequence()`` python methods, and ``call_sequence`` attribute.

# How to install:
1) From PyPi repository:
```pip install tracecall```

2) Develop version:
    - Install ``Python >= 3.10``
    - Create virtual env: ``python -m venv venv`` on Windows or ``python3 -m venv venv`` on Linux.
    - Activate virtual env: ``venv/Scripts/activate`` on Windows or ``source venv/bin/activate`` on Linux.
    - Install the develop requirements: ``pip install -r requirements-dev.txt``
    - Activate pre-commit-hooks (Optional) with `Pylint`, `MyPy`, `Bandit` and `Pytest`: ``pre-commit install``

Note: If you want to run all tests manualy during the development, use ``pytest -v`` command

# Examples:
Full example file in `examples/example.py`

1. Define some methods:
```python
def function_a() -> None:
    """First function"""
    function_b()


def function_b() -> None:
    """Second fuction"""
    pass
```

2. Init CallsTracker object for start tracking:
```python
from tracecall import CallsTracker
tracker = CallsTracker()  # Init calls tracker class
```
3. Choose the method from which we are want to start track methods calls and run ``add_tracking(func)`` method for tracking. At this step target method will wrapped with special decorator. After this run new method:
```python
# Run like this or rename the target method like tracked_function_a
function_a = tracker.add_tracking(function_a)
function_a()  # Run the main function
```
4. Next you call get the ``call_sequence`` attribute from your ``tracker``
```python
print(tracker.call_sequence)
# Output: ['function_a', 'function_b']
```

# Documentation:
It will be later...
