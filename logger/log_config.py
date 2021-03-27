import logging.config
import os
from log_colorformatter import ColorFormatter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'minimal': {
            'format': '%(asctime)s:%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'color_format': {
            'class': 'logging.ColorFormatter',
            'format': '$TIME_COLOR%(asctime)s$RESET:$COLOR%(levelname)s$RESET:$WHITE%(filename)s:%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'color_format',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': os.path.join(ROOT_DIR, os.path.basename(ROOT_DIR).split('.')[0] + '.log'),
            'mode': 'w',
            'class': 'logging.FileHandler',
        },
    },
    'loggers': {
        '': { # Root
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        '__main__': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },      
    },
}


