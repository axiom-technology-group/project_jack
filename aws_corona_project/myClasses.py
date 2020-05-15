import datetime

class MyLogging:
    
    def __init__(self):
        self._filename = str()
        self._filemode = str()
        self._name = str()
        self._loglevel = 0
        self._levels = {'critical':50, 'error':40, 'warning':30,
               'info':20, 'debug':10, 'notset':0}

    def basicConfig(self, filename, filemode, level=30, name='root'):
        self._filename = filename
        self._filemode = filemode
        self._name = name
        self._loglevel = level

    def log(self, level, script):
        if level not in self._levels:
            raise TypeError('Invalid level')
        try:
            f = open(self._filename, self._filemode)
        except:
            raise IOError('Fails to read the file.')
        
        if self._levels.get(level) >= self._loglevel:
            text_in = str(
                datetime.datetime.now()) + ' - ' + self._name + ' - ' + level.upper() + ' - ' + script
            f.write(text_in + '\n')
            f.close()
        