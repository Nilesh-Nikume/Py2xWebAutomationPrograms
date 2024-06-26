import logging
import inspect


class LoggenClass:
    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]  # runtime -getting filepath -class -method
        logger = logging.getLogger(log_name)  # gen logs
        # logger = logging.getLogger()
        logfile = logging.FileHandler("D:\pythonProject-idrive360\Logs\i360.log")
        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")  # log format
        logfile.setFormatter(log_format)  # setting format to the logs
        logger.addHandler(logfile)  # adding log everytime to same file
        logger.setLevel(logging.INFO)  # set log level
        return logger
