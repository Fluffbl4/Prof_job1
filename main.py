from application.salary import calculate_salary
from application.db.people import get_employees
import datetime


def main():
    print(f"Текущая дата: {datetime.datetime.now().date()}")

    calculate_salary()
    get_employees()


if __name__ == "__main__":
    main()