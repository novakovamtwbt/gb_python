class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'okay'
                else:
                    return f'incorrect year'
            else:
                return f'incorrect month'
        else:
            return f'incorrect day'

    def __str__(self):
        return f'Date {Data.extract(self.day_month_year)}'


today = Data('20 - 7 - 2021')
print(today)
print(Data.valid(20, 7, 2021))
print(today.valid(11, 13, -4567))
print(Data.extract('30 - 7 - 2021'))
print(today.extract('20 - 7 - 2021'))
print(Data.valid(1, 11, 2000))
