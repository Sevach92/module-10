import threading
import time
import random



class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            transaction = random.randint(50, 500)
            self.balance += transaction
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение {transaction}. Баланс:  {self.balance}.')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            transaction = random.randint(50, 500)
            print(f'Запрос на {transaction}.')
            if transaction <= self.balance:
                self.balance -= transaction
                print(f'Снятие {transaction}. Баланс: {self.balance}.')
            if transaction > self.balance:
                print(f'Запрос отклонен,недостаточно средств.')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')