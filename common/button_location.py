class ButtonCoordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

button_location = {
    'STRESS_TEST_SIDEBAR': ButtonCoordinate(65, 205),
    'STRESS_TEST_CPU_CHECKBOX': ButtonCoordinate(245, 130),
    'STRESS_TEST_CPU_DAY': ButtonCoordinate(40, 130),
    'STRESS_TEST_CPU_HOUR': ButtonCoordinate(645, 130),
    'STRESS_TEST_CPU_MINUTE': ButtonCoordinate(735, 130),
    'START_TESTING': ButtonCoordinate(300, 330),
    'STOP_TESTING': ButtonCoordinate(300, 180),
    'FILE_LOGGING': ButtonCoordinate(905, 460), # On minimized window, the coordinate will differ from diff resolution if taken maximize window
    }

