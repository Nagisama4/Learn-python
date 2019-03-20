import time

def get_week_day(year, month, day):
    time_tuple = time.strptime("%d/%d/%d"%(year, month, day), "%Y/%m/%d")
    week_day_dict = {
        0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天',
    }
    return week_day_dict[time_tuple[6]]

print(get_week_day(2019, 3, 24))