import os
import sys
import logging

import pyautogui

logger = logging.getLogger(__name__)

ROOT_DIR = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from common.coordinate import get_active_button_coordinate

def click(window_coordinate, button, clicks=1, interval=0):
    try:
        button_coordinate = get_active_button_coordinate(window_coordinate, button)
        logger.info(f"Click on button '{button}' with coordinate [{button_coordinate.x}, {button_coordinate.y}] " \
                    f'with number of click: {clicks} and interval: {interval}')
        pyautogui.click(button_coordinate.x, button_coordinate.y, clicks, interval)
    except:
        raise Exception('Exception throwned by pyautogui.click()!')