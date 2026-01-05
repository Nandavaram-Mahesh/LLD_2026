class SingletonMeta(type):
    _instances={}
    
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls]=super().__call__(*args, **kwds)
        return cls._instances[cls]
    
class Logger(metaclass = SingletonMeta):
    def errorlog(self):
        print("Logging to error file")
        

# ClientCode

logger=Logger()
logger.errorlog()

logger_1 = Logger()
logger_1.errorlog()