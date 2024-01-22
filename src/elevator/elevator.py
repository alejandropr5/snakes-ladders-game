from typing import List, Dict


def elevator_iterations(
    floors: List[int],
    init_floor: int,
    floors_map: Dict[int, int]
) -> None:
    """Simulate the operation of an elevator in a 29-story building.

    As the elevator is running, it receives as parameters: an array of
    floors, an initial floor and an map of floors entered.

    The function prints in console the current floor of the elevator,
    the direction in which it travels, the floor in which it stops and
    the floor entered each time any of these changes.

    >>> elevator_iterations([5, 29, 13, 10], 4, {5:2, 29: 10, 13: 1, 10:1})
    1. Elevator on floor 4
    2. Elevator going up
    3. Elevator on floor 5
    4. Elevator stops → [29, 13, 10] 5.
    5. Floor entered 2 → [29, 13, 10, 2].
    6. Elevator going up
    7. Elevator on floor 6, ... 7, ... 8, ... 9
    8. Elevator on floor 10
    9. Elevator stops → [29, 13, 2] 10.
    10. Floor entered 1 → [29, 13, 1] 11.
    11. Elevator going up
    12. Elevator in floor 11, ... 12.
    13. Elevator on floor 13
    14. Elevator stops → [29, 2, 1].
    15. Elevator going up
    16. Elevator on floor 14, ... 28.
    17. Elevator on floor 29
    18. Elevator stops → [2, 1].
    19. Floor entered 10 → [2, 1, 10].
    20. Elevator descending
    21. Elevator in floor 28, ... 11
    22. Elevator on floor 10
    23. Elevator stops → [2, 1].
    24. Elevator descending
    25. Elevator on floor 9, ... 3
    26. Elevator on floor 2
    27. Elevator stops → [1]
    28. Elevator descending
    29. Elevator on floor 1
    30. Elevator stops

    Args:
        floors (list[int]): An array of floors to which the elevator
            will be called in a defined order.
        init_floor (int): Initial floor of execution
        floors_map (dict[int, int]): Map of floors entered
    """
    pass
