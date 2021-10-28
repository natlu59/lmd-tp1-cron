class Cron:

    def __init__(self):
        self._funk = ""
        self._daysOfWeek = []
        self._months = []
        self._daysOfMonth = []
        self._hours = []
        self._minutes = []

    def funk(self, s):
        self._funk = s
        return self

    def daysOfWeek(self, m):
        self._daysOfWeek.append(m)
        return self

    def months(self, m):
        self._months.append(m)
        return self

    def daysOfMonth(self, m):
        self._daysOfMonth.append(m)
        return self

    def hours(self, m):
        self._hours.append(m)
        return self

    def minutes(self, m):
        self._minutes.append(m)
        return self

    def iterateCron(self, var):
        res = ""
        for m in var:
            if isinstance(m, int):
                res = res + str(m)
            elif isinstance(m, tuple):
                res = res + m[0] + '-' + m[1]
            elif isinstance(m, list):
                for mm in m:
                    res = res + mm
            elif m == '*':
                res = res + '*'
            res = res + ','
        return res[:-1] + ' '

    def generateCron(self):
        return self.iterateCron(self._minutes) + self.iterateCron(self._hours) + self.iterateCron(self._daysOfMonth) + \
               self.iterateCron(self._months) + self.iterateCron \
                   (self._daysOfWeek) + self._funk


cron=Cron().minutes(12).hours(23)
print(cron.generateCron())