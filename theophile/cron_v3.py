
RANGE = 0
STEP = 1

class CronRange:
    def __init__(self,_from,_to):
        self._from = _from
        self._to = _to


class CronDateEntry:
    def __init__(self,_max,_range = None, _step = 1):
        if _range and _range._to <= _max:
            self._range = _range
        else:
            self._range = CronRange(0, _max)
        self._step = _step

    def __str__(self):
        pass

class Minute(CronDateEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(60, *args, **kwargs)
class Hour(CronDateEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(24, *args, **kwargs)
class DayM(CronDateEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(31, *args, **kwargs)
class DayW(CronDateEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(7, *args, **kwargs)
class Month(CronDateEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(12, *args, **kwargs)



class Cron:

    def __init__(self):
        self._cron_dict = {Minute : [],
                        Hour : [],
                        DayM : [],
                        DayW : [],
                        Month : []}


    ##MIN
    def fromTo(self,_from,_to,_type):
        self._cron_dict[_type].append(_type(_range=CronRange(_from, _to)))
        return self

    def every(self,freq,_type):
        self._cron_dict[_type].append(_type(_step=freq))
        return self

    def at(self,_from,_to,_type):
        self._cron_dict[_type].append(_type(CronRange(_from, _to)))
        return self










    def every(self,x): 
        if len(self._cron_array[MIN]) == 0:
            self._cron_array[MIN].append({RANGE: None,STEP: x})
        else:
            self._cron_array[MIN][-1][STEP] = x
        return self
    def atMin(self,x):
        self._cron_array[MIN].append({RANGE: [x],STEP: None})
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
        if len(self._timing_array[MONTH])==0 or mo in self._timing_array[MONTH]:
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
