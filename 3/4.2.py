class Wallet:

    paymentSystem = "МИР"

    def __init__(self, name: str, currency: str, balance: float = 0):
        self.name = name
        self._balance = balance
        self.currency = currency

    def deposit(self, amount: float):
        if self._balance >= 0:
            self._balance += amount
            return self._balance  # Нужно для дебага
        else:
            return "Счета не существует или он был удален"

    def pay(self, amount: float):
        if self._balance >= 0:
            if self._balance >= amount:
                self._balance -= amount
                return self._balance  # Нужно для дебага
            else:
                return "Недостаточно средств"
        else:
            return "Счета не существует или он был удален"

    def getBalance(self):
        if self._balance >= 0:
            return f"{self._balance} {self.currency}"
        else:
            return "Счета не существует или он был удален"

    def delete(self):
        if self._balance >= 0:
            self._balance = -1
            self.name = "Счета не существует или он был удален"
            self.currency = ""
        else:
            return "Счета не существует или он был удален"


class CryptoWallet(Wallet):
    def __init__(self, name, currency, coin, balance=0):
        super().__init__(name, currency, balance)
        self.coin = coin

    def getBalance(self):
        return f"{self._balance} {self.coin}"

    def getBalanceInUsd(self):
        if self.coin == "BTC":
            return self._balance * 72000
        elif self.coin == "ETH":
            return self._balance * 3500
        else:
            return "Unknown coin"


# a1 = Wallet("Vic", "$", 5000)

# print(a1.deposit(10))
# print(a1.pay(50))
# print(a1.pay(50000))
# print(a1.getBalance())
# a1.delete()
# print(a1.deposit(10))
# print(a1.getBalance())
# print(a1.pay(50))

a2 = CryptoWallet("Vic", "$", "ETH", 5000)

print(a2.getBalance())
print(a2.getBalanceInUsd())
