

MIN = 0
HOUR = 1
DAY_M = 2
MONTH = 3
DAY_W = 4

RANGE = 0
STEP = 1

class Cron:

    def __init__(self):
        self._cron_array = [[],[],[],[],[]]
        self._timing_array = []

    ##MIN
    def fromToMin(self,_from,_to):
        self._cron_array[MIN].append({RANGE: [_from,_to],STEP: None})
        return self
    def everyMin(self,x):
        if len(self._cron_array[MIN]) == 0:
            self._cron_array[MIN].append({RANGE: None,STEP: x})
        else:
            self._cron_array[MIN][-1][STEP] = x
        return self
    def atMin(self,x):
        self._cron_array[MIN].append({RANGE: [x],STEP: None})
        return self
    ##HOUR
    def fromToHour(self,_from,_to):
        self._cron_array[HOUR].append({RANGE: [_from,_to],STEP: None})
        return self
    def everyHour(self,x):
        if len(self._cron_array[HOUR]) == 0:
            self._cron_array[HOUR].append({RANGE: None,STEP: x})
        else:
            self._cron_array[HOUR][-1][STEP] = x
        return self
    def atHour(self,x):
        self._cron_array[HOUR].append({RANGE: [x],STEP: None})
        return self
    ##DAY_M
    def fromToDayM(self,_from,_to):
        self._cron_array[DAY_M].append({RANGE: [_from,_to],STEP: None})
        return self
    def everyDayM(self,x):
        if len(self._cron_array[DAY_M]) == 0:
            self._cron_array[DAY_M].append({RANGE: None,STEP: x})
        else:
            self._cron_array[DAY_M][-1][STEP] = x
        return self
    def atDayM(self,x):
        self._cron_array[DAY_M].append({RANGE: [x],STEP: None})
        return self
    ##MONTH
    def fromToMonth(self,_from,_to):
        self._cron_array[MONTH].append({RANGE: [_from,_to],STEP: None})
        return self
    def everyMonth(self,x):
        if len(self._cron_array[MONTH]) == 0:
            self._cron_array[MONTH].append({RANGE: None,STEP: x})
        else:
            self._cron_array[MONTH][-1][STEP] = x
        return self
    def atMonth(self,x):
        self._cron_array[MONTH].append({RANGE: [x],STEP: None})
        return self
    ##DAY_W
    def fromToDayW(self,_from,_to):
        self._cron_array[DAY_W].append({RANGE: [_from,_to],STEP: None})
        return self
    def everyDayW(self,x):
        if len(self._cron_array[DAY_W]) == 0:
            self._cron_array[DAY_W].append({RANGE: None,STEP: x})
        else:
            self._cron_array[DAY_W][-1][STEP] = x
        return self
    def atDayW(self,x):
        self._cron_array[DAY_W].append({RANGE: [x],STEP: None})
        return self

    def done(self):
        _type = 0
        for date_type in self._cron_array:
            self._timing_array.append([])
            for entry in date_type:
                f = 0
                to = 0
                mod = 1
                if entry[RANGE]==None:
                    if _type == MIN:
                        to = 59
                    if _type == HOUR:
                        to = 23
                    if _type == DAY_M:
                        to = 30
                    if _type == MONTH:
                        to = 11
                    if _type == DAY_W:
                        to = 6 
                elif len(entry[RANGE]) == 1:
                    f = entry[RANGE][0]
                    to = entry[RANGE][0]
                else:
                    f = entry[RANGE][0]
                    to = entry[RANGE][1]
                if entry[STEP] != None:
                    mod = entry[STEP]
                for n in range(f,to+1):
                    if n % mod == 0:
                        self._timing_array[-1].append(n)                     
            _type+=1
        return self

    def checkDate(self,m,h,dm,dw,mo):
        
        if m any(m in r for r in self.hours)
            if len(self._timing_array[DAY_W])==0 or dw in self._timing_array[DAY_W]:
                if len(self._timing_array[DAY_M])==0 or dm in self._timing_array[DAY_M]:
                    if len(self._timing_array[HOUR])==0 or h in self._timing_array[HOUR]:
                        if len(self._timing_array[MIN])==0 or m in self._timing_array[MIN]:
                            return True
        return False

    def __str__(self):
        res = ""
        for date_type in self._cron_array:
            if len(date_type)== 0:
                res+="*"
            else:
                for entry in date_type:
                    if entry[RANGE]==None:
                        res+="*"
                    elif len(entry[RANGE]) == 1:
                        res+=str(entry[RANGE][0])
                    else:
                        res+=str(entry[RANGE][0])+"-"+str(entry[RANGE][1])
                    if entry[STEP]!=None:
                        res+="/"+str(entry[STEP])
                    res+=","
            if res[-1] == ",":
                res = res[:-1]
            res+=" "
        return res
    def nextDate(self):
        pass

  



cron = Cron().everyMin(2).fromToMin(0, 5).everyMin(2).atMin(9).atMin(32).atMin(12).fromToHour(4,10).everyHour(3).done()

print(cron)
#print(cron._timing_array)
print(cron.checkDate(4,5,23,4,2))
