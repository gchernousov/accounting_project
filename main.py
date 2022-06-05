import application.salary as salary
import application.db.people as people

from datetime import datetime


if __name__ == "__main__":

    print('Начало работы программы...')

    print(f'Текущая дата: {datetime.now().date()}')

    people.get_employees()
    salary.calculate_salary()

    print('Конец работы программы...')