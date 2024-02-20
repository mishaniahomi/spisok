# Этот файл предназначен для создания классов данных


class Employee: # класс Сотрудник
    def __init__(self, surname: str, name: str, patronymic: str, position: str, rank: str, status: str):
        self.surname = surname  # фамилия
        self.name = name  # имя
        self.patronymic = patronymic  # отчество
        self.position = position  # должность
        self.rank = rank  # звание
        self.status = status  # статус
