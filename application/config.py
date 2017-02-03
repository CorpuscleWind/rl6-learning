from ConfigParser import RawConfigParser


class SafeConfigParser(object, RawConfigParser):
    def __init__(self, **kwargs):
        RawConfigParser.__init__(self, **kwargs)

    def get(self, section, option, default=None):
        try:
            return RawConfigParser.get(self, section, option)
        except Exception:
            return default

    def getint(self, section, option, default=None):
        try:
            return RawConfigParser.getint(self, section, option)
        except Exception:
            return default

    def getboolean(self, section, option, default=None):
        try:
            return RawConfigParser.getboolean(self, section, option)
        except Exception:
            return default

    def getfloat(self, section, option, default=None):
        try:
            return RawConfigParser.getfloat(self, section, option)
        except Exception:
            return default
