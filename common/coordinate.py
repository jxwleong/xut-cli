class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

button_location = {
    'TOP_BAR': Coordinate(365, 20), # To minimize window
    'STRESS_TEST_SIDEBAR': Coordinate(65, 205),
    'STRESS_TEST_CPU_CHECKBOX': Coordinate(245, 130),
    'STRESS_TEST_CPU_DAY': Coordinate(40, 130),
    'STRESS_TEST_CPU_HOUR': Coordinate(645, 130),
    'STRESS_TEST_CPU_MINUTE': Coordinate(735, 130),
    'START_TESTING': Coordinate(300, 330),
    'STOP_TESTING': Coordinate(300, 180),
    'FILE_LOGGING': Coordinate(905, 460), # On minimized window, the coordinate will differ from diff resolution if taken maximize window
    }

def get_active_button_coordinate(
    window_coordinate,
    button
):
    """
    Get the button coordinate on active window
    given the active window coordinate
    """
    if (not isinstance(window_coordinate, Coordinate) or
        not isinstance(button, str)):
        raise ValueError(f'Invalid argument type.')
    return Coordinate(window_coordinate.x + button_location[button].x, \
                window_coordinate.y + button_location[button].y)