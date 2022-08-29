from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from emoji import emojize

if __name__ == '__main__':
    print(datetime.datetime.now())
    calculate_salary()
    get_employees()
    print(emojize("Python is fun :red_heart:", variant="emoji_type"))