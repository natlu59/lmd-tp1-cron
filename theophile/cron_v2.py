

MIN = 0
HOUR = 1
DAY_M = 2
MONTH = 3
DAY_W = 4

RANGE = 0
STEP = 1

class Cron:

    def __init__(self):
        self._cron_array = [[],[],[],[],[],[]]

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
  
    ##TODO



    def toString(self):
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


cron = Cron().fromToMin(0, 5).everyMin(2).atMin(9).atMin(12)
print(cron.toString())