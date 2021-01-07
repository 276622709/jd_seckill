import os
import configparser
from datetime import datetime

class Config(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: config.ini")
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')
        #Auto modify the buy_time in config.ini to 'today 09:59:59.500'
        #ex: buy_time = '2021-01-06 09:59:59.500'       
        self.buy_time = datetime.now().strftime('%Y-%m-%d')+' 09:59:59.500'
        self._config.set('config','buy_time',self.buy_time)
        self._configRaw.set('config','buy_time',self.buy_time)
        with open(self._path,'w') as f:
            self._config.write(f)

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)


global_config = Config()
