class Data:

    def __init__(self, data: str, list1):
        self.data = data
        self.list1 = list1

    def __str__(self):
        return f'day: {self.list1[0]}, month: {self.list1[1]}, year: {self.list1[2]}'

    @classmethod
    def beauty(cls, data0: str, list1):
        list = data0.split('-')
        list1 = []
        for u in range(len(list)):
            list1.append(int(list[u]))
        return Data(data0, list1)

    @staticmethod
    def check(obj):
        if obj.list1[1] > 12 or obj.list1[1] < 1 or obj.list1[0] < 1 or obj.list1[0] > 31:
            return print('error')
        else:
            return print('OK')


event = Data.beauty('01-09-2022', [])
event1 = Data.beauty('40-09-2022', [])
event2 = Data.beauty('01-40-2022', [])
print(event)
Data.check(event)
Data.check(event1)
Data.check(event2)
