import logging
import locale
import argparse
from datetime import time, date, datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename="TesT_15/zadanie_4.log", encoding="utf-8", level=logging.INFO)

logger = logging.getLogger("zadanie_4.py")

def dateconvert(datestr: str) -> date:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    currentyear = datetime.now().year
    try:
        datetmp = datetime.strptime(datestr, '%d %A %B')
        return datetmp.replace(year=currentyear)
    except ValueError as e:
        logger.error(f'Неправильный формат входных данных :"{datestr}"')
        # raise ValueError(e)


if __name__=="__main__":
    print(dateconvert("01 четверг ноября"))
    print(dateconvert("03 среда мая"))
    # print(dateconvert("ййй четверг ноябрь"))

    print('-------------------------')

    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    parser = argparse.ArgumentParser()
    currentweekday = date.today().replace(day=1).strftime("%A")
    currentmonth = date.today().strftime("%B")
    parser.add_argument('-date', metavar="date", type=str, help="Date of month", default="01")
    parser.add_argument('-weekday', metavar="weekday", type=str, help="Day of week", default=currentweekday)
    parser.add_argument('-month', metavar="month", type=str, help="Month", default=currentmonth)
    args = parser.parse_args()
    print(dateconvert(f'{args.date} {args.weekday} {args.month}'))

