import logging

logging.basicConfig(filename="TesT_15/zadanie_1.log", encoding="utf-8", level=logging.INFO)
logger = logging.getLogger("zadanie_1.py")

def devide(num: float, div: float) -> float:
    try:
        return num / div
    except ZeroDivisionError as e: 
        logger.error("Error devide to zero")

if __name__=="__main__":
    print(devide(100, 10))
    print(devide(10, 1))
    print(devide(100, 0))