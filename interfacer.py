import os
import sys
import logging
import time

import pyautogui
import pygetwindow as gw

logger = logging.getLogger(__name__)

ROOT_DIR = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from common.CONSTANT import *
from common.coordinate import Coordinate
from common.coordinate import get_active_button_coordinate


def click(window_coordinate, button, clicks=1, interval=0):
    try:
        button_coordinate = get_active_button_coordinate(window_coordinate, button)
        logger.debug(f"Click on button '{button}' with coordinate [{button_coordinate.x}, {button_coordinate.y}] " \
                    f'with number of click: {clicks} and interval: {interval}')
        pyautogui.click(button_coordinate.x, button_coordinate.y, clicks, interval)
    except:
        raise Exception('Exception throwned by pyautogui.click()!')

def activate_window(title=XTU_WINDOW_NAME, retry_count=5):
    """Grab and active the window with title

    Args:
        title (str): Window of the window to be grab and activate
        retry_count (int, optional): Number of attempt to grab the window. Defaults to 5.
    """
    window_found = False
    count = 0
    while window_found is False:
        try:
            xtu_window = gw.getWindowsWithTitle(XTU_WINDOW_NAME)[0]
            logger.info(f'XTU window found!')
            logger.info(f'Window: {xtu_window}')
            xtu_window.activate()
            time.sleep(1)
            window_found = True
            return xtu_window
        except IndexError:
            logger.info(f"Grabbing XTU window with title '{XTU_WINDOW_NAME}', retry in 5 seconds ({count}/5)")
            count += 1
            time.sleep(5)
            continue