from datetime import datetime


class Payment:

    def __init__(self, Name=' ', oklad=0, year=0, percent=0, Worked_days=0, working_day=1):
        self.__Name = str(Name)
        self.__oklad = int(oklad)
        self.__year = int(year)
        self.__percent = float(percent)
        self.__Worked_days = int(Worked_days)
        self.__working_day = int(working_day)
        self.amount = 0
        self.heldAmount = 0
        self.handAmount = 0
        self.expir= 0

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def accruedAmount(self):
        a = self.__oklad / self.__working_day
        b = a * self.__Worked_days
        percent = self.__percent / 100 + 1
        self.amount = b * percent

    def withheldAmount(self):
        plata = (self.__oklad / self.__working_day) * self.__Worked_days
        self.heldAmount = (plata * 0.13) + (plata * 0.01)

    def handedAmount(self):
        self.handAmount = self.amount - self.heldAmount

    def experience(self):
        self.expir = datetime.now().year - self.__year

    def __round__(self, n=0):
        return round(self.handAmount)

    def __str__(self):
        return f"Опыт работы: {self.expir} год/года/лет \nРасчеты: {self.amount} - {self.heldAmount} = {self.handAmount}"

    def __lt__(self, other):
        return self.__oklad < other.__oklad

    def __eq__(self, other):
        return self.__working_day == other.__working_day

    def __ne__(self, other):
        return self.__percent != other.__percent

    def __gt__(self, other):
        return self.__Worked_days > other.__Worked_days

    def __ge__(self, other):
        return self.expir >= other.expir

    def __le__(self, other):
        return self.handAmount <= other.handAmount

    def __truediv__(self, other):
        if self.__oklad >= other.__oklad:
            return self.__oklad / other.__oklad
        else:
            return other.__oklad / self.__oklad

    def __mul__(self, other):
        return self.__percent * other.__percent

    def __sub__(self, other):
        if self.__Worked_days >= other.__Worked_days:
            return self.__Worked_days - other.__Worked_days
        else:
            return other.__Worked_days - self.__Worked_days

    def __add__(self, other):
        return self.__working_day + other.__working_day