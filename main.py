class Goal:
    def __init__(self, name: str, tottal_amount: int, balance: int, category: str, status: str):
        self.name = name
        self.total_amount = tottal_amount
        self.balance = balance
        self.category = category
        self.status = status

    def increase_balance(self, amount: int):
        try:
            if self.balance + amount > self.total_amount:
                raise ValueError(f'Баланс не может превышать итоговой суммы цели ({self.balance} + {amount} > {self.total_amount})')

            self.balance += amount
        except ValueError as error:
            print(error)

    def decrease_balance(self, amount: int):
        try:
            if self.balance - amount < 0:
                raise ValueError(f'Баланс не может быть отрицательным ({self.balance} - {amount} < 0)')

            self.balance -= amount
        except ValueError as error:
            print(error)

    def get_percentage_of_progress(self):
        result = (self.balance * 100) / self.total_amount

        return result