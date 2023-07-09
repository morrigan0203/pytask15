import csv
import logging
import argparse

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename="TesT_15/zadanie_dz.log", encoding="utf-8", level=logging.INFO)

logger = logging.getLogger("zadanie_dz.py")

class FIO:
    def __init__(self) -> None:
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    
    def __delete__(self, instance):
        logger.error(f'Свойство "{self.param_name}" нельзя удалять')
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    
    def validate(self, value):
        if not (type(value) == str):
            logger.error(f'Значение {value} должно быть строкой')
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.isalpha():
            logger.error(f'Значение {value} должно быть только буквы')
            raise TypeError(f'Значение {value} должно быть только буквы')
        if value[0].islower():
            logger.error(f'Значение {value} должно начинаться с заглавной буквы')
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = FIO()
    surname = FIO()

    def __init__(self, name: str, surname: str, fileName: str) -> None:
        self.name = name
        self.surname = surname
        self.subjects = []
        self.marks = {}
        self.tests = {}
        with open(fileName, "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                self.subjects.append(row[0])
    
    def _validateMark(self, value):
        if type(value) != int:
            logger.error(f'Оценка {value} должна быть числом')
            raise ValueError(f'Оценка {value} должна быть числом')
        if value < 2 or value > 5:
            logger.error(f'Оценка {value} должна быть от 2х до 5ти')
            raise ValueError(f'Оценка {value} должна быть от 2х до 5ти')
    
    def _validateTest(self, value):
        if type(value) != int:
            logger.error(f'Оценка {value} должна быть числом')
            raise ValueError(f'Оценка {value} должна быть числом')
        if value < 0 or value > 100:
            logger.error(f'Оценка {value} должна быть от 0 до 100')
            raise ValueError(f'Оценка {value} должна быть от 0 до 100')
    
    def _validateSubject(self, value):
        if value not in self.subjects:
            logger.error(f'Предмет {value} отсутвует в списке {self.subjects}')
            raise ValueError(f'Предмет {value} отсутвует в списке {self.subjects}')
   
    def addMark(self, subject, mark: int):
        logger.info(f'Добавить оценку {mark} по предмету {subject}')
        self._validateMark(mark)
        if subject in self.subjects:
            listMarks = self.marks.get(subject, [])
            listMarks.append(mark)
            self.marks[subject] = listMarks

    def addTest(self, subject, mark):
        logger.info(f'Добавить оценку {mark} за тест по предмету {subject}')
        self._validateTest(mark)
        if subject in self.subjects:
            listTests = self.tests.get(subject, [])
            listTests.append(mark)
            self.tests[subject] = listTests

    def allMarks(self, subject) -> list:
        logger.info(f'Возвращает список всех оценок по предмету {subject}')
        self._validateSubject(subject)
        return self.marks[subject]

    def allTests(self, subject) -> list:
        logger.info(f'Возвращает список оценок за тесты по предмету {subject}')
        self._validateSubject(subject)
        return self.tests[subject]

    def averangeMark(self):
        amount, count = 0, 0
        for k,v in self.marks.items():
            amount = amount + sum(v)
            count = count + len(v)
        logger.info(f'Средняя оценка : {amount/count}')
        return amount/count

    def averangeTests(self, subject):
        self._validateSubject(subject)
        subjectTests = self.tests[subject]
        res = sum(subjectTests)/len(subjectTests)
        logger.info(f'Средняя оценка за тесты по предмету {subject} : {res}')
        return res


if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-name', metavar="name", type=str, help="Имя студента", default="Вася")
    parser.add_argument('-surname', metavar="surname", type=str, help="Фамилия студента", default="Пупкин")
    parser.add_argument('-subjects', metavar="subjects", type=str, help="Файл со списком предметов", default="TesT_15/subjects.csv")
    args = parser.parse_args()

    s = Student(args.name, args.surname, args.subjects)
    s.addMark("Химия", 5)
    s.addMark("Химия", 4)
    s.addMark("Химия", 5)
    s.addMark("Химия", 4)
    s.addTest("Химия", 90)
    s.addTest("Химия", 100)
    s.addTest("Химия", 80)
    print(s.marks)
    print(s.averangeMark())
    print(s.averangeTests("Химия"))
