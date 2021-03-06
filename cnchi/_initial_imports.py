# Set initial value for "_" to appease PyCharm
_ = lambda x: x

# Standard Lib
import argparse
import gettext
import locale
import logging
import logging.handlers
import os
import shutil
import sys
import uuid

# 3rd-Party Libs
try:
    from bugsnag.handlers import BugsnagHandler
    import bugsnag
    BUGSNAG_ERROR = None
except ImportError as err:
    BUGSNAG_ERROR = str(err)
    print("Error importing bugsnag: ", err)

# This Application
from config import ConfigLoader
from logging_utils import ContextFilter
import info
import misc.extra as misc
import show_message as show

try:
    from _base_object import BaseObject, Gio, Gtk
    from ui.cnchi_ui import CnchiUI
except ImportError as err:
    msg = 'Cannot create Cnchi UI Controller: {0}'.format(err.msg)
    logging.exception(msg)
    sys.exit(1)