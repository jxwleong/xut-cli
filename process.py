import os
import sys
import psutil
import logging
import subprocess

logger = logging.getLogger(__name__)

ROOT_DIR = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from common.CONSTANT import *

def get_process_pid(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return proc.pid

def is_process_running(process_name):
    # source: https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def get_all_xtu_process(process_name_list=XTU_PROCESS_NAME):
    logger.info(f'Searching PID for XTU relevent process...')
    pid_dict = {}
    for process in process_name_list:
        if get_process_pid(process) is not None:
            pid_dict[process] = get_process_pid(process)
    import json

    logger.info(    json.dumps(pid_dict))
    return pid_dict

def is_xtu_running(process_name_list=XTU_PROCESS_NAME):
    logger.info(f'Checking whether XTU is already running...')
    for process in process_name_list:
        if is_process_running(process) is True:
            return True
    return False

def kill_process_with_pid(pid):
    try:
        subprocess.Popen(f'taskkill /F /PID {pid}',
                         stdout=subprocess.DEVNULL)
        logger.info(f'The process with PID {pid} has been terminated')
    except:
        logger.error(f'Unable to terminate process with PID {pid}')
        raise Exception(f'Unable to terminate process with PID {pid}')

def kill_all_xtu_process(process_name_list=XTU_PROCESS_NAME):
    process_dict = get_all_xtu_process()
    for process, process_pid in process_dict.items():
        kill_process_with_pid(process_pid)