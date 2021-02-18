# coding: utf-8

import os
import logging

from viaduct.installerUtils import *


def installDriver(cwd=False):
    """
    Appends the directory of the geckodriver binary file to PATH.
    :param cwd: Flag indicating whether to download to current working directory
    :return: The file path of geckodriver
    """
    geckodriver_filepath = download_geckodriver(cwd)
    if not geckodriver_filepath:
        logging.debug('Can not download geckodriver.')
        return
    geckodriver_dir = os.path.dirname(geckodriver_filepath)
    if 'PATH' not in os.environ:
        os.environ['PATH'] = geckodriver_dir
    elif geckodriver_dir not in os.environ['PATH']:
        os.environ['PATH'] = geckodriver_dir + \
            get_variable_separator() + os.environ['PATH']
    return geckodriver_filepath


def get_firefox_version():
    """
    Get installed version of chrome on client
    :return: The version of chrome
    """
    return get_firefox_version()
