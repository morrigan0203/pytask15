import logging
from typing import Callable
from functools import wraps

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename="TesT_15/zadanie_2.log", encoding="utf-8", level=logging.INFO)

logger = logging.getLogger("zadanie_2.py")

def deco(func: Callable):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        final_dict = {}
        res = func(*args, **kwargs)
        for i in range(len(args)):
            final_dict.update({str(i): args[i]})

        logger.info(f'Call function "{func.__name__}" with parameters : "{final_dict}" and result "{res}"')

    return wrapper


@deco
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__=="__main__":
    multy(6, 7, temp=2, r=3, c=2, d=5)

