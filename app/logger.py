import datetime

def __get_date(cls):
    format = "%H:%M:%S %d/%m"
    return datetime.datetime.now().strftime(format)

def info(cls, msg: str):
    log_msg = f"{'INFO':<10} {msg.ljust(cls.message_width)} {cls.__get_date()} [+]"
    print(log_msg)

def warning(cls, msg: str):
    log_msg = f"{'WARNING':<10} {msg.ljust(cls.message_width)} {cls.__get_date()} <"
    print(log_msg)

def error(cls, msg: str):
    log_msg = f"{'ERROR':<10} {msg.ljust(cls.message_width)} {cls.__get_date()} <<<"
    print(log_msg)

def debug(cls, msg: str):
    log_msg = f"{'DEBUG':<10} {msg.ljust(cls.message_width)} {cls.__get_date()}"
    print(log_msg)