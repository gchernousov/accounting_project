from application.salary import calculate_salary
from application.db.people import get_employees

from datetime import datetime


if __name__ == "__main__":

    print('Начало работы программы...')

    print(f'Текущая дата: {datetime.now().date()}')

    get_employees()
    calculate_salary()

    print('Конец работы программы...')