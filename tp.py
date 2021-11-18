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

    def iterateString(self, var, varName):
        res = ""
        for m in var:
            if isinstance(m, int):
                res += varName + ' ' + str(m)
            elif isinstance(m, tuple):
                res += 'every ' + varName + ' from ' + m[0] + ' through ' + m[1]
            elif isinstance(m, list):
                res += self.iterateString(self, m)
            elif m == '*':
                res += 'every ' + varName
            
            if len(var) > 1 and m == var[-2]:
                res += ' and'
            elif m != var[-1]:
                res += ','

            res += ' '
        return res
    
    def generateString(self):
        res = ''
        if self._minutes:
            res += "At "    + self.iterateString(self._minutes    , 'minute'      )
        if self._hours:
            res += "past " + self.iterateString(self._hours      , 'hour'        )
        if self._daysOfMonth:
            res += "on "   + self.iterateString(self._daysOfMonth, 'day-of-month')
        if self._months:
            res += "in "   + self.iterateString(self._months     , 'month'       )
        return res



cron = Cron().daysOfMonth(2).minutes(15).hours(('0','6')).daysOfMonth('*').minutes(45)
print(cron.generateCron())
print(cron.generateString())