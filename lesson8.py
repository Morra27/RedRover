'''Интернет-банк
- Создайте класс BankAccount, который принимает имя владельца (name) в виде строки и текущее состояние счета (balance) в виде целого числа. Оба
этих атрибута должны быть _защищенным.
- Создайте метод deposit(), который принимает 1 аргумент (если не считать self, конечно) amount (целое число). Метод должен увеличить текущий
баланс аккаунта на amount.
- Создайте метод withdraw(), который принимает 1 аргумент amount (целое число). Метод должен уменьшить текущий баланс аккаунта на amount. Если
денег на счету недостаточно, то метод выводит на экран “Недостаточно средств!”.
- Создайте метод get_balance(), который возвращает текущее значение баланса аккаунта.
'''

class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        return self

    def withdraw(self, amount):
        if self._balance < amount:
            print(f'Недостаточно средств {self._balance}')
        else: self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(2000)
print(account.get_balance()) # 1500
'''
Создайте класс OverdraftAccount, унаследованный от вашего класса BankAccount из предыдущей задачи.
- Переопределите существующий метод withdraw(), но теперь, если баланс аккаунта меньше или равен 0, то это не выводит на экран сообщение
“Недостаточно средств!”, а уменьшает баланс в минус.
'''

class OverdraftAccount(BankAccount):
    def withdraw(self, amount):
        self._balance -= amount

account = OverdraftAccount("Maria", 1000)
account.withdraw(2000)
print(account.get_balance())