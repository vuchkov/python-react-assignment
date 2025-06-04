import os


def get_default_resources_path():
    return os.path.join(os.path.dirname(__file__), 'resources')


class Config(object):
    DEBUG = False
    TESTING = False
    RESOURCES_PATH = get_default_resources_path()
