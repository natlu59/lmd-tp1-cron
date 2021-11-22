from typing import ItemsView


class Cron:

    def __init__(self):
        self._minutes     = []
        self._hours       = []
        self._daysOfMonth = []
        self._months      = []
        self._daysOfWeek  = []
        self._func        = ""

    def minutes(self, m):
        if isinstance(m, list):
            for mm in m:
                self.minutes(mm)
        if isinstance(m, int):
            assert(m == "*" or 0 <= m <= 59)
        if isinstance(m, tuple):
            assert(isinstance(m[0], int) and isinstance(m[1], int))
            assert(0 <= m[0] <= 59 or 0 <= m[1] <= 59)
        self._minutes.append(m)
        return self

    def hours(self, m):
        if isinstance(m, list):
            for mm in m:
                self.hours(mm)
        if isinstance(m, int):
            assert(m == '*' or 0 <= m <= 23)
        if isinstance(m, tuple):
            assert(isinstance(m[0], int) and isinstance(m[1], int))
            assert(0 <= m[0] <= 23 or 0 <= m[1] <= 23)
        self._hours.append(m)
        return self

    def daysOfMonth(self, m):
        if isinstance(m, list):
            for mm in m:
                self.daysOfMonth(mm)
        if isinstance(m, int):
            assert(m == "*" or 1 <= m <= 31)
        if isinstance(m, tuple):
            assert(isinstance(m[0], int) and isinstance(m[1], int))
            assert(1 <= m[0] <= 31 or 1 <= m[1] <= 31)
        self._daysOfMonth.append(m)
        return self
    
    def months(self, m):
        if isinstance(m, list):
            for mm in m:
                self.months(mm)
        if isinstance(m, int):
            assert(m == "*" or 1 <= m <= 12)
        if isinstance(m, tuple):
            assert(isinstance(m[0], int) and isinstance(m[1], int))
            assert(1 <= m[0] <= 12 or 1 <= m[1] <= 12)
        self._months.append(m)
        return self

    def daysOfWeek(self, m):
        if isinstance(m, list):
            for mm in m:
                self.daysOfWeek(mm)
        if isinstance(m, int):
            assert(m == "*" or 1 <= m <= 7)
        if isinstance(m, tuple):
            assert(isinstance(m[0], int) and isinstance(m[1], int))
            assert(1 <= m[0] <= 7 or 1 <= m[1] <= 7)
        self._daysOfWeek.append(m)
        return self

    def func(self, s):
        self._func = s
        return self

    def iterateCron(self, var):
        res = ""
        for m in var:
            if isinstance(m, int):
                res = res + str(m)
            elif isinstance(m, tuple):
                res = res + str(m[0]) + '-' + str(m[1])
            elif m == '*':
                res = res + '*'
            res = res + ','
        return res[:-1] + ' '

    def generateCron(self):
        res = ''
        if self._minutes and self._hours and self._daysOfMonth and self._months and self._daysOfWeek and self._func:
            res += self.iterateCron(self._minutes)
            res += self.iterateCron(self._hours)
            res += self.iterateCron(self._daysOfMonth)
            res += self.iterateCron(self._months)
            res += self.iterateCron(self._daysOfWeek)
            res += self._func
        else:
            res += 'The fields minutes, hours, daysOfMonth, months, daysOfWeek and func should not be empty'
        return res

    def iterateString(self, var, varName):
        res = ""
        for m in var:
            if isinstance(m, int):
                res += varName + ' ' + str(m)
            elif isinstance(m, tuple):
                res += 'every ' + varName + ' from ' + str(m[0]) + ' through ' + str(m[1])
            elif m == '*':
                res += 'every ' + varName
            # import ipdb; ipdb.set_trace()
            res += ' '
        return res
    
    def generateString(self):
        res = ''
        if self._minutes and self._hours and self._daysOfMonth and self._months and self._daysOfWeek and self._func:
            res += "At "   + self.iterateString(self._minutes    , 'minute'      )
            res += "past " + self.iterateString(self._hours      , 'hour'        )
            res += "on "   + self.iterateString(self._daysOfMonth, 'day-of-month')
            res += "on "   + self.iterateString(self._daysOfWeek , 'days-of-Week')
            res += "in "   + self.iterateString(self._months     , 'month'       )
        else:
            res += 'The fields minutes, hours, daysOfMonth, months, daysOfWeek and func should not be empty'
        return res



cron = Cron()



(   cron.minutes(2)
        .hours([(0,6), 15, 20])            
        .daysOfMonth(4)                        
        .months(5)
        .daysOfWeek(6)                      
        .func("Florian_qui_mange_un_kebab.sh")
)



print(cron.generateCron())
print()
print(cron.generateString())