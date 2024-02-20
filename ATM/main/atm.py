class ATM:
    def __init__(self, denominations):
        self.denominations = denominations

    def withdraw(self, amount):
        total = sum(bill * count for bill, count in self.denominations.items())
        if amount > total:
            return "Недостатньо грошей в банкоматі"

        result = {}
        for denom in sorted(self.denominations.keys(), reverse=True):
            if denom <= amount and self.denominations[denom] > 0:
                num = min(amount // denom, self.denominations[denom])
                result[denom] = num
                amount -= denom * num
                self.denominations[denom] -= num

        if amount != 0:
            return "Неможливо виконати операцію з вибраним номіналом"
        else:
            return result


# Приклад використання
atm = ATM({50: 10, 20: 10, 10: 10, 5: 10})
print(atm.withdraw(100))
