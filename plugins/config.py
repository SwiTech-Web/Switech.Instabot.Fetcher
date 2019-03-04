import configparser


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.config = config['CONFIGURATION']


CONFIGURATION = Config()
