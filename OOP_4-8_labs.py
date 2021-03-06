import datetime


class FinallyAttributeError(Exception):
    def __init__(self, type: str, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'{self.type} - {self.value} и его нельзя изменить'


class MilitaryType:
    """Вид войск"""

    def __init__(self, name: str):
        """
        :param name: Название
        """
        self.name = name


class Place:
    """Место дислокации"""

    def __init__(self, country: str, city: str, address: str, square: float):
        """
        :param country: Страна
        :param city: Город
        :param address: Адрес
        :param square: Занимаемая площадь
        """
        self.country = country
        self.city = city
        self.address = address
        self.square = square


class MilitaryUnit:
    """Воинская часть"""

    def __init__(self, number: int, place: Place, type: MilitaryType, number_of_company: int):
        """
        :param number: Номер части
        :param place: Место дислокации
        :param type: Тип войск
        :param number_of_company: Количество рот
        """
        self.number = number
        self.place = place
        self.type = type
        self.number_of_company = number_of_company


class Company:
    """Рота"""
    def __init__(self, name: str):
        """
        :param name: Название
        :param military_count: Количество служащих
        :param personnel: Личный состав роты (список)
        """
        self.name = name
        self.__military_count = 0
        self.__personnel = []
        self.index = 0

    @property
    def military_count(self):
        return self.__military_count

    @property
    def personnel(self):
        return self.personnel

    def __str__(self):
        return f"Название роты - {self.name}\n" \
               f"Количество служащих - {self.military_count}"

    def __add__(self, value):
        self.__personnel.append(value)
        self.__military_count += 1

    def __iter__(self):
        for p in self.__personnel:
            yield p

    def __next__(self):
        if self.index == len(self.__personnel):
            raise StopIteration
        self.index += 1
        return self.__personnel[self.index]


class Personnel:
    """Личный состав"""

    def __init__(self, surname: str, company: Company, post: str, birth_year: int, enlistment: int, awards: list,
                 military_events: list):
        """
        :param surname: Фамилия
        :param company: Рота
        :param post: Должность
        :param birth_year: Год рождения
        :param enlistment: Год поступления на службу
        :param seniority: Выслуга лет
        :param awards: Награды  (список)
        :param military_events: Участие в военных мероприятиях (список)
        """
        self.surname = surname
        self.company = company
        self.post = post
        self.__birth_year = birth_year
        self.__enlistment_year = enlistment
        self.seniority = datetime.date.today().year - self.__enlistment_year
        self.awards = awards
        self.military_events = military_events

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self, value):
        raise FinallyAttributeError("Год рождения", self.__birth_year)

    @property
    def enlistment_year(self):
        return self.__enlistment_year

    @enlistment_year.setter
    def enlistment_year(self, value):
        raise FinallyAttributeError("Год поступления на службу", self.__birth_year)

    def __str__(self):
        return f"---Карточка солдата---\n" \
               f"Фамилия - {self.surname}\n" \
               f"Рота - {self.company}\n" \
               f"Должность - {self.post}\n" \
               f"Год рождения - {self.birth_year}\n" \
               f"Год поступления на службу - {self.__enlistment_year}\n" \
               f"Выслуга лет - {self.seniority}\n" \
               f"Награды - {self.awards}\n" \
               f"Участие в военных операциях - {self.military_events}\n"


company = Company("Лучшая рота")
personnel = Personnel("Иванов",
                      company,
                      "Капитан Роты",
                      1990,
                      2010,
                      ["Награда 1", "Награда 2"],
                      ["Военная операция 1"])
company + personnel

# Получение даты рождения
print(f'Год рождения солдата {personnel.surname} - {personnel.birth_year}')

# Попытка изменить дату рождения и отлов исключения
try:
    personnel.birth_year = 0
except FinallyAttributeError as ex:
    print(f'Ошибка: {ex}')

# Прочтем документацию
print("Документация класса Личный состав")
print(personnel.__init__.__doc__)

# Создадим еще одного солдата и проверим перегрузку, добавив его в роту
personnel2 = Personnel("Петров",
                       company,
                       "Старшина Роты",
                       1997,
                       2017,
                       ["Награда 1"],
                       [])

print(f'В роте "{company.name}" {company.military_count} служащих')
company + personnel2
print(f'В роте "{company.name}" {company.military_count} служащих')


# Проверка агрегации
for soldier in company:
    print(soldier)
===============================================================
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2022 vrl_mck

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
