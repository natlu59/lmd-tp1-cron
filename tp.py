

class cron():

    def __init__(self):
        self.funk=""
        self.daysOfWeek  = []
        self.months      = []
        self.daysOfMonth = []
        self.hours       = []
        self.minutes     = []


    def funk(s, self):
        self.funk=s
        return self

    def daysOfWeek(m, self):
        self.daysOfWeek.append(m)
        return self

    def months(m, self):
        self.months.append(m)
        return self

    def daysOfMonth(m, self):
        self.daysOfMonth.append(m)
        return self

    def hours(m, self):
        self.hours.append(m)
        return self

    def minutes(m, self):
        self.minutes.append(m)
        return self
    
    def iterateCron(var):
        res = ""
        for m in var:
            if(isinstance(m,int)):
                res = res + m
            elif(isinstance(m,tuple)):
                res = res + m[0] + '-' + m[1]
            elif(isinstance(m,list)):
                for mm in m:
                    res = res + mm
            elif(m == '*'):
                res = res + '*'
            res = res + ','
        return res[:-1] + ' '
    
    def generateCron(self):
        return iterateCron(minutes) + iterateCron(hours) + iterateCron(daysOfMonth) + iterateCron(months) + iterateCron(daysOfWeek) + funk


cron.minutes(15).minutes(16)