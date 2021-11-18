import calendar
class Cron:

    def __init__(self):
        self.minutes = []
        self.hours = []
        self.day_month = []
        self.month = []
        self.day_week = []

    def add_minute(self, min_tab):
        for e in min_tab:
            assert (e == "*" or 0 <= e <= 59 )
        self.minutes += min_tab

    def add_hour(self, hour_tab):
        for e in hour_tab:
            assert (e == "*" or 0 <= e <= 23 )
        self.hours += hour_tab

    def add_day_month(self, day_month):
        for e in day_month:
            assert (e == "*" or 1 <= e <= 31 )
        self.day_month += day_month

    def add_month(self, month):
        for e in month:
            assert (e == "*" or 1 <= e <= 12)
        self.month += month

    def add_day_week(self, day_week):
        for e in day_week:
            assert (e == "*" or 1 <= e <= 7)
        self.day_week += day_week

    def value_of(self, number):
        return 'every' if number == '*' else number

    def express_min(self):
        minutes = "on minutes "
        for e in self.minutes:
            minutes += (str(self.value_of(e)) + " and ")
        return minutes[:-4]

    def express_hour(self):
        hours = "on hours "
        for e in self.hours:
            hours += (str(self.value_of(e)) + " and ")
        return hours[:-4]

    def express_day_month(self):
        day_month = "on date "
        for e in self.day_month:
            day_month += (str(self.value_of(e)) + " and ")
        return day_month[:-4]

    def express_day_week(self):
        day_week = "on "
        for e in self.day_week:
            if e=="*":
                day_week += "every day"  + " and "
            else:
                day_week += (calendar.day_name[e]) + " and "
        return day_week[:-4] if len(self.day_week)>0 else ""

    def express_month(self):
        months = "on "
        for e in self.month:
            if e=="*":
                months += "every month "
            else:
                months += (str(calendar.month_name[e]) + " and ")
        return months[:-4]

    def express(self):
        return "this task is scheduled " + self.express_min()\
                                         +self.express_hour()\
                                         +self.express_day_month()\
                                         +self.express_month()\
                                         +self.express_day_week()


cron = Cron()
cron.add_minute([5,25])

cron.add_hour([12])
cron.add_day_month([12])
cron.add_month([6])
cron.add_day_week([1,6])

print(cron.express())
