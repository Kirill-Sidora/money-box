import os
import csv
from datetime import datetime
from datetime import date

class Goal:
    def __init__(self, name: str, tottal_amount: int, balance: int, category: str, deadline):
        self.__name = name
        self.__tottal_amount = tottal_amount
        self.__balance = balance
        self.__category = category
        self.__status = 'не выполнена'
        self.__deadline = deadline

    def increase_balance(self, amount: int):
        try:
            if self.__balance + amount > self.__tottal_amount:
                raise ValueError(f'Баланс не может превышать итоговой суммы цели ({self.__balance} + {amount} > {self.__tottal_amount})')

            self.__balance += amount

            if self.__balance == self.__tottal_amount:
                self.__change_status()
        except ValueError as error:
            print(error)

    def decrease_balance(self, amount: int):
        try:
            if self.__balance - amount < 0:
                raise ValueError(f'Баланс не может быть отрицательным ({self.__balance} - {amount} < 0)')

            self.__balance -= amount
        except ValueError as error:
            print(error)

    def get_percentage_of_progress(self):
        result = (self.__balance * 100) / self.__tottal_amount

        return result

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_deadline(self):
        return self.__deadline

    def get_status(self):
        return self.__status

    def get_balance(self):
        return self.__balance

    def get_tottal_amount(self):
        return self.__tottal_amount

    def __change_status(self):
        self.__status = 'выполнена'

def create_goal():
    while True:
        try:
            category = input('название категории>')

            if category.strip() == '':
                raise ValueError('ошибка>название категории не может состоять только из символов пробела и переноса на новую строку')

            break
        except ValueError as error:
            print(error)

    while True:
        try:
            name = input('название цели>')

            if name.strip() == '':
                raise ValueError('ошибка>название цели не может состоять только из символов пробела и переноса на новую строку')
            elif os.path.exists(f'categoryes/{category}/{name}.csv'):
                raise ValueError(f'ошибка>цель с названием "{name}" уже существует в категории "{category}"')
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            tottal_amount = input('итоговая стоимость>')

            if not tottal_amount.strip().isdigit():
                raise ValueError('ошибка>итоговая стоимость должна состоять только из цифр')

            break
        except ValueError as error:
            print(error)

    while True:
        try:
            balance = input('баланс>')

            if not balance.isdigit():
                raise ValueError('ошибка>баланс должен состоять только из цифр')
            elif int(balance) >= int(tottal_amount):
                raise ValueError('ошибка>баланс должен быть меньше итоговой суммы')

            break
        except ValueError as error:
            print(error)

    current_date = datetime.now()
    current_year = current_date.year

    while True:
        try:
            year = input('дата завершения. год>')

            if int(year) < int(current_year):
                raise ValueError(f'ошибка>{year} уже прошёл')

            break
        except ValueError as error:
            print(error)

    current_month = current_date.month

    while True:
        months_list = ['январь', 'ферваль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентрябрь', 'октябрь', 'ноябрь', 'декабрь']

        try:
            month = input('дата завершения. месяц>')

            if int(month) < 1 or int(month) > 12:
                raise ValueError(f'ошибка>неопознанный номер месяца. в году всего 12 месяцев')

            if int(year) == int(current_year) and int(month) < int(current_month):
                raise ValueError(f'ошибка>{months_list[int(month)-1]} уже прошёл')

            break
        except ValueError as error:
            print(error)

    current_day = current_date.day

    while True:
        month_days_dict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

        try:
            day = input('дата завершения. день>')

            if int(day) < 0 or int(day) > month_days_dict.get(month):
                raise ValueError(f'ошибка>введите номер дня от {current_day} до {month_days_dict.get(month)}')

            break
        except ValueError as error:
            print(error)

    deadline = date(int(year), int(month), int(day))

    current_directory = os.getcwd()

    category_src = f'{current_directory}/categoryes/{category}'
    if not os.path.exists(f'categoryes/{category}'):

        os.makedirs(category_src)

    goal_src = f'{category_src}/{name}.csv'

    goal = Goal(name, tottal_amount, balance, category, deadline)

    with open(goal_src, 'w', encoding='utf-8', newline='') as goal_file:
        writer = csv.DictWriter(goal_file, ['name', 'tottal_amount', 'balance', 'category', 'status', 'year', 'month', 'day'])
        writer.writeheader()
        writer.writerow({'name': name, 'tottal_amount': tottal_amount, 'balance': balance, 'category': category, 'status': goal.get_status(), 'year': year, 'month': month, 'day': day})

    return goal

def delete_goal():
    while True:
        try:
            category = input('название категории>')

            if category.strip() == '':
                raise ValueError('ошибка>название категории не может состоять только из символов пробела и переноса на новую строку')

            break
        except ValueError as error:
            print(error)

    while True:
        try:
            name = input('название цели>')

            if name.strip() == '':
                raise ValueError('ошибка>название цели не может состоять только из символов пробела и переноса на новую строку')
            
            break
        except ValueError as error:
            print(error)

    try:
        goal_file_src = f'{os.getcwd()}/categoryes/{category}/{name}.csv'

        os.remove(goal_file_src)
    except FileNotFoundError:
        print(f'ошибка>в категории "{category}" нетуцели "{name}"')

def find_goal():
    while True:
        try:
            category = input('название категории>')

            if category.strip() == '':
                raise ValueError('ошибка>название категории не может состоять только из символов пробела и переноса на новую строку')

            break
        except ValueError as error:
            print(error)

    while True:
        try:
            name = input('название цели>')

            if name.strip() == '':
                raise ValueError('ошибка>название цели не может состоять только из символов пробела и переноса на новую строку')
            
            break
        except ValueError as error:
            print(error)

    goal_file_src = f'{os.getcwd()}/categoryes/{category}/{name}.csv'
    goal_category_src = f'{os.getcwd()}/categoryes/{category}'

    try:
        if not os.path.exists(goal_category_src):
            raise FileNotFoundError(f'сообщение>категория с названием "{category}" не существует')
        if not os.path.exists(goal_file_src):
            raise FileNotFoundError(f'сообщение>в категории "{category}" нету цели "{name}"')
    except FileNotFoundError as error:
        print(error)
    

        return

    with open(goal_file_src, 'r', encoding='utf-8') as goal_file:
        reader = csv.DictReader(goal_file)

        current_date = date.today()

        for row in reader:
            goal = Goal(row.get('name'), int(row.get('tottal_amount')), int(row.get('balance')), row.get('category'), row.get('deadline'))

            if current_date > date(int(row.get('year')), int(row.get('month')), int(row.get('day'))):
                with open(goal_file_src, 'w', encoding='utf-8', newline='') as goal_file:
                    writer = csv.DictWriter(goal_file, ['name', 'tottal_amount', 'balance', 'category', 'status', 'deadline'])

                    writer.writeheader
                    writer.writerow({'name': goal.get_name(), 'tottal_amount': goal.get_tottal_amount(), 'balance': goal.get_balance(), 'category': goal.get_category(), 'status': 'просрочена', 'deadline': goal.get_deadline()})

    command_list = ['увеличить баланс', 'уменьшить баланс', 'информация', 'выход']

    while True:
        while True:
            try:
                command = input(f'Текущая цель: {goal.get_name()}, команда>')

                if not command in command_list:
                    raise ValueError(f'ошибка>{command}\nсообщение>для просмотра всех допустимых комманд введите "помощь"')

                break
            except ValueError as error:
                print(error)

        if command == 'помощь':
            print(f'''
                помощь - выводит все доступные команды
                увеличить баланс - увеличивает баланс цели на введённое значение
                уменьшить баланс - уменьшает баланс цели на введённое значение
                выход - завершение работы с текущей целью
            ''')

        if command == 'выход':
            return

        if command == 'увеличить баланс':
            current_balance = goal.get_balance()

            while True:
                try:
                    amount = input('сумма>')

                    if not amount.strip().isdigit():
                        raise ValueError('сумма должна состоять только из цифр')

                    break
                except ValueError as error:
                    print(error)

            goal.increase_balance(int(amount))

            if current_balance != goal.get_balance():
                with open(goal_file_src, 'r', encoding='utf-8') as goal_file:
                    reader = csv.DictReader(goal_file)
                    row = list(reader)[0]
                    row.update({'balance': goal.get_balance()})

                with open(goal_file_src, 'w', encoding='utf-8', newline='') as goal_file:
                    writer = csv.DictWriter(goal_file, ['name', 'tottal_amount', 'balance', 'category', 'status', 'deadline'])
                    writer.writeheader()
                    writer.writerow(row)

            goal_progress_notification(goal.get_tottal_amount(), goal.get_balance())

        if command == 'уменьшить баланс':
            current_balance = goal.get_balance()

            while True:
                try:
                    amount = input('сумма>')

                    if not amount.strip().isdigit():
                        raise ValueError('сумма должна состоять только из цифр')

                    break
                except ValueError as error:
                    print(error)

            goal.decrease_balance(int(amount))

            if current_balance != goal.get_balance():
                with open(goal_file_src, 'r', encoding='utf-8') as goal_file:
                    reader = csv.DictReader(goal_file)
                    row = list(reader)[0]
                    row.update({'balance': goal.get_balance()})

                with open(goal_file_src, 'w', encoding='utf-8', newline='') as goal_file:
                    writer = csv.DictWriter(goal_file, ['name', 'tottal_amount', 'balance', 'category', 'status'])
                    writer.writeheader()
                    writer.writerow(row)

            goal_progress_notification(goal.get_tottal_amount(), goal.get_balance())

        if command == 'информация':
            print(f'''
                название цели - {goal.name}
                итоговая сумма - {goal.get_tottal_amount()}
                текущий баланс - {goal.get_balance()}
                название категории - {goal.category}
                статус - {goal.get_status()}
            ''')

def goal_progress_notification(tottal_amount, balance):
    percentages_list = [25, 50, 75]

    current_percent = 0

    for percent in percentages_list:
        if ((balance * 100) / tottal_amount) >= percent:
            current_percent = percent

    print(f'баланс по цели составляет {'более' if ((balance * 100) / tottal_amount) > current_percent else ''} {current_percent}% от итоговой суммы')

def print_tottal_progress():
    categoryes_folder_src = f'{os.getcwd()}/categoryes'

    balance = 0
    tottal_amount = 0

    
    for dirpath, dirnames, filenames in os.walk(categoryes_folder_src):
        if filenames == []:
            continue

        filename = filenames[0]
        with open(f'{dirpath}/{filename}', 'r', encoding='utf-8') as goal_file:
            reader = csv.DictReader(goal_file)
            for row in reader:
                balance += int(row.get('balance'))

                tottal_amount += int(row.get('tottal_amount'))

    print(f'''
    общий баланс - {balance}
    общая итоговая сумма - {tottal_amount}
    ''')

def print_commands():
    print('''
    помощь - выводит все доступные команды
    создать цель - создаёт цель с указанными атрибутами
    создать категорию - создаёт категорию с указанным названием
    удалить цель - удаляет цель с указанным названием
    ''')

def money_box():
    print('сообщение>Итоговый проект "Копилка"')
    commands_list = ['помощь', 'выход', 'создать цель', 'удалить цель', 'найти цель', 'общий прогресс']
    current_goal = None

    while True:
        while True:
            try:
                command = input('команда>')

                if not command in commands_list:
                    raise ValueError(f'ошибка>неизвестная комманда "{command}"\nсообщение>для просмотра всех допустимых комманд введите "помощь"')

                break
            except ValueError as error:
                print(error)
        if command == 'общий прогресс':
            print_tottal_progress()
        
        if command == 'удалить цель':
            delete_goal()
        
        if command == 'создать цель':
            current_goal = create_goal()

        if command == 'найти цель':
            find_goal()

        if command == 'помощь':
            print_commands()
        
        if command == 'выход':
            break

money_box()