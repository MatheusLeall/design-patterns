from typing import Any, Dict


class MetaSingleton(type):
    __instances: Dict = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


first_log = Logger()
print(f"first log = {id(first_log)}")

second_log = Logger()
print(f"second log = {id(second_log)}")
